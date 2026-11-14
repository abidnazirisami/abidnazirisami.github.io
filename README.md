# Welcome to the website of M M Abid Naziri

This is a repo containing the portfolio website for me (M M Abid Naziri). It was created using jekyll.
To build and run the server locally, run:

```bash
$ bash scripts/serve_locally.sh
```

## Where the content lives

The homepage (`index.markdown`) holds every section, and the header links jump
to them. Only the bug list (`bugs.md`) and the undergraduate projects
(`projects.md`) are separate pages.

| What | File |
| --- | --- |
| Header links | `_data/navigation.yml` |
| Experience, Education, Awards, Volunteering | `_data/cv.yml`, rendered by `_includes/timeline.html` |
| Publications | `_includes/publications_list.md` |
| News | `_includes/news.md` |
| Reported Bugs counts | `_data/bug_stats.json` (generated, see `README-bugs.md`) |

The Resume button opens `resume.pdf` directly. `/publications/`, `/resume/`
and `/co-curricular/` only forward to their new place (`_layouts/redirect.html`).

`experience.md` is the earlier, longer Experience page. It is still built at
`/experience/` but nothing links to it. To use it again, set the Experience
url in `_data/navigation.yml` to `/experience/`.

## Frontend variants

The site ships two frontends. `frontend` in `_config.yml` picks the one that
gets built:

| value | what you get |
| --- | --- |
| `modern` (default) | the current design, with a light/dark toggle |
| `legacy` | the pre-redesign Minima look |

Page content is shared by both, so there is only ever one copy of it. The
split lives in `_includes/{modern,legacy}/`, in the `site.frontend` branches
in `_layouts/`, and in `assets/main.scss`, which imports either `_sass/abid/`
or `_sass/legacy/`.

To preview the legacy build without editing `_config.yml`:

```bash
$ bash scripts/serve_locally.sh --config _config.yml,_config.legacy.yml
```

GitHub Pages only reads `_config.yml`, so the deployed site always follows
the value set there.

[![Pages build](https://github.com/abidnazirisami/abidnazirisami.github.io/actions/workflows/pages/pages-build-deployment/badge.svg?branch=main)](https://github.com/abidnazirisami/abidnazirisami.github.io/actions/workflows/pages/pages-build-deployment)