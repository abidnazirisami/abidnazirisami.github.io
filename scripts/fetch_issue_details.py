#!/usr/bin/env python3
"""
Fetch GitHub issue and pull request details for bugs listed in bugs/*.csv.

Saves structured JSON data for each bug so that LLM agents and scripts can inspect
issue status, maintainer comments, PR merge state, and labels offline without
needing to fetch information from the web.

Key features:
- Reads all bugs CSV files in bugs/ (ignoring raw source files like rq3_bugs_reported.csv).
- Uses $GITHUB_TOKEN environment variable or --token CLI flag.
- Pulls issue metadata, comments, and PR details from GitHub API.
- Supports both GitHub issues (/issues/<num>) and GitHub pull requests (/pull/<num>).
- Gracefully handles external trackers (Bugzilla, PostgreSQL, etc.) and records them.
- If existing entries exist, updates them (using HTTP conditional requests/ETags
  for efficiency and quota preservation).
- Saves issue details to a gitignored directory (default: bugs_data/).
- Generates a summary.json index for quick scanning by LLM agents.
- Ensures the data directory is added to .gitignore.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import parse_qs, urlparse

import requests

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUGS_DIR = REPO_ROOT / "bugs"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "bugs_data"
GITIGNORE_PATH = REPO_ROOT / ".gitignore"

GITHUB_API_BASE = "https://api.github.com"
ISSUE_URL_RE = re.compile(
    r"https?://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)/(?P<type>issues|pull)/(?P<number>\d+)"
)

# Raw multi-app datasets to skip when scanning bugs directory
RAW_DATASETS_TO_SKIP = {"rq3_bugs_reported.csv"}


def ensure_gitignored(target_dir: Path, gitignore_path: Path = GITIGNORE_PATH) -> bool:
    """Ensure the target directory path or pattern is present in .gitignore."""
    try:
        rel_path = target_dir.relative_to(REPO_ROOT).as_posix().rstrip("/") + "/"
    except ValueError:
        rel_path = target_dir.name.rstrip("/") + "/"

    if not gitignore_path.exists():
        gitignore_path.write_text(f"{rel_path}\n", encoding="utf-8")
        return True

    content = gitignore_path.read_text(encoding="utf-8")
    patterns = [line.strip() for line in content.splitlines()]

    # Check if directory or pattern is already covered
    pattern_candidates = {rel_path, rel_path.rstrip("/"), f"**/{rel_path}", f"/{rel_path}"}
    if any(p in pattern_candidates for p in patterns):
        return False

    # Append to .gitignore
    with gitignore_path.open("a", encoding="utf-8") as f:
        if content and not content.endswith("\n"):
            f.write("\n")
        f.write(f"\n# Cached GitHub bug data (gitignored for LLM agent use)\n{rel_path}\n")
    return True


def read_bugs_csv(csv_path: Path) -> List[Dict[str, str]]:
    """
    Read bug entries from a CSV file.
    Skips preamble lines until the header row containing 'link' is found.
    """
    rows = []
    if not csv_path.exists():
        return rows

    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = None
        for r in reader:
            if not r or all(not c.strip() for c in r):
                continue
            if "link" in r:
                headers = [h.strip() for h in r]
                break

        if headers is None:
            return rows

        dict_reader = csv.DictReader(f, fieldnames=headers)
        for row in dict_reader:
            clean_row = {k.strip(): (v.strip() if v else "") for k, v in row.items() if k}
            if clean_row.get("link"):
                rows.append(clean_row)
    return rows


def parse_github_url(url: str) -> Optional[Tuple[str, str, str, int]]:
    """
    Parse a GitHub issue or pull URL into (owner, repo, type, number).
    Example: https://github.com/pytorch/pytorch/issues/139342 -> ('pytorch', 'pytorch', 'issues', 139342)
    """
    if not url:
        return None
    match = ISSUE_URL_RE.search(url.strip())
    if match:
        owner = match.group("owner")
        repo = match.group("repo")
        item_type = match.group("type")
        number = int(match.group("number"))
        return owner, repo, item_type, number
    return None


def parse_external_url(url: str) -> Dict[str, str]:
    """Parse a non-GitHub URL into metadata (domain, extracted issue id/token)."""
    parsed = urlparse(url.strip())
    domain = parsed.netloc.lower()

    # Try extracting id from query (e.g. ?id=4008)
    query_params = parse_qs(parsed.query)
    issue_id = ""
    if "id" in query_params:
        issue_id = query_params["id"][0]
    else:
        # Try finding trailing numeric component in path (e.g. /submitbug/19730/)
        num_match = re.search(r"/(\d+)/?$", parsed.path)
        if num_match:
            issue_id = num_match.group(1)
        else:
            issue_id = re.sub(r"[^a-zA-Z0-9_-]", "_", parsed.path.strip("/")) or "index"

    tracker_name = "bugzilla" if "bugzilla" in domain else domain
    return {
        "domain": domain,
        "tracker_name": tracker_name,
        "issue_id": issue_id,
        "url": url.strip(),
    }


class GitHubIssueFetcher:
    """Manages fetching and updating GitHub issue and PR details with caching."""

    def __init__(
        self,
        token: Optional[str] = None,
        session: Optional[requests.Session] = None,
        verbose: bool = False,
    ):
        self.token = token or os.environ.get("GITHUB_TOKEN")
        self.session = session or requests.Session()
        self.verbose = verbose

        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "antigravity-bugs-fetcher/1.0",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        self.session.headers.update(headers)

    def check_rate_limit(self) -> Dict[str, Any]:
        """Fetch current rate limit status."""
        try:
            r = self.session.get(f"{GITHUB_API_BASE}/rate_limit", timeout=10)
            if r.status_code == 200:
                core = r.json().get("resources", {}).get("core", {})
                return {
                    "limit": core.get("limit"),
                    "remaining": core.get("remaining"),
                    "reset": core.get("reset"),
                    "reset_datetime": (
                        datetime.fromtimestamp(core.get("reset", 0), tz=timezone.utc).isoformat()
                        if core.get("reset")
                        else None
                    ),
                }
        except Exception as e:
            if self.verbose:
                print(f"[Warning] Failed to check rate limit: {e}", file=sys.stderr)
        return {}

    def fetch_issue(
        self,
        owner: str,
        repo: str,
        number: int,
        etag: Optional[str] = None,
    ) -> Tuple[int, Optional[Dict[str, Any]], Optional[str]]:
        """
        Fetch issue data using conditional GET (If-None-Match: etag).
        Works for both issues and pull requests via GitHub's unified issues API.
        Returns: (status_code, json_data_or_None, new_etag_or_None)
        """
        url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/issues/{number}"
        headers = {}
        if etag:
            headers["If-None-Match"] = etag

        r = self.session.get(url, headers=headers, timeout=20)
        new_etag = r.headers.get("ETag")

        if r.status_code == 304:
            return 304, None, etag
        elif r.status_code == 200:
            return 200, r.json(), new_etag
        else:
            return r.status_code, None, None

    def fetch_comments(
        self,
        owner: str,
        repo: str,
        number: int,
        etag: Optional[str] = None,
    ) -> Tuple[int, Optional[List[Dict[str, Any]]], Optional[str]]:
        """
        Fetch issue comments using conditional GET.
        Returns: (status_code, comments_list_or_None, new_etag_or_None)
        """
        url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/issues/{number}/comments"
        headers = {}
        if etag:
            headers["If-None-Match"] = etag

        r = self.session.get(url, headers=headers, timeout=20)
        new_etag = r.headers.get("ETag")

        if r.status_code == 304:
            return 304, None, etag
        elif r.status_code == 200:
            raw_comments = r.json()
            cleaned_comments = []
            for c in raw_comments:
                cleaned_comments.append(
                    {
                        "id": c.get("id"),
                        "author": (c.get("user") or {}).get("login"),
                        "author_association": c.get("author_association"),
                        "created_at": c.get("created_at"),
                        "updated_at": c.get("updated_at"),
                        "html_url": c.get("html_url"),
                        "body": c.get("body", ""),
                    }
                )
            return 200, cleaned_comments, new_etag
        else:
            return r.status_code, None, None

    def fetch_pull_request(
        self,
        owner: str,
        repo: str,
        number: int,
        etag: Optional[str] = None,
    ) -> Tuple[int, Optional[Dict[str, Any]], Optional[str]]:
        """
        Fetch pull request details using conditional GET.
        Returns: (status_code, pr_data_or_None, new_etag_or_None)
        """
        url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/pulls/{number}"
        headers = {}
        if etag:
            headers["If-None-Match"] = etag

        r = self.session.get(url, headers=headers, timeout=20)
        new_etag = r.headers.get("ETag")

        if r.status_code == 304:
            return 304, None, etag
        elif r.status_code == 200:
            pr = r.json()
            cleaned_pr = {
                "number": pr.get("number"),
                "title": pr.get("title"),
                "state": pr.get("state"),
                "merged": pr.get("merged", False),
                "mergeable": pr.get("mergeable"),
                "merged_at": pr.get("merged_at"),
                "merged_by": (pr.get("merged_by") or {}).get("login"),
                "created_at": pr.get("created_at"),
                "updated_at": pr.get("updated_at"),
                "closed_at": pr.get("closed_at"),
                "html_url": pr.get("html_url"),
                "head_ref": (pr.get("head") or {}).get("ref"),
                "base_ref": (pr.get("base") or {}).get("ref"),
            }
            return 200, cleaned_pr, new_etag
        else:
            return r.status_code, None, None


def analyze_bug_status(
    csv_records: List[Dict[str, str]],
    github_state: Optional[str],
    github_state_reason: Optional[str],
    labels: List[str],
    pr_details: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    Perform heuristic status analysis to aid LLM agents in detecting updates.
    """
    csv_statuses = list({r.get("Status", "").strip() for r in csv_records if r.get("Status")})
    primary_csv_status = csv_statuses[0] if csv_statuses else ""

    is_closed = github_state == "closed"
    has_merged_pr = bool(pr_details and pr_details.get("merged"))
    has_open_pr = bool(pr_details and pr_details.get("state") == "open")

    lower_labels = [l.lower() for l in labels]
    is_rejected_label = any(
        term in l for l in lower_labels for term in ["wontfix", "invalid", "not-a-bug", "rejected"]
    )
    is_triaged_label = any("triaged" in l for l in lower_labels)

    # Detect possible discrepancy between CSV status and GitHub reality
    discrepancy = False
    suggested_status = primary_csv_status

    is_pending_status = primary_csv_status in ["Submitted", "Pending", "submitted", "pending"]

    if has_merged_pr and primary_csv_status not in ["Fixed", "Previously Fixed"]:
        discrepancy = True
        suggested_status = "Fixed"
    elif is_closed and github_state_reason == "completed" and is_pending_status:
        discrepancy = True
        suggested_status = "Fixed"
    elif is_closed and (github_state_reason == "not_planned" or is_rejected_label) and primary_csv_status != "Rejected":
        discrepancy = True
        suggested_status = "Rejected"
    elif not is_closed and is_pending_status and is_triaged_label:
        discrepancy = True
        suggested_status = "Confirmed"

    return {
        "csv_status": primary_csv_status,
        "all_csv_statuses": csv_statuses,
        "github_state": github_state,
        "github_state_reason": github_state_reason,
        "is_closed": is_closed,
        "has_merged_pr": has_merged_pr,
        "has_open_pr": has_open_pr,
        "discrepancy_detected": discrepancy,
        "suggested_status": suggested_status,
    }


