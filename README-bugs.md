Regenerate Bugs Page
---------------------

When you update the CSVs in `bugs/`, regenerate the page:

1. Ensure Python 3 is installed.
2. If `bugs/rq3_bugs_reported.csv` changed, split it into the per-application CSVs first:

       python3 scripts/split_rq3_bugs.py

   A report marked `Fixed=yes` there is listed as Fixed. `rq3_bugs_reported.csv` is the paper's snapshot, so statuses that changed on the tracker afterwards go in `bugs/status_updates.csv` (one row per issue link); the script applies them on top.

   It writes `Agentic-PBT` in the `tool` column. The model behind each run stays in the `Model` column of `rq3_bugs_reported.csv`.

3. Run the generator:

       python3 scripts/generate_bugs_page.py

4. Preview locally:

       bash scripts/serve_locally.sh

The output is written to `bugs.md` at the repo root and published at `/bugs/`. The generator also rewrites `bugs/Reported_Bugs_Complete.xlsx` and `scripts/google_apps_script.js` (this step needs `openpyxl` and is skipped without it) and `_data/bug_stats.json`.

Both scripts are safe to rerun: with unchanged CSVs they reproduce the same files, apart from the "Last updated" time.

Issue titles come from `bugs/titles.json`, which is committed. The scripts add to it whenever `bugs_data/` holds newer titles (see the next section), so a clone without `bugs_data/` still produces the full page. A new GitHub issue shows its CSV note as the title until you fetch its details once.

Homepage Reported Bugs Section
------------------------------

The Reported Bugs section of the homepage reads `_data/bug_stats.json`, which holds the counts per system and per domain. The generator above rewrites it. To refresh only this file, without touching `bugs.md`, run:

    python3 scripts/generate_bug_stats.py

A new application also needs a domain in `DOMAINS` in `scripts/generate_bug_stats.py`.

Fetch GitHub Issue Details
--------------------------

To fetch or update local cached details of GitHub issues and pull requests (for offline LLM agent review):

1. Set your token: `export GITHUB_TOKEN="<your_token>"` (or pass `--token <your_token>`).
2. Run the script:

   ```bash
   python3 scripts/fetch_issue_details.py
   ```

   Options:
   - `--force`: Force refresh all issue details bypassing ETag cache.
   - `--csv <name.csv>`: Process only a specific CSV file (e.g. `--csv pytorch.csv`).
   - `--limit <N>`: Limit number of issues to fetch per CSV.
   - `--no-comments`: Skip fetching issue comments.
   - `--no-pr`: Skip fetching pull request details.

All issue data is cached under `bugs_data/` (gitignored), including `bugs_data/summary.json` for rapid agent inspection.

Update Google Sheet
--------------------

To update your Google Sheet (`https://docs.google.com/spreadsheets/d/1r03ajIybbPeLBqHdxbD54Qghwoy8NjL2weeh89vX7wM/edit`):

### Option A: 1-Click Google Apps Script (Fastest, no installation)
1. Open your sheet: https://docs.google.com/spreadsheets/d/1r03ajIybbPeLBqHdxbD54Qghwoy8NjL2weeh89vX7wM/edit
2. Click **Extensions > Apps Script**.
3. Replace the contents of `Code.gs` with [scripts/google_apps_script.js](file:///home/mnaziri/Documents/Personal/abidnazirisami.github.io/scripts/google_apps_script.js).
4. Click **Save** (floppy icon) and then **Run**.
5. All 11 application sheets will be automatically created and populated!

### Option B: Upload Master Excel Workbook
1. Open the sheet and click **File > Import > Upload**.
2. Select [bugs/Reported_Bugs_Complete.xlsx](file:///home/mnaziri/Documents/Personal/abidnazirisami.github.io/bugs/Reported_Bugs_Complete.xlsx).
3. Select **Replace spreadsheet** or **Insert new sheet(s)**.

### Option C: Python Script (with Google Credentials)
Run:
```bash
python3 scripts/update_google_sheet.py --credentials path/to/service_account.json
# or
python3 scripts/update_google_sheet.py --token "<oauth_access_token>"
```

