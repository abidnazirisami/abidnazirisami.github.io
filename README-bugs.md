Regenerate Bugs Page
---------------------

When you update the CSVs in `bugs/`, regenerate the page:

1. Ensure Python 3 is installed.
2. Run the generator:

   python3 scripts/generate_bugs_page.py

3. Rebuild locally to preview:

   bundle exec jekyll build

The output is written to `bugs.md` at the repo root and published at `/bugs/`.
