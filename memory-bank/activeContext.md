# Active Context

## Current Focus

- PR #6 complete. Next: PR #7 (deployment) or PR #8 (first post & docs).
- PR #1–#6 done. Repo is blog-only.

## Recent Changes

- **PR numbering:** Former PR #9 (First post & documentation) renumbered to PR #8. All PRD and memory-bank references updated.
- **PR #6:** GA4 tracking code in base.html (gated by GA4_MEASUREMENT_ID in build.py); README analytics section.

## Next Steps

1. **PR #7:** GitHub Pages deployment (Actions workflow, CNAME in output).
2. **PR #8:** First post & documentation.

## Active Decisions

- Build output: `output/` directory; CNAME must be present in deployed root (repo root or copied into output when using output/ as Pages source).
- Design: follow `designs/` and PRD design specs; implement via Sass variables in `scss/`.
