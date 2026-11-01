# Welcome to the website of M M Abid Naziri

This is a repo containing the portfolio website for me (M M Abid Naziri). It was created using jekyll.
To build and run the server locally, run:

```bash
$ bash scripts/serve_locally.sh
```

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
$ bundle exec jekyll serve --config _config.yml,_config.legacy.yml
```

GitHub Pages only reads `_config.yml`, so the deployed site always follows
the value set there.

[![Pages build](https://github.com/abidnazirisami/abidnazirisami.github.io/actions/workflows/pages/pages-build-deployment/badge.svg?branch=main)](https://github.com/abidnazirisami/abidnazirisami.github.io/actions/workflows/pages/pages-build-deployment)