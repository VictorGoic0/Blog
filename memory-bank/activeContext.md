# Active Context

## Current Focus

- Both redesign phases complete. Blog is live and visually matches both designs.
- Next: Write content for Bitcoin series Parts 2–5.

## Recent Changes

- **Redesign Phase 1:** Implemented `page-design.png` one-to-one.
  - `base.html`: Header restructured — `GOICOLOG_` logo left, `Articles` + `About` nav right. About links to `victorgoico.com/#about`. Added `{% block body_class %}` and `{% block main_class %}` extension points.
  - `post.html`: Post meta moved above title. Meta line is `date · By Victor M. Goico · N min read`. Author links to `victorgoico.com`. Tags commented out (preserved for future phase).
  - `index.html`: Tag filter UI, all-tags section, per-item tag badges, and filter JS all commented out with `{# #}`.
  - `scss/blog.scss`: Header `border-bottom` restored. `.site-header-inner` flex layout. Color inherited from container. `.author-link` style added.

- **Redesign Phase 2:** Implemented `list-design.png` one-to-one.
  - `build.py`: Added `date_short` field (`YY.MM.DD` format).
  - `index.html`: Rebuilt with hero section (headline + subtitle) and article card list. `page-articles` body class suppresses header/footer borders on this page only. `main-content--wide` gives 1400px max-width.
  - `scss/blog.scss`: Added all article list styles — `.articles-hero`, `.article-card` two-column layout, `.article-card-meta` (330px, date + `tags[0]` as category + author pinned to bottom), `.article-card-body`, `.article-tag` non-clickable badge, `.read-article-btn` outlined pill.
  - `scss/_variables.scss`: Added `$color-border-dark: #b0b0b0` and `$content-max-width-wide: 1400px`.
  - Tag filter stays commented out — will re-enable in the hero section once there are multiple articles.

## Next Steps

- Write content for Bitcoin series Parts 2–5.
- Re-enable tag filter in the articles hero section once several articles exist.
- Future enhancements per PRD Phase 2–4 (comments, search, dark mode, etc.) when ready.

## Active Decisions

- Deploy via GitHub Actions on push to master; `output/` is gitignored and never committed.
- CNAME is copied into `output/` by the workflow (`cp CNAME output/`) before deploy.
- Sass compiled via `npm run build:css`; must be run locally before committing `css/blog.css` for local preview.
- Tag filter functionality is commented out (not deleted) — re-enable when article count warrants it.
- Convention: first tag in a post's `tags` list is the primary category, displayed in the article card left column.
- Completed plan docs moved to `old-docs/`.
