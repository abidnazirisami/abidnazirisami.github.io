#!/usr/bin/env python3
"""
Write _data/bug_stats.json, the bug counts the homepage trophy case reads.

The counts come from the same CSVs and the same status rules as the bugs page,
so the homepage and /bugs/ cannot disagree. This script only reads bugs/*.csv;
it does not touch bugs.md.

Usage:
    python3 scripts/generate_bug_stats.py
"""

import json
import sys
from datetime import date
from pathlib import Path
from typing import Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_bugs_page import APP_CONFIGS, BUGS_DIR, REPO_ROOT, categorize_status, read_issues

DATA_DIR = REPO_ROOT / "_data"
OUT_FILE = DATA_DIR / "bug_stats.json"

# The homepage groups the systems into these domains, in this order.
DOMAINS = [
    ("Deep learning libraries", ["pytorch", "tensorflow", "jax"]),
    ("LLM serving engines", ["vllm", "sglang"]),
    ("Databases", ["arangodb", "postgresql"]),
    ("Compilers", ["clang_llvm", "gcc"]),
    ("System software", ["cronie", "openssh"]),
]


def collect_stats() -> Dict:
    """Count reports per system and per domain."""
    configs = {cfg["slug"]: cfg for cfg in APP_CONFIGS}

    grouped = {slug for _, slugs in DOMAINS for slug in slugs}
    missing = sorted(set(configs) - grouped)
    if missing:
        sys.exit(f"No domain for {missing}. Add each one to DOMAINS in {Path(__file__).name}.")

    totals = {"Confirmed": 0, "Fixed": 0, "Pending": 0, "Rejected": 0}
    domains: List[Dict] = []

    for domain_name, slugs in DOMAINS:
        systems = []
        for slug in slugs:
            cfg = configs[slug]
            counts = {"Confirmed": 0, "Fixed": 0, "Pending": 0, "Rejected": 0}
            for row in read_issues(BUGS_DIR / cfg["file"]):
                counts[categorize_status(row.get("status") or "")] += 1
            for status, n in counts.items():
                totals[status] += n
            systems.append({
                "name": cfg["name"].replace(" / ", "/"),
                "slug": slug,
                "total": sum(counts.values()),
                "confirmed": counts["Confirmed"],
                "fixed": counts["Fixed"],
                "accepted": counts["Confirmed"] + counts["Fixed"],
            })
        systems.sort(key=lambda s: s["accepted"], reverse=True)
        domains.append({"name": domain_name, "systems": systems})

    total = sum(totals.values())
    accepted = totals["Confirmed"] + totals["Fixed"]
    return {
        "generated": date.today().isoformat(),
        "total": total,
        "confirmed": totals["Confirmed"],
        "fixed": totals["Fixed"],
        "accepted": accepted,
        "pending": totals["Pending"],
        "rejected": totals["Rejected"],
        "accepted_pct": f"{accepted / total * 100:.1f}" if total else "0.0",
        "system_count": len(configs),
        "domain_count": len(DOMAINS),
        "domains": domains,
    }


def main() -> None:
    stats = collect_stats()
    DATA_DIR.mkdir(exist_ok=True)
    OUT_FILE.write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")
    print(
        f"Wrote {OUT_FILE.relative_to(REPO_ROOT)}: {stats['total']} reported, "
        f"{stats['accepted']} confirmed or fixed, {stats['system_count']} systems."
    )


if __name__ == "__main__":
    main()
