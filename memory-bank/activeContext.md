# Active Context

## Current Focus

- Memory Bank initialized from PRD. Next: start implementation per PR #2 (project structure and build script core).
- PR #1 (DNS and CNAME) is done; CNAME exists at repo root. Repo is blog-only.

## Recent Changes

- PRD and README updated for blog-only repo (no portfolio in same repo; one CNAME per GitHub Pages repo).
- Memory Bank created: projectbrief, productContext, systemPatterns, techContext, activeContext, progress.

## Next Steps

1. **PR #2:** Set up directory structure (posts/, templates/, scss/, css/, output/), .gitignore, requirements.txt, build.py skeleton with discovery and parsing, frontmatter, HTML generation, output writing, README usage.
2. After PR #2: PR #3 (templates + Sass design), then PR #4 (SEO, RSS, sitemap), then remaining PRs per PRD order.

## Active Decisions

- Build output: `output/` directory; CNAME must be present in deployed root (repo root or copied into output when using output/ as Pages source).
- Design: follow `designs/` and PRD design specs; implement via Sass variables in `scss/`.
- Portfolio link to blog: implemented in portfolio repo (PR #8), not in this repo.
