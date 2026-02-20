# Active Context

## Current Focus

- Redesign Phase 1 complete. Visual layout now matches `designs/page-design.png`.
- Next: Redesign Phase 2 — implement `designs/list-design.png` (article list page).

## Recent Changes

- **Redesign Phase 1:** Implemented page-design.png one-to-one.
  - `base.html`: Header restructured — `GOICOLOG_` logo left, `Articles` + `About` nav right. About links to `victorgoico.com/#about`.
  - `post.html`: Post meta moved above title. Meta line is now `date · By Victor M. Goico · N min read`. Author links to `victorgoico.com`. Tags commented out (preserved for phase 2).
  - `index.html`: Tag filter UI, all-tags section, per-item tag badges, and filter JS all commented out with `{# #}` (preserved for phase 2).
  - `scss/blog.scss`: Removed header `border-bottom`. Added `.site-header-inner` flex layout (logo left, nav right). Color set once on `.site-header-inner` so logo and nav inherit black. Added `.author-link` style.

## Next Steps

- Implement `designs/list-design.png` (Redesign Phase 2).
- Write content for Bitcoin series Parts 2–5.
- Future enhancements per PRD Phase 2–4 (comments, search, dark mode, etc.) when ready.

## Active Decisions

- Deploy via GitHub Actions on push to master; `output/` is gitignored and never committed.
- CNAME is copied into `output/` by the workflow (`cp CNAME output/`) before deploy.
- Sass compiled via `npm run build:css`; must be run locally before committing `css/blog.css` for local preview.
- Tag filter functionality is commented out (not deleted) in templates — re-enable in a future redesign phase.
- Completed plan docs moved to `old-docs/`.