def process_external_issue(
    url: str,
    csv_records: List[Dict[str, str]],
    dest_path: Path,
) -> Tuple[str, Dict[str, Any]]:
    """Record an issue from an external (non-GitHub) tracker."""
    ext = parse_external_url(url)
    primary = csv_records[0] if csv_records else {}
    action = "unchanged" if dest_path.exists() else "created"

    data = {
        "tracker_type": "external",
        "tracker_domain": ext["domain"],
        "tracker_name": ext["tracker_name"],
        "issue_id": ext["issue_id"],
        "html_url": url,
        "title": primary.get("note") or primary.get("api(s)") or "",
        "api": primary.get("api(s)", ""),
        "csv_status": primary.get("Status", "Pending"),
        "bug_type": primary.get("bug_type", ""),
        "tool": primary.get("tool", ""),
        "csv_records": csv_records,
        "status_analysis": {
            "csv_status": primary.get("Status", "Pending"),
            "all_csv_statuses": [primary.get("Status", "Pending")],
            "github_state": "external",
            "is_closed": False,
            "discrepancy_detected": False,
            "suggested_status": primary.get("Status", "Pending"),
        },
        "_fetch_metadata": {
            "tracker": ext["domain"],
            "last_checked_at": datetime.now(timezone.utc).isoformat(),
        },
    }

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = dest_path.with_suffix(".tmp")
    temp_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    temp_path.replace(dest_path)

    return action, data


