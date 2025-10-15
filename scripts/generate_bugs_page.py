#!/usr/bin/env python3
import csv
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parents[1]
CSV_DIR = REPO_ROOT / "bugs"
OUT_FILE = REPO_ROOT / "bugs.md"

# Map CSV Status -> icon (emoji)
STATUS_ICON = {
    "Fixed": "✅",
    "Previously Fixed": "✅",
    "Submitted": "🔄",
    "Confirmed": "🔵",
    "Rejected": "❌",
}

def read_issues(csv_path: Path):
    rows = []
    with csv_path.open(newline="", encoding="utf-8") as f:
        # Skip preamble lines until header row is found
        reader = csv.reader(f)
        headers = None
        buffered = []
        for r in reader:
            if not r or all(not c for c in r):
                continue
            buffered.append(r)
            if "api(s)" in r and "link" in r and "Status" in r:
                headers = r
                break
        if headers is None:
            return rows
        # Read the rest as DictReader using the detected headers
        dict_reader = csv.DictReader(f, fieldnames=headers)
        for row in dict_reader:
            if not row.get("link"):
                continue
            rows.append(row)
    return rows

def format_list_html(rows):
    items = []
    for row in rows:
        status = (row.get("Status") or "").strip()
        link = (row.get("link") or "").strip()
        icon = STATUS_ICON.get(status, "🔎")
        if not link:
            continue
        items.append(f"<li>{icon} <a href=\"{link}\" target=\"_blank\" rel=\"noopener\">{link}</a></li>")
    return "<ul class=\"bugs-list\">" + "".join(items) + "</ul>"

def summarize(rows_list):
    submitted = confirmed = fixed = 0
    for rows in rows_list:
        for r in rows:
            s = (r.get("Status") or "").strip()
            if s == "Submitted":
                submitted += 1
            elif s == "Confirmed":
                confirmed += 1
            elif s in ("Fixed", "Previously Fixed"):
                fixed += 1
    return submitted, confirmed, fixed

def main():
    pytorch_rows = read_issues(CSV_DIR / "pytorch.csv")
    tf_rows = read_issues(CSV_DIR / "tensorflow.csv")

    content = []
    # YAML front matter for Jekyll
    content.append("---")
    content.append("layout: page")
    content.append("title: Reported Bugs")
    content.append("permalink: /bugs/")
    # Add a machine-readable last-updated timestamp in the front matter
    now = datetime.now(timezone.utc)
    iso_ts = now.isoformat(timespec="seconds")
    content.append(f"last_updated: \"{iso_ts}\"")
    content.append("---\n")

    # Human-friendly 'Last updated' line displayed on the page
    content.append(f"_Last updated: {now.strftime('%Y-%m-%d %H:%M:%S UTC')}_")

    # Summary section
    sub, conf, fix = summarize([pytorch_rows, tf_rows])
    total = len(pytorch_rows) + len(tf_rows)
    # Single-line summary as requested
    content.append(
        f"## {STATUS_ICON['Confirmed']} {conf + fix} Confirmed ({STATUS_ICON['Fixed']} {fix} Fixed) + {STATUS_ICON['Submitted']} {sub} Pending + {STATUS_ICON['Rejected']} {total - (sub + conf + fix)} Rejected = **{total}**"
    )
    content.append("Detailed Spreadsheet: [Google Sheets](https://docs.google.com/spreadsheets/d/1r03ajIybbPeLBqHdxbD54Qghwoy8NjL2weeh89vX7wM/edit?usp=sharing)")
    content.append("\n<hr class=\"bugs-divider\" />\n")
    # Two-column grid for PyTorch and TensorFlow
    content.append("<div class=\"bugs-grid\">")
    content.append("  <section class=\"bugs-col\">")
    content.append("  <h2>PyTorch</h2>")
    content.append(format_list_html(pytorch_rows) or "<em>No entries found.</em>")
    content.append("  </section>")
    content.append("  <section class=\"bugs-col\">")
    content.append("  <h2>TensorFlow</h2>")
    content.append(format_list_html(tf_rows) or "<em>No entries found.</em>")
    content.append("  </section>")
    content.append("</div>")

    OUT_FILE.write_text("\n".join(content), encoding="utf-8")
    print(f"Wrote {OUT_FILE}")

if __name__ == "__main__":
    main()
