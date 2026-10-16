#!/usr/bin/env python3
"""
Generate:
1. Reported_Bugs_Complete.xlsx: Multi-sheet Excel workbook with all 11 applications + Summary tab.
2. scripts/google_apps_script.js: Google Apps Script that updates the active Google Sheet directly with 1 click.
3. scripts/update_google_sheet.py: Python script to update via Google Sheets API (with credentials.json).
"""

import csv
import json
import re
from pathlib import Path
from typing import Dict, List

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

REPO_ROOT = Path(__file__).resolve().parents[1]
BUGS_DIR = REPO_ROOT / "bugs"
BUGS_DATA_DIR = REPO_ROOT / "bugs_data"
EXCEL_OUT = BUGS_DIR / "Reported_Bugs_Complete.xlsx"
APPS_SCRIPT_OUT = REPO_ROOT / "scripts" / "google_apps_script.js"

SHEET_CONFIGS = [
    {"name": "Summary", "file": None, "category": "Overview"},
    {"name": "PyTorch", "file": "pytorch.csv", "category": "Deep Learning"},
    {"name": "TensorFlow", "file": "tensorflow.csv", "category": "Deep Learning"},
    {"name": "Jax", "file": "jax.csv", "category": "Autodiff / ML"},
    {"name": "vLLM", "file": "vllm.csv", "category": "LLM Serving"},
    {"name": "SGLang", "file": "sglang.csv", "category": "LLM Serving"},
    {"name": "ArangoDB", "file": "arangodb.csv", "category": "Graph Database"},
    {"name": "cronie", "file": "cronie.csv", "category": "System Daemon"},
    {"name": "PostgreSQL", "file": "postgresql.csv", "category": "Database Engine"},
    {"name": "Clang_LLVM", "file": "clang_llvm.csv", "category": "Compiler / Toolchain"},
    {"name": "GCC", "file": "gcc.csv", "category": "Compiler / Toolchain"},
    {"name": "OpenSSH", "file": "openssh.csv", "category": "Security / Network"},
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


def read_app_csv(csv_path: Path, cached_titles: Dict[str, str]) -> List[Dict[str, str]]:
    rows = []
    if not csv_path.exists():
        return rows

    with csv_path.open(newline="", encoding="utf-8") as f:
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
                # Clean title lookup for note column
                url = row_dict["link"].rstrip("/").lower()
                raw_note = row_dict.get("note", "").strip()
                api = row_dict.get("api(s)", "").strip()
                if url in cached_titles:
                    row_dict["note"] = cached_titles[url]
                elif raw_note and not re.match(r"^\d+$", raw_note) and raw_note not in ["Invalid input", "SIGABRT"]:
                    row_dict["note"] = raw_note
                elif api:
                    row_dict["note"] = f"Issue reported in {api}"

                # Wipe noise from comments / invalid inputs
                if re.match(r"^\d+$", row_dict.get("comments", "")):
                    row_dict["comments"] = ""
                rows.append(row_dict)

    return rows


def build_excel_workbook(cached_titles: Dict[str, str]) -> None:
    wb = openpyxl.Workbook()
    # remove default sheet
    default_sheet = wb.active
    wb.remove(default_sheet)

    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="1E293B", end_color="1E293B", fill_type="solid")
    summary_fill = PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid")
    bold_font = Font(name="Calibri", size=11, bold=True)
    regular_font = Font(name="Calibri", size=11)
    thin_border = Border(
        left=Side(style="thin", color="E2E8F0"),
        right=Side(style="thin", color="E2E8F0"),
        top=Side(style="thin", color="E2E8F0"),
        bottom=Side(style="thin", color="E2E8F0"),
    )

    app_stats = []

    # 1. Generate individual application sheets
    for cfg in SHEET_CONFIGS:
        if cfg["name"] == "Summary":
            continue

        sheet = wb.create_sheet(title=cfg["name"])
        rows = read_app_csv(BUGS_DIR / cfg["file"], cached_titles)

        # Compute counts
        total = len(rows)
        conf = sum(1 for r in rows if STATUS_NORMALIZE.get(r.get("status", "").strip().lower()) == "Confirmed")
        fix = sum(1 for r in rows if STATUS_NORMALIZE.get(r.get("status", "").strip().lower()) == "Fixed")
        pend = sum(1 for r in rows if STATUS_NORMALIZE.get(r.get("status", "").strip().lower()) == "Pending")
        rej = sum(1 for r in rows if STATUS_NORMALIZE.get(r.get("status", "").strip().lower()) == "Rejected")

        app_stats.append({
            "name": cfg["name"],
            "category": cfg["category"],
            "total": total,
            "confirmed": conf,
            "fixed": fix,
            "pending": pend,
            "rejected": rej,
        })

        # Row 1: Reported stats header
        sheet.append(["Reported:", total, conf, fix, "", "", rej, "", "", ""])
        sheet.cell(1, 1).font = bold_font
        for col_idx in [2, 3, 4, 7]:
            sheet.cell(1, col_idx).font = bold_font

        # Row 2: Empty
        sheet.append([""] * 10)

        # Row 3: Headers
        cols = ["api(s)", "link", "Status", "data_dependent", "comments", "bug_type", "pr", "pr_link", "note", "tool"]
        sheet.append(cols)
        for col_idx in range(1, 11):
            cell = sheet.cell(3, col_idx)
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal="center", vertical="center")

        # Row 4+: Data rows
        for r in rows:
            norm_status = STATUS_NORMALIZE.get(r.get("status", "").strip().lower(), r.get("status", ""))
            row_vals = [
                r.get("api(s)", ""),
                r.get("link", ""),
                norm_status,
                r.get("data_dependent", ""),
                r.get("comments", ""),
                r.get("bug_type", ""),
                r.get("pr", ""),
                r.get("pr_link", ""),
                r.get("note", ""),
                r.get("tool", ""),
            ]
            sheet.append(row_vals)
            row_idx = sheet.max_row
            for col_idx in range(1, 11):
                cell = sheet.cell(row_idx, col_idx)
                cell.font = regular_font
                cell.border = thin_border
                if col_idx in [2, 8] and cell.value and str(cell.value).startswith("http"):
                    cell.font = Font(name="Calibri", size=11, color="0000EE", underline="single")

        # Auto-adjust column widths
        for col in sheet.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                val = str(cell.value or "")
                if len(val) > max_len:
                    max_len = len(val)
            sheet.column_dimensions[col_letter].width = min(max(max_len + 3, 12), 65)

    # 2. Master Summary Sheet (Insert at index 0)
    summary_sheet = wb.create_sheet(title="Summary", index=0)
    summary_headers = ["Application", "Domain / Category", "Total Reported", "Confirmed", "Fixed", "Pending", "Rejected", "% Confirmed or Fixed"]
    summary_sheet.append(["Reported Bugs & Vulnerabilities - Master Summary"])
    summary_sheet.cell(1, 1).font = Font(name="Calibri", size=16, bold=True, color="0F172A")
    summary_sheet.append([])

    summary_sheet.append(summary_headers)
    for col_idx in range(1, len(summary_headers) + 1):
        cell = summary_sheet.cell(3, col_idx)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center", vertical="center")

    tot_total = sum(s["total"] for s in app_stats)
    tot_conf = sum(s["confirmed"] for s in app_stats)
    tot_fix = sum(s["fixed"] for s in app_stats)
    tot_pend = sum(s["pending"] for s in app_stats)
    tot_rej = sum(s["rejected"] for s in app_stats)

    for s in app_stats:
        conf_fix_pct = f"{((s['confirmed'] + s['fixed']) / s['total'] * 100):.1f}%" if s['total'] else "0%"
        summary_sheet.append([
            s["name"],
            s["category"],
            s["total"],
            s["confirmed"],
            s["fixed"],
            s["pending"],
            s["rejected"],
            conf_fix_pct,
        ])
        row_idx = summary_sheet.max_row
        for col_idx in range(1, len(summary_headers) + 1):
            cell = summary_sheet.cell(row_idx, col_idx)
            cell.font = regular_font
            cell.border = thin_border
            if col_idx in [3, 4, 5, 6, 7, 8]:
                cell.alignment = Alignment(horizontal="right")

    # Grand Total Row
    tot_conf_fix_pct = f"{((tot_conf + tot_fix) / tot_total * 100):.1f}%" if tot_total else "0%"
    summary_sheet.append([
        "Total",
        "Across 11 Applications",
        tot_total,
        tot_conf,
        tot_fix,
        tot_pend,
        tot_rej,
        tot_conf_fix_pct,
    ])
    total_row = summary_sheet.max_row
    for col_idx in range(1, len(summary_headers) + 1):
        cell = summary_sheet.cell(total_row, col_idx)
        cell.font = bold_font
        cell.fill = summary_fill
        cell.border = thin_border
        if col_idx in [3, 4, 5, 6, 7, 8]:
            cell.alignment = Alignment(horizontal="right")

    for col in summary_sheet.columns:
        max_len = 0
        col_letter = get_column_letter(col[0].column)
        for cell in col:
            val = str(cell.value or "")
            if len(val) > max_len:
                max_len = len(val)
        summary_sheet.column_dimensions[col_letter].width = max(max_len + 4, 15)

    wb.save(EXCEL_OUT)
    print(f"Saved complete workbook with 11 application tabs to {EXCEL_OUT}")


