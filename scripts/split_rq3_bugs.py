#!/usr/bin/env python3
"""
Split bugs/rq3_bugs_reported.csv into individual application CSV files,
following the format of pytorch.csv and tensorflow.csv:
    Reported:,<total>,<confirmed>,<fixed>,,,<rejected>,,,
    ,,,,,,,,,
    api(s),link,Status,data_dependent,comments,bug_type,pr,pr_link,note,tool

Applications:
- ArangoDB   -> bugs/arangodb.csv
- Clang/LLVM -> bugs/clang_llvm.csv
- GCC        -> bugs/gcc.csv
- Jax        -> bugs/jax.csv
- OpenSSH    -> bugs/openssh.csv
- PostgreSQL -> bugs/postgresql.csv
- PyTorch    -> appended to bugs/pytorch.csv
- SGLang     -> bugs/sglang.csv
- cronie     -> bugs/cronie.csv
- vLLM       -> bugs/vllm.csv
"""

import csv
import re
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
BUGS_DIR = REPO_ROOT / "bugs"
RQ3_CSV_PATH = BUGS_DIR / "rq3_bugs_reported.csv"

URL_RE = re.compile(r"https?://[^\s,\);\"]+")
GH_PR_RE = re.compile(r"https?://github\.com/[^/]+/[^/]+/pull/\d+")

APP_FILENAME_MAP = {
    "ArangoDB": "arangodb.csv",
    "Clang/LLVM": "clang_llvm.csv",
    "GCC": "gcc.csv",
    "Jax": "jax.csv",
    "OpenSSH": "openssh.csv",
    "PostgreSQL": "postgresql.csv",
    "PyTorch": "pytorch.csv",
    "SGLang": "sglang.csv",
    "cronie": "cronie.csv",
    "vLLM": "vllm.csv",
}

STATUS_MAP = {
    "confirmed": "Confirmed",
    "pending": "Pending",
    "rejected": "Rejected",
}


