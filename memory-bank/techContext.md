# Tech Context

## Technologies

- **Static site generation:** Custom Python build script (`build.py`).
- **Content:** Markdown with YAML frontmatter (title, date, tags, description).
- **Templating:** Jinja2.
- **Styling:** Sass compiled to CSS. Design tokens in `scss/_variables.scss` (colors, spacing, typography); main entry `scss/blog.scss` → `css/blog.css`. Sass tooling to be installed as needed (e.g. `sass` npm package).
- **Hosting:** GitHub Pages.
- **Domain:** blog.victorgoico.com (subdomain; DNS via SquareSpace CNAME to GitHub Pages).
- **Analytics:** Google Analytics 4.

## Directory Structure (blog/)

- `build.py` — Markdown → HTML converter
- `requirements.txt` — Python deps
- `posts/` — Source markdown (YYYY-MM-DD-slug.md)
- `templates/` — base.html, post.html, index.html
- `scss/` — _variables.scss, blog.scss (source)
- `css/` — blog.css (compiled)
- `output/` — Generated site (gitignored): posts/, index.html, feed.xml, sitemap.xml
- `.gitignore`, `CNAME`, `README.md`

## Dependencies (Python)

- markdown >= 3.5
- python-frontmatter >= 1.1.0
- Jinja2 >= 3.1.2

Sass: install per PR #3 (e.g. npm `sass` or Python libsass).

## Development Setup

- Python env for build script; optionally Node/npm if using `sass` for compilation.
- Run `python build.py` to generate output; run Sass compile when changing `scss/`.
- Design reference: `designs/` at repo root (page-design.png, list-design.png, etc.).

## Constraints

- GitHub Pages: static files only; no server-side logic.
- SquareSpace DNS: CNAME record for `blog` subdomain.
- Portfolio (index.html) is separate; blog link added in PR #8 after blog is live.