def process_issue(
    fetcher: GitHubIssueFetcher,
    owner: str,
    repo: str,
    number: int,
    item_type: str,
    csv_records: List[Dict[str, str]],
    dest_path: Path,
    fetch_comments_flag: bool = True,
    fetch_pr_flag: bool = True,
    force: bool = False,
    verbose: bool = False,
) -> Tuple[str, Dict[str, Any]]:
    """
    Fetch or update a single GitHub issue or pull request entry.
    Returns: (action_status, issue_data_dict)
    action_status: 'created', 'updated', 'unchanged', or 'error'
    """
    existing_data: Optional[Dict[str, Any]] = None
    if dest_path.exists() and not force:
        try:
            existing_data = json.loads(dest_path.read_text(encoding="utf-8"))
        except Exception:
            existing_data = None

    fetch_meta = (existing_data or {}).get("_fetch_metadata", {})
    issue_etag = None if force else fetch_meta.get("etag")
    comments_etag = None if force else fetch_meta.get("comments_etag")
    pr_etag = None if force else fetch_meta.get("pr_etag")

    # 1. Fetch / Update Issue (GitHub API unified issues endpoint handles issues & PRs)
    status_code, raw_issue, new_issue_etag = fetcher.fetch_issue(owner, repo, number, etag=issue_etag)

    if status_code == 304 and existing_data:
        # Issue unchanged on GitHub
        issue_data = existing_data
        action = "unchanged"
    elif status_code == 200 and raw_issue:
        # Issue newly fetched or updated
        labels_list = [
            {"name": l.get("name"), "description": l.get("description", "")}
            for l in raw_issue.get("labels", [])
        ]
        is_pr_item = item_type == "pull" or bool(raw_issue.get("pull_request"))
        issue_data = {
            "issue_number": number,
            "repo_owner": owner,
            "repo_name": repo,
            "html_url": raw_issue.get("html_url"),
            "title": raw_issue.get("title"),
            "github_state": raw_issue.get("state"),
            "github_state_reason": raw_issue.get("state_reason"),
            "author": (raw_issue.get("user") or {}).get("login"),
            "created_at": raw_issue.get("created_at"),
            "updated_at": raw_issue.get("updated_at"),
            "closed_at": raw_issue.get("closed_at"),
            "closed_by": (raw_issue.get("closed_by") or {}).get("login"),
            "labels": labels_list,
            "assignees": [(u or {}).get("login") for u in raw_issue.get("assignees", [])],
            "milestone": (raw_issue.get("milestone") or {}).get("title"),
            "comments_count": raw_issue.get("comments", 0),
            "body": raw_issue.get("body", ""),
            "pull_request_ref": is_pr_item,
            "comments": existing_data.get("comments", []) if existing_data else [],
            "pull_request": existing_data.get("pull_request") if existing_data else None,
            "_fetch_metadata": {
                "etag": new_issue_etag,
                "comments_etag": comments_etag,
                "pr_etag": pr_etag,
            },
        }
        action = "updated" if existing_data else "created"
    else:
        err_msg = f"GitHub API returned HTTP {status_code} for {owner}/{repo}#{number}"
        if verbose:
            print(f"[Error] {err_msg}", file=sys.stderr)
        if existing_data:
            existing_data["_last_fetch_error"] = err_msg
            return "error", existing_data
        return "error", {
            "issue_number": number,
            "repo_owner": owner,
            "repo_name": repo,
            "html_url": f"https://github.com/{owner}/{repo}/issues/{number}",
            "error": err_msg,
            "status_code": status_code,
        }

    # 2. Update Comments if enabled
    comments_count = issue_data.get("comments_count", 0)
    if fetch_comments_flag and comments_count > 0:
        need_comments_fetch = (
            force
            or action in ["created", "updated"]
            or not issue_data.get("comments")
            or len(issue_data.get("comments", [])) != comments_count
        )
        if need_comments_fetch:
            c_code, new_comments, new_comments_etag = fetcher.fetch_comments(
                owner, repo, number, etag=comments_etag
            )
            if c_code == 200 and new_comments is not None:
                issue_data["comments"] = new_comments
                issue_data["_fetch_metadata"]["comments_etag"] = new_comments_etag
            elif c_code == 304 and existing_data:
                issue_data["comments"] = existing_data.get("comments", [])

    # 3. Handle Pull Request if linked in CSV, referenced by issue, or if item itself is a PR
    pr_target = None
    if item_type == "pull" or issue_data.get("pull_request_ref"):
        pr_target = (owner, repo, number)
    else:
        for r in csv_records:
            if r.get("pr_link"):
                parsed_pr = parse_github_url(r["pr_link"].strip())
                if parsed_pr:
                    pr_target = (parsed_pr[0], parsed_pr[1], parsed_pr[3])
                    break

    if fetch_pr_flag and pr_target:
        pr_owner, pr_repo, pr_num = pr_target
        need_pr_fetch = (
            force
            or action in ["created", "updated"]
            or not issue_data.get("pull_request")
        )
        if need_pr_fetch:
            pr_code, pr_info, new_pr_etag = fetcher.fetch_pull_request(
                pr_owner, pr_repo, pr_num, etag=pr_etag
            )
            if pr_code == 200 and pr_info is not None:
                issue_data["pull_request"] = pr_info
                issue_data["_fetch_metadata"]["pr_etag"] = new_pr_etag
            elif pr_code == 304 and existing_data:
                issue_data["pull_request"] = existing_data.get("pull_request")

    # 4. Attach CSV Context & Status Analysis
    label_names = [l["name"] for l in issue_data.get("labels", []) if isinstance(l, dict) and l.get("name")]
    status_analysis = analyze_bug_status(
        csv_records=csv_records,
        github_state=issue_data.get("github_state"),
        github_state_reason=issue_data.get("github_state_reason"),
        labels=label_names,
        pr_details=issue_data.get("pull_request"),
    )

    issue_data["csv_records"] = csv_records
    issue_data["api"] = csv_records[0].get("api(s)", "") if csv_records else ""
    issue_data["status_analysis"] = status_analysis
    issue_data["_fetch_metadata"]["last_checked_at"] = datetime.now(timezone.utc).isoformat()

    # Save to disk
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = dest_path.with_suffix(".tmp")
    temp_path.write_text(json.dumps(issue_data, indent=2, ensure_ascii=False), encoding="utf-8")
    temp_path.replace(dest_path)

    return action, issue_data


