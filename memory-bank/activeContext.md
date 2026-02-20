# Active Context

## Current Focus

- PR #4 complete. Next: PR #5 (tags/categories) or PR #6/#7.
- PR #1–#3 done. Repo is blog-only.

## Recent Changes

- **PR #4:** SEO: base.html meta (description, keywords block, canonical, Open Graph, Twitter Card), RSS link in head. Post template: canonical, og/twitter overrides, JSON-LD (BlogPosting) via build.py. build.py: SITE_URL, env.globals["site_url"], json_ld per post; generates feed.xml (RSS 2.0), sitemap.xml (urlset, lastmod, priority, changefreq), robots.txt (Allow /, Sitemap).

## Next Steps

1. **PR #5:** Tags/categories (extract, index, tag pages or filtering—filtering already in PR #3).
2. Then PR #6 (GA4), #7 (deployment), #8 (portfolio nav), #9 (first post & docs).

## Active Decisions

- Build output: `output/` directory; CNAME must be present in deployed root (repo root or copied into output when using output/ as Pages source).
- Design: follow `designs/` and PRD design specs; implement via Sass variables in `scss/`.
- Portfolio link to blog: implemented in portfolio repo (PR #8), not in this repo.
