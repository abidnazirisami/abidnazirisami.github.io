#!/usr/bin/env python3
"""
Generate a clean, visually structured Reported Bugs dashboard for bugs.md.
Features:
- Headline KPI metrics (Total, Confirmed, Fixed, Pending, Rejected)
- Proportional stacked bar charts and resolution donut chart
- Application brand SVG logos (no emojis)
- Uniform bug cards containing official issue titles
- Real-time search and status filtering
- Preserves spreadsheet link and timestamps
"""

import csv
import html
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
BUGS_DIR = REPO_ROOT / "bugs"
BUGS_DATA_DIR = REPO_ROOT / "bugs_data"
OUT_FILE = REPO_ROOT / "bugs.md"

SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1r03ajIybbPeLBqHdxbD54Qghwoy8NjL2weeh89vX7wM/edit?usp=sharing"

# Clean inline SVG logos for each application
APP_LOGOS = {
    "pytorch": (
        '<svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="PyTorch">'
        '<path d="M12.5 2.5C12.5 2.5 7.5 7.5 7.5 13.5C7.5 16.8 9.7 19.5 12.5 19.5C15.3 19.5 17.5 16.8 17.5 13.5C17.5 7.5 12.5 2.5 12.5 2.5Z" fill="#EE4C2C"/>'
        '<circle cx="16.5" cy="7.5" r="1.8" fill="#EE4C2C"/>'
        '</svg>'
    ),
    "tensorflow": (
        '<svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="TensorFlow">'
        '<path d="M12 2L3 7.2V17.5L7.5 15V9.8L12 7.2L16.5 9.8V15L21 17.5V7.2L12 2Z" fill="#FF6F00"/>'
        '<path d="M10 10.5V22L14 22V10.5L12 9.3L10 10.5Z" fill="#FFA000"/>'
        '</svg>'
    ),
    "jax": (
        '<svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="JAX">'
        '<rect x="2" y="4" width="20" height="16" rx="4" fill="#E8F0FE"/>'
        '<text x="12" y="15.5" font-family="system-ui, -apple-system, sans-serif" font-size="9" font-weight="800" fill="#1A73E8" text-anchor="middle" letter-spacing="-0.02em">JAX</text>'
        '</svg>'
    ),
    "vllm": (
        '<svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="vLLM">'
        '<path d="M4 4L12 20L20 4H15.5L12 13L8.5 4H4Z" fill="#2563EB"/>'
        '<circle cx="12" cy="7" r="2.2" fill="#60A5FA"/>'
        '</svg>'
    ),
    "sglang": (
        '<svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="SGLang">'
        '<rect x="2" y="4" width="20" height="16" rx="4" fill="#F3E8FF"/>'
        '<text x="12" y="15.5" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" font-weight="800" fill="#7C3AED" text-anchor="middle" letter-spacing="-0.02em">SGL</text>'
        '</svg>'
    ),
    "arangodb": (
        '<svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="ArangoDB">'
        '<path d="M12 2C8 2 4 8 4 14C4 18.5 7.5 22 12 22C16.5 22 20 18.5 20 14C20 8 16 2 12 2Z" fill="#2B8236"/>'
        '<circle cx="12" cy="15" r="4.2" fill="#84CC16"/>'
        '<circle cx="12" cy="15" r="2.5" fill="#65A30D"/>'
        '</svg>'
    ),
    "cronie": (
        '<svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="cronie">'
        '<circle cx="12" cy="12" r="9" stroke="#475569" stroke-width="2" fill="none"/>'
        '<polyline points="12,7 12,12 15,14" stroke="#475569" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
        '</svg>'
    ),
    "postgresql": (
        '<svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="PostgreSQL">'
        '<path d="M12 3C8 3 4 5 4 10C4 13.5 5.5 17 8 19V22H11V18H13V22H16V19C18.5 17 20 13.5 20 10C20 5 16 3 12 3Z" fill="#336791"/>'
        '<circle cx="9.5" cy="9.5" r="1.5" fill="#FFFFFF"/>'
        '<circle cx="14.5" cy="9.5" r="1.5" fill="#FFFFFF"/>'
        '<path d="M11 12H13V15H11V12Z" fill="#E2E8F0"/>'
        '</svg>'
    ),
    "clang_llvm": (
        '<svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Clang / LLVM">'
        '<path d="M4 18C4 18 7 19 10 16C13 13 13 8 13 8C13 8 15 11 17 12C19 13 21 12 21 12C21 12 19 15 16 17C13 19 8 20 4 18Z" fill="#D9381E"/>'
        '<path d="M13 8C11 5 7 4 7 4C7 4 8 7 10 9C11 10 13 8 13 8Z" fill="#EA580C"/>'
        '</svg>'
    ),
    "gcc": (
        '<svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="GCC">'
        '<rect x="2" y="4" width="20" height="16" rx="4" fill="#FEE2E2"/>'
        '<text x="12" y="15.5" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" font-weight="800" fill="#991B1B" text-anchor="middle" letter-spacing="-0.02em">GCC</text>'
        '</svg>'
    ),
    "openssh": (
        '<svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="OpenSSH">'
        '<path d="M12 2L4 6V12C4 17 7.5 21 12 22C16.5 21 20 17 20 12V6L12 2Z" fill="#0F766E"/>'
        '<circle cx="12" cy="10" r="2.5" fill="#CCFBF1"/>'
        '<path d="M11 12.5H13V16H11V12.5Z" fill="#CCFBF1"/>'
        '</svg>'
    ),
}