def generate_summary(
    all_issues: List[Dict[str, Any]],
    output_dir: Path,
) -> Path:
    """Generate summary.json and README.md in output_dir."""
    output_dir.mkdir(parents=True, exist_ok=True)
    summary_path = output_dir / "summary.json"
    readme_path = output_dir / "README.md"

    now = datetime.now(timezone.utc).isoformat()
    by_status: Dict[str, int] = {}
    by_github_state: Dict[str, int] = {}
    by_tracker: Dict[str, int] = {"github": 0, "external": 0}
    discrepancies: List[Dict[str, Any]] = []

    compact_list = []
    for issue in all_issues:
        is_external = issue.get("tracker_type") == "external"
        analysis = issue.get("status_analysis", {})
        csv_status = analysis.get("csv_status", "Unknown")
        gh_state = issue.get("github_state", "unknown")

        by_status[csv_status] = by_status.get(csv_status, 0) + 1
        by_github_state[gh_state] = by_github_state.get(gh_state, 0) + 1
        if is_external:
            by_tracker["external"] += 1
        else:
            by_tracker["github"] += 1

        is_discrepancy = analysis.get("discrepancy_detected", False)
        item = {
            "tracker": "external" if is_external else "github",
            "issue_id": issue.get("issue_id") or issue.get("issue_number"),
            "repo_or_domain": issue.get("tracker_domain") or f"{issue.get('repo_owner')}/{issue.get('repo_name')}",
            "api": issue.get("api"),
            "csv_status": csv_status,
            "github_state": gh_state,
            "github_state_reason": issue.get("github_state_reason"),
            "labels": [l["name"] for l in issue.get("labels", []) if isinstance(l, dict)],
            "comments_count": issue.get("comments_count", 0),
            "has_merged_pr": (issue.get("pull_request") or {}).get("merged", False),
            "discrepancy_detected": is_discrepancy,
            "suggested_status": analysis.get("suggested_status"),
            "relative_json_path": issue.get("_relative_file_path"),
            "html_url": issue.get("html_url"),
        }
        compact_list.append(item)
        if is_discrepancy:
            discrepancies.append(item)

    summary_data = {
        "generated_at": now,
        "total_issues": len(all_issues),
        "by_tracker": by_tracker,
        "by_csv_status": by_status,
        "by_github_state": by_github_state,
        "discrepancies_count": len(discrepancies),
        "discrepancies": discrepancies,
        "issues": compact_list,
    }

    summary_path.write_text(json.dumps(summary_data, indent=2, ensure_ascii=False), encoding="utf-8")

    # Generate human & agent readable README.md
    readme_lines = [
        "# Cached Bug Details",
        "",
        "> **Note**: This entire directory is gitignored so that local scripts and LLM agents can inspect",
        "> issue details, comments, PR statuses, and maintainer decisions without making web calls.",
        "",
        f"- **Last Updated**: `{now}`",
        f"- **Total Issues**: {len(all_issues)} (GitHub: {by_tracker['github']}, External: {by_tracker['external']})",
        f"- **Issues with Status Discrepancies**: {len(discrepancies)}",
        "",
        "## Status Overview",
        "",
        "### CSV Status Breakdown",
        "| CSV Status | Count |",
        "| :--- | :--- |",
    ]
    for s, count in sorted(by_status.items(), key=lambda x: -x[1]):
        readme_lines.append(f"| {s} | {count} |")

    readme_lines.extend([
        "",
        "### GitHub State Breakdown",
        "| State | Count |",
        "| :--- | :--- |",
    ])
    for s, count in sorted(by_github_state.items(), key=lambda x: -x[1]):
        readme_lines.append(f"| {s} | {count} |")

    if discrepancies:
        readme_lines.extend([
            "",
            "## Flagged Discrepancies for LLM Review",
            "The following issues may require status updates in the CSVs:",
            "",
            "| Issue | API | Current CSV | GitHub State | Suggested | Reason / PR |",
            "| :--- | :--- | :--- | :--- | :--- | :--- |",
        ])
        for d in discrepancies:
            issue_str = f"[{d['repo_or_domain']}#{d['issue_id']}]({d['html_url']})"
            merged = "Merged PR" if d["has_merged_pr"] else (d["github_state_reason"] or d["github_state"])
            readme_lines.append(
                f"| {issue_str} | `{d['api']}` | **{d['csv_status']}** | {d['github_state']} | **{d['suggested_status']}** | {merged} |"
            )

    readme_lines.extend([
        "",
        "## Directory Structure",
        "- `summary.json`: Aggregated index of all issues with quick status flags.",
        "- `<application>/<issue_id>.json`: Full issue details including labels, body, maintainer comments, and PR data.",
    ])

    readme_path.write_text("\n".join(readme_lines) + "\n", encoding="utf-8")
    return summary_path