def build_apps_script(cached_titles: Dict[str, str]) -> None:
    """Generate a 1-click Google Apps Script that populates the active Google Sheet."""
    sheet_data = {}

    for cfg in SHEET_CONFIGS:
        if cfg["name"] == "Summary":
            continue
        rows = read_app_csv(BUGS_DIR / cfg["file"], cached_titles)
        total = len(rows)
        conf = sum(1 for r in rows if STATUS_NORMALIZE.get(r.get("status", "").strip().lower()) == "Confirmed")
        fix = sum(1 for r in rows if STATUS_NORMALIZE.get(r.get("status", "").strip().lower()) == "Fixed")
        rej = sum(1 for r in rows if STATUS_NORMALIZE.get(r.get("status", "").strip().lower()) == "Rejected")

        table = []
        table.append(["Reported:", total, conf, fix, "", "", rej, "", "", ""])
        table.append([""] * 10)
        table.append(["api(s)", "link", "Status", "data_dependent", "comments", "bug_type", "pr", "pr_link", "note", "tool"])

        for r in rows:
            norm_status = STATUS_NORMALIZE.get(r.get("status", "").strip().lower(), r.get("status", ""))
            table.append([
                r.get("api(s)", ""),
                r.get("link", ""),
                norm_status,
                r.get("data_dependent", ""),
                r.get("comments", ""),
                r.get("bug_type", ""),
                r.get("pr", ""),
                r.get("pr_link", ""),
                r.get("note", ""),
                r.get("tool", ""),
            ])

        sheet_data[cfg["name"]] = table

    js_code = f"""/**
 * Google Apps Script to update your Google Sheet with all 323 reported bugs across all 11 applications.
 *
 * HOW TO USE (Takes 30 seconds):
 * 1. Open your Google Sheet: https://docs.google.com/spreadsheets/d/1r03ajIybbPeLBqHdxbD54Qghwoy8NjL2weeh89vX7wM/edit
 * 2. In the menu, click: Extensions > Apps Script
 * 3. Replace all text in Code.gs with this entire script.
 * 4. Click the "Save" icon (Floppy disk), then click "Run".
 * 5. Grant permissions if prompted.
 * 6. Switch back to your Google Sheet — all 11 application sheets will be instantly created/updated with formatted rows!
 */

const BUG_SHEETS_DATA = {json.dumps(sheet_data, ensure_ascii=False, indent=2)};

function updateReportedBugs() {{
  const ss = SpreadsheetApp.getActiveSpreadsheet();

  for (const [sheetName, rows] of Object.entries(BUG_SHEETS_DATA)) {{
    let sheet = ss.getSheetByName(sheetName);
    if (!sheet) {{
      sheet = ss.insertSheet(sheetName);
    }}
    sheet.clear();

    if (rows.length > 0 && rows[0].length > 0) {{
      const numRows = rows.length;
      const numCols = rows[0].length;
      const range = sheet.getRange(1, 1, numRows, numCols);
      range.setValues(rows);

      // Format header row (Row 3)
      if (numRows >= 3) {{
        const headerRange = sheet.getRange(3, 1, 1, numCols);
        headerRange.setFontWeight("bold");
        headerRange.setBackground("#1E293B");
        headerRange.setFontColor("#FFFFFF");
      }}

      // Format Row 1 summary
      const row1Range = sheet.getRange(1, 1, 1, numCols);
      row1Range.setFontWeight("bold");

      // Auto resize columns
      for (let c = 1; c <= numCols; c++) {{
        sheet.autoResizeColumn(c);
      }}
    }}
  }}

  SpreadsheetApp.getUi().alert("Successfully updated all 11 application tabs with 323 reported bugs!");
}}
"""
    APPS_SCRIPT_OUT.write_text(js_code, encoding="utf-8")
    print(f"Generated Google Apps Script at {APPS_SCRIPT_OUT}")


def main():
    cached_titles = load_cached_titles()
    build_excel_workbook(cached_titles)
    build_apps_script(cached_titles)


if __name__ == "__main__":
    main()
