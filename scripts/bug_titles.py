#!/usr/bin/env python3
"""
Issue titles shared by the bug scripts.

The titles shown on the bugs page come from the upstream trackers.
fetch_issue_details.py downloads them into bugs_data/, which is gitignored and
therefore missing on a fresh clone. bugs/titles.json is the committed copy: the
scripts read it first and then overlay whatever bugs_data/ holds, so the page
and the spreadsheet come out the same with or without the download.
"""

import json
from pathlib import Path
from typing import Dict

REPO_ROOT = Path(__file__).resolve().parents[1]
BUGS_DATA_DIR = REPO_ROOT / "bugs_data"
TITLES_FILE = REPO_ROOT / "bugs" / "titles.json"


def normalize_url(url: str) -> str:
    return url.strip().rstrip("/").lower()


def read_fetched_titles() -> Dict[str, str]:
    """Titles from the bugs_data/ download, if it exists."""
    titles: Dict[str, str] = {}
    if not BUGS_DATA_DIR.exists():
        return titles
    for path in BUGS_DATA_DIR.glob("*/*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if not isinstance(data, dict):
            continue
        url, title = data.get("html_url"), data.get("title")
        if url and title:
            titles[normalize_url(url)] = title.strip()
    return titles


def load_titles() -> Dict[str, str]:
    """Return {normalized issue URL: title} and keep bugs/titles.json current."""
    stored: Dict[str, str] = {}
    if TITLES_FILE.exists():
        stored = json.loads(TITLES_FILE.read_text(encoding="utf-8"))

    merged = {**stored, **read_fetched_titles()}
    if merged != stored:
        TITLES_FILE.write_text(
            json.dumps(merged, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"Updated {TITLES_FILE.relative_to(REPO_ROOT)}: {len(merged)} titles ({len(merged) - len(stored)} new).")
    return merged