def main():
    parser = argparse.ArgumentParser(
        description="Fetch GitHub issue and PR details for bugs listed in bugs/*.csv"
    )
    parser.add_argument(
        "--token",
        type=str,
        default=None,
        help="GitHub Personal Access Token (defaults to $GITHUB_TOKEN env variable)",
    )
    parser.add_argument(
        "--bugs-dir",
        type=Path,
        default=DEFAULT_BUGS_DIR,
        help="Directory containing bug CSV files (default: bugs/)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Output directory to save issue data (default: bugs_data/)",
    )
    parser.add_argument(
        "--csv",
        type=str,
        default=None,
        help="Process only a specific CSV file name (e.g. pytorch.csv)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Limit number of issues to fetch per CSV (useful for testing)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force re-fetch all issues, bypassing ETag caching",
    )
    parser.add_argument(
        "--no-comments",
        action="store_true",
        help="Skip fetching issue comments",
    )
    parser.add_argument(
        "--no-pr",
        action="store_true",
        help="Skip fetching linked pull request details",
    )
    parser.add_argument(
        "--ensure-gitignore",
        action="store_true",
        default=True,
        help="Ensure output directory is in .gitignore (default: True)",
    )
    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="Suppress per-issue log messages",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output",
    )

    args = parser.parse_args()

    # 1. Ensure output directory is gitignored
    if args.ensure_gitignore:
        ignored = ensure_gitignored(args.output_dir)
        if ignored and not args.quiet:
            print(f"Ensured {args.output_dir.name}/ is listed in .gitignore")

    # 2. Check token and rate limits
    token = args.token or os.environ.get("GITHUB_TOKEN")
    if not token and not args.quiet:
        print(
            "[Warning] No GitHub token found ($GITHUB_TOKEN or --token). "
            "Unauthenticated requests are limited to 60 requests/hour.",
            file=sys.stderr,
        )

    fetcher = GitHubIssueFetcher(token=token, verbose=args.verbose)
    rate_info = fetcher.check_rate_limit()
    if rate_info and not args.quiet:
        print(
            f"GitHub API Rate Limit: {rate_info.get('remaining')}/{rate_info.get('limit')} remaining "
            f"(resets at {rate_info.get('reset_datetime')})"
        )

    # 3. Locate CSV files to process
    if not args.bugs_dir.exists():
        print(f"Error: Bugs directory '{args.bugs_dir}' does not exist.", file=sys.stderr)
        sys.exit(1)

    if args.csv:
        target_csvs = [args.bugs_dir / args.csv]
    else:
        # Scan all .csv files excluding raw multi-dataset tables
        target_csvs = sorted(
            [p for p in args.bugs_dir.glob("*.csv") if p.name not in RAW_DATASETS_TO_SKIP]
        )

    if not target_csvs:
        print(f"No CSV files found in {args.bugs_dir}", file=sys.stderr)
        sys.exit(0)

    # 4. Process each CSV file
    total_processed = 0
    stats = {"created": 0, "updated": 0, "unchanged": 0, "external": 0, "error": 0}
    all_collected_issues: List[Dict[str, Any]] = []

    for csv_file in target_csvs:
        if not csv_file.exists():
            print(f"Warning: {csv_file} does not exist, skipping.", file=sys.stderr)
            continue

        csv_name = csv_file.stem
        rows = read_bugs_csv(csv_file)
        if not args.quiet:
            print(f"\nProcessing {csv_file.name} ({len(rows)} entries)...")

        # Group rows by link
        issues_map: Dict[str, List[Dict[str, str]]] = {}
        for r in rows:
            link = r.get("link", "").strip()
            if not link:
                continue
            issues_map.setdefault(link, []).append(r)

        items = list(issues_map.items())
        if args.limit:
            items = items[: args.limit]

        csv_output_dir = args.output_dir / csv_name
        csv_output_dir.mkdir(parents=True, exist_ok=True)

        for idx, (link, records) in enumerate(items, 1):
            parsed = parse_github_url(link)
            api_name = records[0].get("api(s)", "")
            csv_st = records[0].get("Status", "")

            if parsed:
                owner, repo, item_type, number = parsed
                dest_file = csv_output_dir / f"{number}.json"
                action, issue_data = process_issue(
                    fetcher=fetcher,
                    owner=owner,
                    repo=repo,
                    number=number,
                    item_type=item_type,
                    csv_records=records,
                    dest_path=dest_file,
                    fetch_comments_flag=not args.no_comments,
                    fetch_pr_flag=not args.no_pr,
                    force=args.force,
                    verbose=args.verbose,
                )
                stats[action] = stats.get(action, 0) + 1
                total_processed += 1

                rel_file = dest_file.relative_to(REPO_ROOT).as_posix()
                issue_data["_relative_file_path"] = rel_file
                all_collected_issues.append(issue_data)

                if not args.quiet:
                    icon = {
                        "created": "✨ [Created]",
                        "updated": "🔄 [Updated]",
                        "unchanged": "💤 [Unchanged]",
                        "error": "❌ [Error]",
                    }.get(action, action)
                    gh_st = issue_data.get("github_state", "unknown")
                    type_label = "PR" if item_type == "pull" else "Issue"
                    print(
                        f"  [{idx}/{len(items)}] {icon} {owner}/{repo} {type_label}#{number} "
                        f"({api_name[:30]}) CSV:{csv_st} -> GH:{gh_st}"
                    )
            else:
                # External / non-GitHub issue tracker
                ext_info = parse_external_url(link)
                clean_id = ext_info["issue_id"]
                dest_file = csv_output_dir / f"{clean_id}.json"
                action, ext_data = process_external_issue(
                    url=link,
                    csv_records=records,
                    dest_path=dest_file,
                )
                stats["external"] = stats.get("external", 0) + 1
                total_processed += 1

                rel_file = dest_file.relative_to(REPO_ROOT).as_posix()
                ext_data["_relative_file_path"] = rel_file
                all_collected_issues.append(ext_data)

                if not args.quiet:
                    print(
                        f"  [{idx}/{len(items)}] 🌐 [External: {ext_info['domain']}] #{clean_id} "
                        f"({api_name[:30]}) CSV:{csv_st}"
                    )

    # 5. Generate summary files
    summary_path = generate_summary(all_collected_issues, args.output_dir)

    if not args.quiet:
        print("\n" + "=" * 50)
        print("Summary of Bug Fetch Run:")
        print(f"  Total Processed: {total_processed}")
        print(f"  Created:   {stats['created']}")
        print(f"  Updated:   {stats['updated']}")
        print(f"  Unchanged: {stats['unchanged']}")
        print(f"  External:  {stats['external']}")
        print(f"  Errors:    {stats['error']}")
        print(f"  Data Directory: {args.output_dir}")
        print(f"  Summary Index:  {summary_path}")
        print("=" * 50)


if __name__ == "__main__":
    main()
