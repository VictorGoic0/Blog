# Progress

## What Works

- **PR #1 (DNS & subdomain):** Complete. SquareSpace CNAME for `blog` → GitHub Pages; CNAME file at repo root with `blog.victorgoico.com`.
- **PR #2 (structure & build):** Complete. `build.py` with --clean and optional post path; discovery/parsing; frontmatter (title, date, tags, description); Markdown→HTML; Jinja2 base/post/index; output to output/.
- **PR #3 (templates & Sass):** Complete. Semantic base (meta placeholders, nav, footer + social), post (article, date/tags/read time), index (excerpts, tag filter UI). Sass design tokens and blog.scss; code blocks, responsive; build copies css to output/.
- **PR #4 (SEO, RSS, sitemap):** Complete. Meta, canonical, Open Graph, Twitter Card, JSON-LD; feed.xml (RSS 2.0), sitemap.xml, robots.txt.
- **PR #5 (tags/categories):** Complete. Tag index (tag → posts), "All tags" section with counts, ?tag= pre-select on index, filter buttons with counts.
- **PR #6 (GA4):** Complete. GA4_MEASUREMENT_ID in build.py, tracking code in base.html, README docs.
- **PR #7 (GitHub Pages deployment):** Complete. GitHub Actions workflow builds Sass + Python on push to master, copies CNAME into output/, deploys to Pages. Site live at blog.victorgoico.com.
- **PR #8 (first post & docs):** Complete. First post live (Why is Bitcoin King? Part One: The History). README updated with writing guide, Markdown/HTML reference, deployment and GA4 docs.

## What's Left to Build

| PR   | Scope                              | Status   |
|------|------------------------------------|----------|
| #1   | DNS & subdomain                    | Done     |
| #2   | Project structure & build script  | Done     |
| #3   | HTML templates & Sass design      | Done     |
| #4   | SEO, RSS, sitemap                  | Done     |
| #5   | Tags/categories                    | Done     |
| #6   | Google Analytics 4                 | Done     |
| #7   | GitHub Pages deployment            | Done     |
| #8   | First post & documentation         | Done     |

## Redesign

| Phase | Scope | Status |
|-------|-------|--------|
| Phase 1 | Article page layout (`page-design.png`) — header logo/nav, post meta above title, author attribution, tag filter hidden | Done |
| Phase 2 | Article list page layout (`list-design.png`) | Pending |

## Current Status

- **Phase:** All PRs complete. Blog is live. Redesign Phase 1 complete.
- **Blocker:** None.

## Known Issues

- None.
