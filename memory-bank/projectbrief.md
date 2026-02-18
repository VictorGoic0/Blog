# Project Brief: Custom Blog System

## Core Requirements

Build a custom markdown-based blog system with:

- Automated HTML generation via a Python build script
- SEO optimization (meta tags, Open Graph, Twitter Cards, JSON-LD, sitemap, robots.txt)
- RSS feed (RSS 2.0)
- Analytics (Google Analytics 4)
- Tags and categories with filtering
- Deployment on subdomain **blog.victorgoico.com** (GitHub Pages, CNAME via SquareSpace DNS)
- Clean, minimal design separate from the main portfolio

Design reference materials live in **`designs/`** and must be used as the guideline for styles, layout, and visual treatment.

## Goals

- Professional blogging platform to share technical knowledge and build audience
- Thought leadership and increased reach for job opportunities
- Full control over design, features, and content
- Optimized for SEO and discoverability
- Support cross-posting workflow: Blog → Twitter → Medium → LinkedIn

## Scope (PRs)

Work is organized into 9 PRs:

1. **DNS & subdomain** — CNAME for blog.victorgoico.com (critical first)
2. **Project structure & build script** — `blog/` layout, `build.py`, markdown → HTML
3. **HTML templates & design** — Base/post/index templates, **Sass** design system, follow `designs/`
4. **SEO, RSS, sitemap** — Meta, feed.xml, sitemap.xml, robots.txt
5. **Tags/categories** — Frontmatter tags, index filtering, tag badges
6. **Google Analytics** — GA4 on blog
7. **GitHub Pages deployment** — Repo/branch, Pages config, CNAME in output
8. **Portfolio nav** — Blog link from portfolio (after DNS + deployment)
9. **First post & docs** — Sample post, README, content workflow

## Out of Scope (Initial)

- Comments, related posts, social share buttons (Phase 2)
- Search, archive, newsletter (Phase 3)
- Dark mode, TOC, image optimization, print (Phase 4)