def extract_rows_from_rq3(app_rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Convert rq3_bugs_reported rows for an application to target CSV row format."""
    out_rows = []
    for r in app_rows:
        api = (r.get("Found_by") or r.get("Bug") or r.get("Title") or "").strip()
        status_raw = r.get("Status", "").strip().lower()
        status = STATUS_MAP.get(status_raw, status_raw.capitalize() if status_raw else "Pending")
        bug_type = r.get("Bug_type", "").strip().capitalize()
        note = r.get("Title", "").strip()
        tool = r.get("Model", "").strip()
        fixed = r.get("Fixed", "").strip()

        report = r.get("Report", "").strip()
        upstream = r.get("Upstream", "").strip()

        report_urls = URL_RE.findall(report)
        upstream_urls = URL_RE.findall(upstream)
        main_urls = report_urls if report_urls else upstream_urls

        pr_matches = GH_PR_RE.findall(upstream + " " + report)
        pr_link = pr_matches[0] if pr_matches else ""

        pr_val = ""
        if fixed.lower() == "yes":
            pr_val = "Yes"
        elif pr_link:
            pr_val = "Open"

        for u in main_urls:
            this_pr_link = u if "/pull/" in u else pr_link
            this_pr_val = "Open" if ("/pull/" in u and not pr_val) else pr_val
            out_rows.append({
                "api(s)": api,
                "link": u,
                "Status": status,
                "data_dependent": "",
                "comments": "",
                "bug_type": bug_type,
                "pr": this_pr_val,
                "pr_link": this_pr_link if this_pr_link != u else "",
                "note": note,
                "tool": tool,
            })
    return out_rows


def format_csv_content(rows: List[Dict[str, str]]) -> str:
    """Format rows into standard CSV with 2 header preamble lines and column headers."""
    total = len(rows)
    confirmed = sum(1 for r in rows if r.get("Status") in ["Confirmed", "Fixed", "Previously Fixed", "Previously Reported"])
    fixed = sum(1 for r in rows if r.get("Status") in ["Fixed", "Previously Fixed"] or r.get("pr") == "Yes")
    rejected = sum(1 for r in rows if r.get("Status") == "Rejected")

    lines = [
        f"Reported:,{total},{confirmed},{fixed},,,{rejected},,,",
        ",,,,,,,,,",
        "api(s),link,Status,data_dependent,comments,bug_type,pr,pr_link,note,tool",
    ]

    import io
    output = io.StringIO()
    writer = csv.DictWriter(
        output,
        fieldnames=["api(s)", "link", "Status", "data_dependent", "comments", "bug_type", "pr", "pr_link", "note", "tool"],
        lineterminator="\n",
    )
    for r in rows:
        writer.writerow(r)

    return "\n".join(lines) + "\n" + output.getvalue()


def update_pytorch_csv(new_rows: List[Dict[str, str]]) -> int:
    """Append new PyTorch rows to existing bugs/pytorch.csv and update line 1 summary."""
    pytorch_path = BUGS_DIR / "pytorch.csv"
    existing_content = pytorch_path.read_text(encoding="utf-8")
    lines = existing_content.splitlines()

    # Identify existing links to prevent any duplicate appending
    existing_links = set()
    for l in lines[3:]:
        # Parse link roughly or via csv reader
        parts = list(csv.reader([l]))
        if parts and len(parts[0]) > 1:
            existing_links.add(parts[0][1].strip())

    added_count = 0
    import io
    output = io.StringIO()
    writer = csv.DictWriter(
        output,
        fieldnames=["api(s)", "link", "Status", "data_dependent", "comments", "bug_type", "pr", "pr_link", "note", "tool"],
        lineterminator="\n",
    )
    for r in new_rows:
        if r["link"] not in existing_links:
            writer.writerow(r)
            existing_links.add(r["link"])
            added_count += 1

    appended_csv = output.getvalue()

    # Calculate updated totals
    all_data_lines = [l for l in lines[3:] if l.strip()] + [l for l in appended_csv.splitlines() if l.strip()]
    total = len(all_data_lines)

    # Count confirmed, fixed, rejected across all
    all_rows = []
    for l in all_data_lines:
        parsed = list(csv.reader([l]))
        if parsed and len(parsed[0]) >= 3:
            all_rows.append(parsed[0])

    confirmed = sum(1 for r in all_rows if len(r) > 2 and r[2] in ["Confirmed", "Fixed", "Previously Fixed", "Previously Reported"])
    fixed = sum(1 for r in all_rows if len(r) > 2 and r[2] in ["Fixed", "Previously Fixed"])
    rejected = sum(1 for r in all_rows if len(r) > 2 and r[2] == "Rejected")

    # Update line 0
    new_header_0 = f"Reported:,{total},{confirmed},{fixed},,,{rejected},,,"
    lines[0] = new_header_0

    new_full_content = "\n".join(lines)
    if not new_full_content.endswith("\n"):
        new_full_content += "\n"
    new_full_content += appended_csv

    pytorch_path.write_text(new_full_content, encoding="utf-8")
    return added_count


def main():
    if not RQ3_CSV_PATH.exists():
        print(f"Error: {RQ3_CSV_PATH} not found.")
        return

    with RQ3_CSV_PATH.open(encoding="utf-8") as f:
        rq3_rows = list(csv.DictReader(f))

    print(f"Loaded {len(rq3_rows)} rows from {RQ3_CSV_PATH.name}")

    apps = {}
    for r in rq3_rows:
        apps.setdefault(r["Application"], []).append(r)

    created_files = []
    for app_name, target_filename in APP_FILENAME_MAP.items():
        app_rows = apps.get(app_name, [])
        if not app_rows:
            print(f"Warning: No rows found for application '{app_name}'")
            continue

        extracted = extract_rows_from_rq3(app_rows)

        if app_name == "PyTorch":
            added = update_pytorch_csv(extracted)
            print(f"Appended {added} rows to bugs/pytorch.csv (total {len(extracted)} extracted)")
            created_files.append("pytorch.csv (appended)")
        else:
            target_path = BUGS_DIR / target_filename
            content = format_csv_content(extracted)
            target_path.write_text(content, encoding="utf-8")
            print(f"Wrote {len(extracted)} rows to bugs/{target_filename}")
            created_files.append(target_filename)

    print(f"\nSuccessfully divided rq3_bugs_reported.csv across {len(created_files)} files.")


if __name__ == "__main__":
    main()
