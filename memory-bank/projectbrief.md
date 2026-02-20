# Project Brief: Custom Blog System

## Purpose

Build a custom markdown-based blog system for blog.victorgoico.com. Full control over design, content, and features. Deploy on GitHub Pages; blog lives in this dedicated repo (one CNAME per repo; portfolio is a separate repo).

## Core Requirements

- **Content:** Markdown with YAML frontmatter (title, date, tags, description).
- **Build:** Custom Python script converts Markdown → HTML; generates RSS feed and sitemap.
- **Design:** Clean, minimal, readable; design system via Sass variables; reference in `designs/`.
- **SEO:** Meta tags, Open Graph, Twitter Cards, canonical URLs, JSON-LD, sitemap, robots.txt.
- **Discovery:** Tags/categories; optional tag pages or client-side filtering on index.
- **Analytics:** Google Analytics 4.
- **Hosting:** GitHub Pages at blog.victorgoico.com (CNAME; DNS via SquareSpace).

## Goals

- Professional platform to share technical knowledge and build audience.
- Thought leadership and reach for job opportunities.
- Optimize for SEO and discoverability.
- Support cross-posting (Blog → Twitter → Medium → LinkedIn).
- Publish new posts in under 5 minutes.

## Scope (In Scope)

- Static site generation (no server runtime).
- Posts, index, tag filtering, RSS, sitemap.
- GA4, CNAME/DNS, README and usage docs.
- Optional back link from blog to portfolio (in this repo).

## Scope (Out of Scope for Initial PRs)

- Comments (utterances/giscus), reading time, related posts, share buttons.
- Client-side search, archive by date, newsletter.
- Dark mode, TOC, image optimization, print stylesheet.

## Source of Truth

- **PRD:** `PRD.md` — full task breakdown (PRs #1–#9), design specs, success metrics.
- **Memory Bank:** This folder — project context for AI and handoffs.