APP_CONFIGS = [
    {"name": "PyTorch", "slug": "pytorch", "file": "pytorch.csv", "category": "Deep Learning"},
    {"name": "TensorFlow", "slug": "tensorflow", "file": "tensorflow.csv", "category": "Deep Learning"},
    {"name": "JAX", "slug": "jax", "file": "jax.csv", "category": "Autodiff / ML"},
    {"name": "vLLM", "slug": "vllm", "file": "vllm.csv", "category": "LLM Serving"},
    {"name": "SGLang", "slug": "sglang", "file": "sglang.csv", "category": "LLM Serving"},
    {"name": "ArangoDB", "slug": "arangodb", "file": "arangodb.csv", "category": "Graph Database"},
    {"name": "cronie", "slug": "cronie", "file": "cronie.csv", "category": "System Daemon"},
    {"name": "PostgreSQL", "slug": "postgresql", "file": "postgresql.csv", "category": "Database Engine"},
    {"name": "Clang / LLVM", "slug": "clang_llvm", "file": "clang_llvm.csv", "category": "Compiler / Toolchain"},
    {"name": "GCC", "slug": "gcc", "file": "gcc.csv", "category": "Compiler / Toolchain"},
    {"name": "OpenSSH", "slug": "openssh", "file": "openssh.csv", "category": "Security / Network"},
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
    """Load cached issue titles from bugs_data/."""
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
                    norm = url.strip().rstrip("/").lower()
                    titles[norm] = t.strip()
        except Exception:
            pass
    return titles


def read_issues(csv_path: Path) -> List[Dict[str, str]]:
    """Read issues from CSV with robust header detection."""
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
                rows.append(row_dict)

    return rows


def categorize_status(raw_status: str) -> str:
    s = (raw_status or "").strip().lower()
    return STATUS_NORMALIZE.get(s, "Pending")


def extract_rejection_flag(raw_note: str) -> str:
    """Extract clean rejection flag if applicable."""
    raw = (raw_note or "").strip().lower()
    if "duplicate" in raw:
        return "Duplicate"
    if "not a bug" in raw or "intended" in raw or "expected" in raw:
        return "Not a bug"
    if "feature" in raw or "enhancement" in raw:
        return "Feature request"
    if "out of scope" in raw or "wontfix" in raw:
        return "Won't fix"
    return ""


def format_link_label(url: str) -> str:
    url = url.strip()
    m = re.search(r"github\.com/[^/]+/[^/]+/issues/(\d+)", url)
    if m:
        return f"Issue #{m.group(1)} ↗"
    m = re.search(r"github\.com/[^/]+/[^/]+/pull/(\d+)", url)
    if m:
        return f"PR #{m.group(1)} ↗"
    m = re.search(r"gcc\.gnu\.org/bugzilla/show_bug\.cgi\?id=(\d+)", url)
    if m:
        return f"GCC #{m.group(1)} ↗"
    m = re.search(r"bugzilla\.mindrot\.org/show_bug\.cgi\?id=(\d+)", url)
    if m:
        return f"Bugzilla #{m.group(1)} ↗"
    if "postgresql.org/message-id" in url:
        return "pg-hackers ↗"
    return "Tracker ↗"


def format_pr_label(url: str) -> str:
    url = url.strip()
    m = re.search(r"github\.com/[^/]+/[^/]+/pull/(\d+)", url)
    if m:
        return f"PR #{m.group(1)} ↗"
    return "PR ↗"


def build_kpi_cards_html(total: int, conf: int, fix: int, pend: int, rej: int) -> str:
    conf_pct = f"{(conf / total * 100):.1f}%" if total else "0%"
    fix_pct = f"{(fix / total * 100):.1f}%" if total else "0%"
    pend_pct = f"{(pend / total * 100):.1f}%" if total else "0%"
    rej_pct = f"{(rej / total * 100):.1f}%" if total else "0%"
    conf_and_fixed_pct = f"{((conf + fix) / total * 100):.1f}%" if total else "0%"

    html_parts = [
        '<div class="bugs-kpi-grid">',
        # Card 1: Total Reported
        '  <div class="bugs-kpi-card kpi-total-card">',
        '    <div class="kpi-header">',
        '      <span class="kpi-label">Total Reported</span>',
        '    </div>',
        f'    <div class="kpi-number">{total}</div>',
        '    <div class="kpi-total-sub">',
        '      <span class="kpi-total-item"><strong>11</strong> applications</span>',
        '      <span class="kpi-total-divider"></span>',
        f'      <span class="kpi-total-item"><strong>{conf_and_fixed_pct}</strong> confirmed or fixed</span>',
        '    </div>',
        '  </div>',
        # Card 2: Confirmed
        '  <div class="bugs-kpi-card kpi-confirmed-card">',
        '    <div class="kpi-header">',
        '      <span class="kpi-label">Confirmed</span>',
        '    </div>',
        f'    <div class="kpi-number">{conf}</div>',
        '    <div class="kpi-sub">',
        f'      <span class="kpi-badge kpi-badge-confirmed">{conf_pct}</span>',
        '      <span>Triaged by maintainers</span>',
        '    </div>',
        '  </div>',
        # Card 3: Fixed Upstream
        '  <div class="bugs-kpi-card kpi-fixed-card">',
        '    <div class="kpi-header">',
        '      <span class="kpi-label">Fixed Upstream</span>',
        '    </div>',
        f'    <div class="kpi-number">{fix}</div>',
        '    <div class="kpi-sub">',
        f'      <span class="kpi-badge kpi-badge-fixed">{fix_pct}</span>',
        '      <span>Patched in releases</span>',
        '    </div>',
        '  </div>',
        # Card 4: Under Review / Pending
        '  <div class="bugs-kpi-card kpi-pending-card">',
        '    <div class="kpi-header">',
        '      <span class="kpi-label">Under Review</span>',
        '    </div>',
        f'    <div class="kpi-number">{pend}</div>',
        '    <div class="kpi-sub">',
        f'      <span class="kpi-badge kpi-badge-pending">{pend_pct}</span>',
        '      <span>Awaiting maintainer triage</span>',
        '    </div>',
        '  </div>',
        # Card 5: Rejected
        '  <div class="bugs-kpi-card kpi-rejected-card">',
        '    <div class="kpi-header">',
        '      <span class="kpi-label">Rejected</span>',
        '    </div>',
        f'    <div class="kpi-number">{rej}</div>',
        '    <div class="kpi-sub">',
        f'      <span class="kpi-badge kpi-badge-rejected">{rej_pct}</span>',
        '      <span>Closed as invalid or duplicate</span>',
        '    </div>',
        '  </div>',
        '</div>',
    ]
    return "\n".join(html_parts)


def build_visuals_html(apps_data: List[Dict], total: int, conf: int, fix: int, pend: int, rej: int, bug_types: Dict[str, int]) -> str:
    max_app_count = max(app["total"] for app in apps_data) if apps_data else 1
    conf_and_fix_rate = f"{((conf + fix) / total * 100):.1f}%" if total else "0%"

    html_parts = [
        '<div class="bugs-visuals-grid">',
        # Left card: Stacked Bar Chart by Application
        '  <div class="bugs-chart-card">',
        '    <div class="chart-card-header">',
        '      <h3 class="chart-card-title">Reported Bugs by Application</h3>',
        '      <div class="chart-legend">',
        '        <span class="legend-item"><span class="legend-dot dot-confirmed"></span> Confirmed</span>',
        '        <span class="legend-item"><span class="legend-dot dot-fixed"></span> Fixed</span>',
        '        <span class="legend-item"><span class="legend-dot dot-pending"></span> Pending</span>',
        '        <span class="legend-item"><span class="legend-dot dot-rejected"></span> Rejected</span>',
        '      </div>',
        '    </div>',
        '    <div class="apps-bar-list">',
    ]

    for app in apps_data:
        app_total = app["total"]
        if app_total == 0:
            continue
        app_name = app["name"]
        app_slug = app["slug"]
        app_cat = app["category"]
        logo_svg = APP_LOGOS.get(app_slug, "")

        c = app["counts"]["Confirmed"]
        fx = app["counts"]["Fixed"]
        p = app["counts"]["Pending"]
        r = app["counts"]["Rejected"]

        track_scale = (app_total / max_app_count) * 100
        c_pct = (c / app_total) * track_scale
        fx_pct = (fx / app_total) * track_scale
        p_pct = (p / app_total) * track_scale
        r_pct = (r / app_total) * track_scale

        tooltip_text = f"{app_name}: {c} Confirmed, {fx} Fixed, {p} Pending, {r} Rejected ({app_total} total)"

        html_parts.extend([
            f'      <div class="app-bar-row" title="{html.escape(tooltip_text)}" style="cursor: pointer;" onclick="toggleAppAccordion(\'{app_slug}\')">',
            '        <div class="app-bar-info">',
            f'          <span class="app-bar-name">{logo_svg} <strong>{html.escape(app_name)}</strong> <span class="app-bar-domain">{html.escape(app_cat)}</span></span>',
            f'          <span class="app-bar-total">{app_total} bugs</span>',
            '        </div>',
            '        <div class="app-bar-track">',
            f'          <div class="bar-segment seg-confirmed" style="width: {c_pct:.2f}%;"></div>',
            f'          <div class="bar-segment seg-fixed" style="width: {fx_pct:.2f}%;"></div>',
            f'          <div class="bar-segment seg-pending" style="width: {p_pct:.2f}%;"></div>',
            f'          <div class="bar-segment seg-rejected" style="width: {r_pct:.2f}%;"></div>',
            '        </div>',
            '      </div>',
        ])

    html_parts.extend([
        '    </div>',
        '  </div>',
        # Right card: Status Breakdown & Donut Chart
        '  <div class="bugs-chart-card">',
        '    <div class="chart-card-header">',
        '      <h3 class="chart-card-title">Resolution Status</h3>',
        f'      <span class="kpi-badge kpi-badge-confirmed">{conf_and_fix_rate} Confirmed + Fixed</span>',
        '    </div>',
        '    <div class="donut-chart-container">',
        '      <canvas id="statusDonutChart" width="220" height="220" style="max-height: 220px;"></canvas>',
        '      <div class="donut-center-stat">',
        f'        <div class="donut-center-number">{conf + fix}</div>',
        '        <div class="donut-center-label">Confirmed &amp; Fixed</div>',
        '      </div>',
        '    </div>',
        '    <div class="status-stat-pills">',
        f'      <div class="status-stat-item stat-item-confirmed"><span><span class="status-dot dot-confirmed"></span> Confirmed</span> <strong>{conf} ({conf/total*100:.1f}%)</strong></div>',
        f'      <div class="status-stat-item stat-item-fixed"><span><span class="status-dot dot-fixed"></span> Fixed</span> <strong>{fix} ({fix/total*100:.1f}%)</strong></div>',
        f'      <div class="status-stat-item stat-item-pending"><span><span class="status-dot dot-pending"></span> Pending</span> <strong>{pend} ({pend/total*100:.1f}%)</strong></div>',
        f'      <div class="status-stat-item stat-item-rejected"><span><span class="status-dot dot-rejected"></span> Rejected</span> <strong>{rej} ({rej/total*100:.1f}%)</strong></div>',
        '    </div>',
    ])

    if bug_types:
        sorted_types = sorted(bug_types.items(), key=lambda x: x[1], reverse=True)
        html_parts.extend([
            '    <div class="bug-types-cloud">',
            '      <div class="bug-types-title">Classification by Bug Type</div>',
            '      <div class="bug-types-tags">',
        ])
        for btype, bcount in sorted_types:
            html_parts.append(
                f'        <span class="bug-type-tag">{html.escape(btype)} <span class="bug-type-count">{bcount}</span></span>'
            )
        html_parts.extend([
            '      </div>',
            '    </div>',
        ])

    html_parts.extend([
        '  </div>',
        '</div>',
    ])

    return "\n".join(html_parts)


def build_toolbar_html(total: int, conf: int, fix: int, pend: int, rej: int) -> str:
    html_parts = [
        '<div class="bugs-toolbar">',
        '  <div class="bugs-search-box">',
        '    <span aria-hidden="true" style="color: #64748b; font-size: 0.9rem;">🔍</span>',
        '    <input type="text" id="bugSearchInput" class="bugs-search-input" placeholder="Search by API, keyword, or title..." aria-label="Search bugs">',
        '  </div>',
        '  <div class="bugs-filter-group">',
        f'    <button class="filter-btn active" data-filter="all">All ({total})</button>',
        f'    <button class="filter-btn" data-filter="Confirmed"><span class="filter-dot dot-confirmed"></span>Confirmed ({conf})</button>',
        f'    <button class="filter-btn" data-filter="Fixed"><span class="filter-dot dot-fixed"></span>Fixed ({fix})</button>',
        f'    <button class="filter-btn" data-filter="Pending"><span class="filter-dot dot-pending"></span>Pending ({pend})</button>',
        f'    <button class="filter-btn" data-filter="Rejected"><span class="filter-dot dot-rejected"></span>Rejected ({rej})</button>',
        '  </div>',
        '  <div class="bugs-action-group">',
        '    <button class="action-btn" id="expandAllBtn">Expand All</button>',
        '    <button class="action-btn" id="collapseAllBtn">Collapse All</button>',
        f'    <span style="font-size: 0.8rem; color: #64748b; font-weight: 500; margin-left: 4px;">Showing <strong id="visibleCount" style="color: #0f172a;">{total}</strong> of {total}</span>',
        '  </div>',
        '</div>',
        '<div id="noBugsMessage" class="no-bugs-found">No reported bugs matched your filter or search query.</div>',
    ]
    return "\n".join(html_parts)


def build_collapsible_app_section(app: Dict, cached_titles: Dict[str, str]) -> str:
    app_name = app["name"]
    app_slug = app["slug"]
    app_cat = app["category"]
    app_total = app["total"]
    logo_svg = APP_LOGOS.get(app_slug, "")

    c = app["counts"]["Confirmed"]
    fx = app["counts"]["Fixed"]
    p = app["counts"]["Pending"]
    r = app["counts"]["Rejected"]

    html_parts = [
        f'<details class="app-collapsible-card" id="app-{app_slug}" data-app="{app_slug}">',
        '  <summary class="app-summary">',
        '    <div class="app-summary-left">',
        f'      {logo_svg}',
        f'      <span class="app-name-text">{html.escape(app_name)}</span>',
        f'      <span class="app-domain-pill">{html.escape(app_cat)}</span>',
        f'      <span class="app-count-badge">{app_total} bugs</span>',
        '    </div>',
        '    <div class="app-summary-right">',
        '      <div class="app-pills-row">',
    ]

    if c:
        html_parts.append(f'        <span class="mini-status-pill mini-confirmed">{c} Confirmed</span>')
    if fx:
        html_parts.append(f'        <span class="mini-status-pill mini-fixed">{fx} Fixed</span>')
    if p:
        html_parts.append(f'        <span class="mini-status-pill mini-pending">{p} Pending</span>')
    if r:
        html_parts.append(f'        <span class="mini-status-pill mini-rejected">{r} Rejected</span>')

    html_parts.extend([
        '      </div>',
        '      <span class="app-chevron-icon" aria-hidden="true">▼</span>',
        '    </div>',
        '  </summary>',
        '  <div class="app-details-body">',
        '    <div class="bugs-cards-list">',
    ])

    for row in app["rows"]:
        cat_status = categorize_status(row.get("status") or "")
        status_slug = cat_status.lower()

        api = (row.get("api(s)") or row.get("api") or "").strip()
        link = (row.get("link") or "").strip()
        pr_link = (row.get("pr_link") or "").strip()
        raw_note = (row.get("note") or "").strip()
        btype = (row.get("bug_type") or "").strip()
        tool = (row.get("tool") or "").strip()

        # Resolve clean uniform title
        norm_url = link.rstrip("/").lower()
        title = ""
        if norm_url in cached_titles:
            title = cached_titles[norm_url]
        elif raw_note and not re.match(r"^\d+$", raw_note) and raw_note not in ["Invalid input", "SIGABRT"]:
            title = raw_note
        elif api:
            title = f"Issue reported in {api}"
        else:
            title = "Reported issue"

        rejection_flag = ""
        if cat_status == "Rejected":
            rejection_flag = extract_rejection_flag(raw_note)

        link_label = format_link_label(link)
        pr_label = format_pr_label(pr_link) if pr_link else ""

        # Search index content
        search_terms = f"{api} {title} {btype} {tool} {link} {pr_link} {cat_status}".lower()

        html_parts.extend([
            f'      <div class="bug-card-row" data-status="{cat_status}" data-search="{html.escape(search_terms)}">',
            '        <div class="bug-row-main">',
            '          <div class="bug-row-tags">',
            f'            <span class="bug-status-badge badge-{status_slug}"><span class="status-dot dot-{status_slug}"></span>{cat_status}</span>',
        ])

        if api:
            html_parts.append(f'            <span class="bug-api-code">{html.escape(api)}</span>')
        if btype:
            html_parts.append(f'            <span class="bug-type-pill">{html.escape(btype)}</span>')
        if rejection_flag:
            html_parts.append(f'            <span class="bug-flag-pill">{html.escape(rejection_flag)}</span>')
        if tool:
            html_parts.append(f'            <span class="bug-tool-pill">{html.escape(tool)}</span>')

        html_parts.append('          </div>')

        # Uniform body: always the clean official title
        html_parts.append(f'          <div class="bug-title-text">{html.escape(title)}</div>')

        html_parts.extend([
            '        </div>',
            '        <div class="bug-row-actions">',
            f'          <a href="{html.escape(link)}" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">{html.escape(link_label)}</a>',
        ])

        if pr_link:
            html_parts.append(
                f'          <a href="{html.escape(pr_link)}" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">{html.escape(pr_label)}</a>'
            )

        html_parts.extend([
            '        </div>',
            '      </div>',
        ])

    html_parts.extend([
        '    </div>',
        '  </div>',
        '</details>',
    ])

    return "\n".join(html_parts)


def build_client_javascript(total: int, conf: int, fix: int, pend: int, rej: int) -> str:
    js_code = f"""
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<script>
(function() {{
  // 1. Chart.js Donut Initialization
  function initChart() {{
    const ctx = document.getElementById('statusDonutChart');
    if (!ctx || typeof Chart === 'undefined') return;

    new Chart(ctx, {{
      type: 'doughnut',
      data: {{
        labels: ['Confirmed', 'Fixed', 'Pending', 'Rejected'],
        datasets: [{{
          data: [{conf}, {fix}, {pend}, {rej}],
          backgroundColor: ['#10b981', '#3b82f6', '#f59e0b', '#ef4444'],
          borderWidth: 2,
          borderColor: '#ffffff',
          hoverOffset: 6
        }}]
      }},
      options: {{
        responsive: true,
        maintainAspectRatio: false,
        cutout: '72%',
        plugins: {{
          legend: {{ display: false }},
          tooltip: {{
            callbacks: {{
              label: function(context) {{
                const val = context.parsed;
                const total = {total};
                const pct = ((val / total) * 100).toFixed(1);
                return ' ' + context.label + ': ' + val + ' (' + pct + '%)';
              }}
            }}
          }}
        }}
      }}
    }});
  }}

  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', initChart);
  }} else {{
    initChart();
  }}

  // 2. Global helper to toggle an accordion and scroll to it
  window.toggleAppAccordion = function(slug) {{
    const el = document.getElementById('app-' + slug);
    if (!el) return;
    el.open = true;
    el.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
  }};

  // 3. Search and Status Filtering
  document.addEventListener('DOMContentLoaded', function() {{
    const searchInput = document.getElementById('bugSearchInput');
    const filterBtns = document.querySelectorAll('.filter-btn');
    const expandAllBtn = document.getElementById('expandAllBtn');
    const collapseAllBtn = document.getElementById('collapseAllBtn');
    const visibleCountEl = document.getElementById('visibleCount');
    const noBugsMsg = document.getElementById('noBugsMessage');
    const appCards = document.querySelectorAll('.app-collapsible-card');

    let activeFilter = 'all';

    function applyFilters() {{
      const query = (searchInput ? searchInput.value : '').toLowerCase().trim();
      let visibleCount = 0;

      appCards.forEach(function(card) {{
        let cardHasMatch = false;
        const rows = card.querySelectorAll('.bug-card-row');

        rows.forEach(function(row) {{
          const rowStatus = row.getAttribute('data-status');
          const rowSearch = row.getAttribute('data-search') || '';

          const statusMatch = (activeFilter === 'all') || (rowStatus === activeFilter);
          const queryMatch = !query || rowSearch.indexOf(query) !== -1;

          if (statusMatch && queryMatch) {{
            row.style.display = '';
            visibleCount++;
            cardHasMatch = true;
          }} else {{
            row.style.display = 'none';
          }}
        }});

        if (cardHasMatch) {{
          card.style.display = '';
          if (query || activeFilter !== 'all') {{
            card.open = true;
          }}
        }} else {{
          card.style.display = 'none';
        }}
      }});

      if (visibleCountEl) {{
        visibleCountEl.textContent = visibleCount;
      }}
      if (noBugsMsg) {{
        noBugsMsg.style.display = (visibleCount === 0) ? 'block' : 'none';
      }}
    }}

    if (searchInput) {{
      searchInput.addEventListener('input', applyFilters);
    }}

    filterBtns.forEach(function(btn) {{
      btn.addEventListener('click', function() {{
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeFilter = btn.getAttribute('data-filter') || 'all';
        applyFilters();
      }});
    }});

    if (expandAllBtn) {{
      expandAllBtn.addEventListener('click', function() {{
        appCards.forEach(card => card.open = true);
      }});
    }}

    if (collapseAllBtn) {{
      collapseAllBtn.addEventListener('click', function() {{
        appCards.forEach(card => card.open = false);
      }});
    }}
  }});
}})();
</script>
"""
    return js_code


def main():
    cached_titles = load_cached_titles()
    print(f"Loaded {len(cached_titles)} cached titles from bugs_data/.")

    total_bugs = 0
    total_confirmed = 0
    total_fixed = 0
    total_pending = 0
    total_rejected = 0

    bug_types: Dict[str, int] = {}
    apps_data: List[Dict] = []

    for cfg in APP_CONFIGS:
        csv_file = BUGS_DIR / cfg["file"]
        rows = read_issues(csv_file)
        counts = {"Confirmed": 0, "Fixed": 0, "Pending": 0, "Rejected": 0}

        for r in rows:
            cat = categorize_status(r.get("status") or "")
            counts[cat] += 1
            btype = (r.get("bug_type") or "").strip()
            if btype:
                btype_norm = btype.capitalize()
                bug_types[btype_norm] = bug_types.get(btype_norm, 0) + 1

        total = len(rows)
        total_bugs += total
        total_confirmed += counts["Confirmed"]
        total_fixed += counts["Fixed"]
        total_pending += counts["Pending"]
        total_rejected += counts["Rejected"]

        apps_data.append({
            "name": cfg["name"],
            "slug": cfg["slug"],
            "category": cfg["category"],
            "rows": rows,
            "counts": counts,
            "total": total,
        })

    # Sort apps by count descending
    apps_data.sort(key=lambda x: x["total"], reverse=True)

    now = datetime.now(timezone.utc)
    iso_ts = now.isoformat(timespec="seconds")
    formatted_ts = now.strftime("%Y-%m-%d %H:%M:%S UTC")

    content = []
    content.append("---")
    content.append("layout: page")
    content.append("title: Reported Bugs")
    content.append("permalink: /bugs/")
    content.append(f'last_updated: "{iso_ts}"')
    content.append("---\n")

    content.append('<div class="bugs-dashboard">')

    # Factual Hero Banner without promotional jargon
    content.append('  <div class="bugs-hero-banner">')
    content.append('    <h1 class="bugs-hero-title">Reported Bugs</h1>')
    content.append(
        '    <p class="bugs-hero-subtitle">'
        f'A list of <strong>{total_bugs} bugs and issues</strong> reported across <strong>11 open-source applications</strong> '
        'spanning deep learning frameworks (PyTorch, TensorFlow, JAX), LLM serving engines (vLLM, SGLang), '
        'databases (ArangoDB, PostgreSQL), compilers (Clang/LLVM, GCC), and system utilities (cronie, OpenSSH). '
        f'<strong>{((total_confirmed + total_fixed) / total_bugs * 100):.1f}%</strong> have been confirmed or fixed upstream.'
        '</p>'
    )
    content.append('    <div class="bugs-hero-meta">')
    content.append(f'      <span class="bugs-meta-pill">Last updated: {formatted_ts}</span>')
    content.append('      <span class="bugs-meta-pill">11 Applications</span>')
    content.append(f'      <a class="bugs-sheet-link" href="{SPREADSHEET_URL}" target="_blank" rel="noopener noreferrer">Spreadsheet: Google Sheets ↗</a>')
    content.append('    </div>')
    content.append('  </div>\n')

    # Headline KPI Metric Cards
    content.append(build_kpi_cards_html(total_bugs, total_confirmed, total_fixed, total_pending, total_rejected))
    content.append("\n")

    # Visual Charts Grid
    content.append(build_visuals_html(apps_data, total_bugs, total_confirmed, total_fixed, total_pending, total_rejected, bug_types))
    content.append("\n")

    # Filter & Search Toolbar
    content.append(build_toolbar_html(total_bugs, total_confirmed, total_fixed, total_pending, total_rejected))
    content.append("\n")

    # Collapsible Application Sections
    content.append('<div class="bugs-apps-accordion">')
    for app in apps_data:
        content.append(build_collapsible_app_section(app, cached_titles))
    content.append('</div>')

    # Client JavaScript
    content.append(build_client_javascript(total_bugs, total_confirmed, total_fixed, total_pending, total_rejected))

    content.append("</div>\n")

    OUT_FILE.write_text("\n".join(content), encoding="utf-8")
    print(f"Successfully generated {OUT_FILE} with {total_bugs} bugs across {len(apps_data)} applications.")

    # Automatically keep Reported_Bugs_Complete.xlsx and google_apps_script.js in sync
    try:
        import sys
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from export_sheets_workbook import build_excel_workbook, build_apps_script
        build_excel_workbook(cached_titles)
        build_apps_script(cached_titles)
    except Exception as e:
        print(f"[Notice] Excel/Apps Script sync skipped: {e}")


if __name__ == "__main__":
    main()
