#!/usr/bin/env python3
"""
Update Google Sheet directly using Google Sheets API v4.

Usage:
    # 1. With Google Service Account JSON:
    python3 scripts/update_google_sheet.py --credentials path/to/service_account.json

    # 2. With Google OAuth Bearer Token:
    python3 scripts/update_google_sheet.py --token "ya29...."

    # 3. Dry-run / status inspection:
    python3 scripts/update_google_sheet.py --dry-run
"""

import argparse
import csv
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
BUGS_DIR = REPO_ROOT / "bugs"
BUGS_DATA_DIR = REPO_ROOT / "bugs_data"
SPREADSHEET_ID = "1r03ajIybbPeLBqHdxbD54Qghwoy8NjL2weeh89vX7wM"

SHEET_CONFIGS = [
    {"name": "PyTorch", "file": "pytorch.csv"},
    {"name": "TensorFlow", "file": "tensorflow.csv"},
    {"name": "Jax", "file": "jax.csv"},
    {"name": "vLLM", "file": "vllm.csv"},
    {"name": "SGLang", "file": "sglang.csv"},
    {"name": "ArangoDB", "file": "arangodb.csv"},
    {"name": "cronie", "file": "cronie.csv"},
    {"name": "PostgreSQL", "file": "postgresql.csv"},
    {"name": "Clang_LLVM", "file": "clang_llvm.csv"},
    {"name": "GCC", "file": "gcc.csv"},
    {"name": "OpenSSH", "file": "openssh.csv"},
]

STATUS_NORMALIZE = {
    "confirmed": "Confirmed",
    "previously reported": "Confirmed",
    "fixed": "Fixed",
    "previously fixed": "Fixed",
    "pending": "Pending",
    "submitted": "Pending",
    "rejected": "Rejected",
}


def load_cached_titles() -> Dict[str, str]:
    titles = {}
    if not BUGS_DATA_DIR.exists():
        return titles
    for p in BUGS_DATA_DIR.glob("*/*.json"):
        try:
            with p.open(encoding="utf-8") as f:
                d = json.load(f)
                url = d.get("html_url")
                t = d.get("title")
                if url and t:
                    titles[url.strip().rstrip("/").lower()] = t.strip()
        except Exception:
            pass
    return titles


def build_sheet_table(csv_file: Path, cached_titles: Dict[str, str]) -> List[List[str]]:
    rows = []
    if not csv_file.exists():
        return rows

    with csv_file.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = None
        for r in reader:
            if not r or all(not c for c in r):
                continue
            lower_r = [c.strip().lower() for c in r]
            if any("link" in c for c in lower_r) and any("status" in c for c in lower_r):
                headers = lower_r
                break
        if headers is None:
            return rows

        parsed_rows = []
        for r in reader:
            if not r or all(not c for c in r):
                continue
            row_dict = {}
            for i, h in enumerate(headers):
                if i < len(r):
                    row_dict[h] = r[i].strip()
                else:
                    row_dict[h] = ""
            if row_dict.get("link"):
                parsed_rows.append(row_dict)

    total = len(parsed_rows)
    conf = sum(1 for r in parsed_rows if STATUS_NORMALIZE.get(r.get("status", "").strip().lower()) == "Confirmed")
    fix = sum(1 for r in parsed_rows if STATUS_NORMALIZE.get(r.get("status", "").strip().lower()) == "Fixed")
    rej = sum(1 for r in parsed_rows if STATUS_NORMALIZE.get(r.get("status", "").strip().lower()) == "Rejected")

    table = [
        ["Reported:", str(total), str(conf), str(fix), "", "", str(rej), "", "", ""],
        [""] * 10,
        ["api(s)", "link", "Status", "data_dependent", "comments", "bug_type", "pr", "pr_link", "note", "tool"],
    ]

    for r in parsed_rows:
        norm_status = STATUS_NORMALIZE.get(r.get("status", "").strip().lower(), r.get("status", ""))
        url = r.get("link", "").rstrip("/").lower()
        raw_note = r.get("note", "").strip()
        api = r.get("api(s)", "").strip()

        title = ""
        if url in cached_titles:
            title = cached_titles[url]
        elif raw_note and not re.match(r"^\d+$", raw_note) and raw_note not in ["Invalid input", "SIGABRT"]:
            title = raw_note
        elif api:
            title = f"Issue reported in {api}"
        else:
            title = "Reported issue"

        table.append([
            r.get("api(s)", ""),
            r.get("link", ""),
            norm_status,
            r.get("data_dependent", ""),
            "",
            r.get("bug_type", ""),
            r.get("pr", ""),
            r.get("pr_link", ""),
            title,
            r.get("tool", ""),
        ])

    return table


