# Progress

## What Works

- **PR #1 (DNS & subdomain):** Complete. SquareSpace CNAME for `blog` → GitHub Pages; CNAME file at repo root with `blog.victorgoico.com`; DNS documented in README.
- **PR #2 (structure & build):** Complete. `build.py` with --clean and optional post path; discovery/parsing; frontmatter (title, date, tags, description); Markdown→HTML; Jinja2 base/post/index; output to output/; sample post; README usage.
- **PR #3 (templates & Sass):** Complete. Semantic base (meta placeholders, nav, footer + social), post (article, date/tags/read time), index (excerpts, tag filter UI). Sass design tokens and blog.scss; code blocks, responsive; build copies css to output/.
- **PR #4 (SEO, RSS, sitemap):** Complete. Meta, canonical, Open Graph, Twitter Card, JSON-LD; feed.xml (RSS 2.0), sitemap.xml, robots.txt.
- **PR #5 (tags/categories):** Complete. Tag index (tag → posts), "All tags" section with counts, ?tag= pre-select on index, filter buttons with counts.
- **PR #6 (GA4):** Complete. GA4_MEASUREMENT_ID in build.py, tracking code in base.html, README docs.
- **Repo:** Blog-only; PRD and README aligned. Memory Bank initialized.

## What's Left to Build

| PR   | Scope                              | Status   |
|------|------------------------------------|----------|
| #2   | Project structure & build script  | Done     |
| #3   | HTML templates & Sass design      | Done     |
| #4   | SEO, RSS, sitemap                  | Done     |
| #5   | Tags/categories                    | Done     |
| #6   | Google Analytics 4                 | Done     |
| #7   | GitHub Pages deployment            | Not started |
| #8   | First post & documentation         | Not started |

## Current Status

- **Phase:** GA4 done. Ready for PR #7 (deployment) or PR #8 (first post & docs).
- **Blocker:** None. Live site after PR #7 and deployment config.

## Known Issues

- None. CNAME is at repo root; if GitHub Pages source is set to output/, CNAME must be copied into output/ at deploy time (or use a workflow that does so).