def get_token_from_service_account(creds_path: Path) -> str:
    """Exchange service account JSON for Google OAuth token."""
    import time
    try:
        import jwt  # PyJWT
    except ImportError:
        print("Please install pyjwt and cryptography: uv run --with pyjwt --with cryptography python3 scripts/update_google_sheet.py ...")
        sys.exit(1)

    with creds_path.open() as f:
        creds = json.load(f)

    now = int(time.time())
    payload = {
        "iss": creds["client_email"],
        "scope": "https://www.googleapis.com/auth/spreadsheets",
        "aud": creds["token_uri"],
        "exp": now + 3600,
        "iat": now,
    }

    signed_jwt = jwt.encode(payload, creds["private_key"], algorithm="RS256")
    data = urllib.parse.urlencode({
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": signed_jwt,
    }).encode("utf-8")

    req = urllib.request.Request(creds["token_uri"], data=data)
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read())
        return res["access_token"]


def api_request(url: str, token: str, method: str = "GET", data: dict = None) -> dict:
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8") if data else None,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method=method,
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def main():
    parser = argparse.ArgumentParser(description="Update Google Sheet with reported bugs.")
    parser.add_argument("--credentials", help="Path to Google service account JSON file.")
    parser.add_argument("--token", default=os.getenv("GOOGLE_ACCESS_TOKEN"), help="OAuth access token.")
    parser.add_argument("--dry-run", action="store_true", help="Inspect payload without updating.")
    args = parser.parse_args()

    cached_titles = load_cached_titles()

    all_sheets = {}
    for cfg in SHEET_CONFIGS:
        table = build_sheet_table(BUGS_DIR / cfg["file"], cached_titles)
        all_sheets[cfg["name"]] = table
        print(f"Prepared '{cfg['name']}': {len(table) - 3} bugs")

    if args.dry_run:
        print("\n[Dry Run] Prepared all 11 application sheets.")
        print(f"Target Sheet ID: {SPREADSHEET_ID}")
        print("To update live, run with --credentials <file.json> or --token <token>.")
        return

    token = args.token
    if not token and args.credentials:
        token = get_token_from_service_account(Path(args.credentials))

    if not token:
        print("\n[Notice] No Google API credentials provided.")
        print("To update your Google Sheet, choose one of these simple methods:\n")
        print("Method 1 (Fastest, 1-Click in Browser):")
        print("  1. Open your Google Sheet:")
        print(f"     https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit")
        print("  2. Click: Extensions > Apps Script")
        print("  3. Paste the contents of 'scripts/google_apps_script.js' into Code.gs and click 'Run'.")
        print("     All 11 application tabs will be populated automatically!\n")
        print("Method 2 (Import Excel File):")
        print("  1. In your Google Sheet, click File > Import > Upload.")
        print(f"  2. Select: {BUGS_DIR / 'Reported_Bugs_Complete.xlsx'}")
        print("  3. Choose 'Replace spreadsheet' or 'Insert new sheet(s)'.\n")
        print("Method 3 (API Automation):")
        print("  Run: python3 scripts/update_google_sheet.py --credentials <service_account.json>")
        sys.exit(0)

    # If token is available, update via REST API
    base_url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}"
    metadata = api_request(base_url, token)
    existing_sheets = {s["properties"]["title"]: s["properties"]["sheetId"] for s in metadata.get("sheets", [])}

    # Create missing sheets
    requests = []
    for sheet_name in all_sheets.keys():
        if sheet_name not in existing_sheets:
            requests.append({"addSheet": {"properties": {"title": sheet_name}}})

    if requests:
        api_request(f"{base_url}:batchUpdate", token, method="POST", data={"requests": requests})
        print(f"Created {len(requests)} new sheets.")

    # Update values in each sheet
    value_data = []
    for sheet_name, table in all_sheets.items():
        value_data.append({
            "range": f"'{sheet_name}'!A1:J{len(table)}",
            "values": table,
        })

    api_request(
        f"{base_url}/values:batchUpdate",
        token,
        method="POST",
        data={
            "valueInputOption": "USER_ENTERED",
            "data": value_data,
        },
    )
    print("Successfully updated all application sheets in the Google Sheet!")


if __name__ == "__main__":
    main()
