# Product Requirements Document: Custom Blog System

## Overview

Build a custom markdown-based blog system with automated HTML generation, SEO optimization, RSS feed, analytics, and tags/categories. Deploy on subdomain blog.victorgoico.com with clean, minimal design. This repo is dedicated to the blog only (GitHub Pages allows one CNAME per repo, so the blog lives in a separate repo from the portfolio). Design reference materials have been brought in (in `designs/`) to use as a guideline for styles.

## Goals

- Create a professional blogging platform to share technical knowledge and build audience
- Establish thought leadership and increase reach for job opportunities
- Maintain full control over design, features, and content
- Optimize for SEO and discoverability
- Support cross-posting workflow (Blog → Twitter → Medium → LinkedIn)

## Technical Architecture

### Stack

- **Static Site Generation:** Custom Python build script
- **Content Format:** Markdown with YAML frontmatter
- **Templating:** Jinja2
- **Styling:** Sass (compiled to CSS). Use Sass variables for a consistent design system (spacing, typography, colors). Install Sass tooling as needed (e.g. `sass` npm package or build-step dependency).
- **Hosting:** GitHub Pages
- **Domain:** blog.victorgoico.com (subdomain on SquareSpace)
- **Analytics:** Google Analytics 4

### Directory Structure

Repo root is the blog project

```
├── build.py              # Markdown → HTML converter
├── requirements.txt      # Python dependencies
├── posts/                # Source markdown files
│   └── YYYY-MM-DD-slug.md
├── templates/            # HTML templates
│   ├── base.html        # Shared layout
│   ├── post.html        # Single post template
│   └── index.html       # Blog index template
├── scss/                 # Sass source (compile to css/)
│   ├── _variables.scss  # Design tokens: colors, spacing, typography
│   └── blog.scss        # Main entry (imports variables, components)
├── css/
│   └── blog.css         # Compiled output from scss/ (gitignore or commit)
├── output/              # Generated files (gitignored)
│   ├── posts/
│   ├── index.html
│   ├── feed.xml
│   └── sitemap.xml
├── .gitignore
├── CNAME                # blog.victorgoico.com (repo root)
└── README.md
```

### Build Process Flow

```
Markdown Posts → build.py → HTML + RSS + Sitemap → Git Push → GitHub Pages
```

---

## Pull Requests & Tasks

### PR #1: DNS Configuration & Subdomain Setup

**Priority:** Critical - Must complete before other PRs
**Estimated Time:** 30 minutes

#### Tasks

- [x] 1.1. Log into SquareSpace DNS management for victorgoico.com
- [x] 1.2. Add CNAME record: `blog` pointing to `victorgoic0.github.io` (or your GitHub Pages domain)
- [x] 1.3. Verify DNS propagation (use dig or nslookup)
- [x] 1.4. Create `CNAME` file at repo root with content: `blog.victorgoico.com`
- [x] 1.5. Test subdomain resolves correctly
- [x] 1.6. Document DNS setup in README.md

**SquareSpace DNS Steps:**

1. Go to SquareSpace DNS Management for victorgoico.com
2. In **Custom Records**, add a new record:
   - **Type:** CNAME
   - **Host:** `blog` (subdomain only)
   - **Alias Data:** `victorgoic0.github.io` (or your GitHub Pages hostname)
   - **TTL:** 30 minutes (SquareSpace’s minimum)
3. Save and wait for propagation (often 5–15 minutes; can be longer)

---

### PR #2: Project Structure & Build Script Core

**Priority:** High
**Estimated Time:** 2-3 hours

#### Tasks

- [x] 2.1. Set up directory structure at repo root (posts/, templates/, scss/, css/, output/)
- [x] 2.2. Create `.gitignore` to exclude output/ directory
- [x] 2.3. Create `requirements.txt` with dependencies (markdown, python-frontmatter, jinja2)
- [x] 2.4. Build `build.py` script skeleton with argument parsing
- [x] 2.5. Implement markdown file discovery and parsing
- [x] 2.6. Add frontmatter extraction (title, date, tags, description)
- [x] 2.7. Implement basic HTML generation from markdown
- [x] 2.8. Add file writing to output/ directory
- [x] 2.9. Test with sample markdown post
- [x] 2.10. Add README.md with usage instructions

**Dependencies:**

```txt
markdown>=3.5
python-frontmatter>=1.1.0
Jinja2>=3.1.2
```

---

### PR #3: HTML Templates & Clean Blog Design

**Priority:** High
**Estimated Time:** 3-4 hours

**Design reference:** Use the designs in `designs/` as the guideline for styles, layout, and visual treatment when implementing templates and Sass stylesheets.

**Styling approach:** Use Sass (not plain CSS) so we can maintain a consistent design system via variables for spacing, typography, and colors. Install whatever packages or tooling are needed for Sass compilation (e.g. `sass` npm package, or a Python Sass compiler); that is acceptable and should be done in this PR.

#### Tasks

- [x] 3.1. Create `templates/base.html` with semantic HTML structure
- [x] 3.2. Add head section with meta tags placeholders
- [x] 3.3. Create navigation header (simple: Home, All Posts)
- [x] 3.4. Add footer with copyright and social links
- [x] 3.5. Create `templates/post.html` extending base template
- [x] 3.6. Add article structure with proper semantic tags
- [x] 3.7. Include metadata display (date, tags, read time)
- [x] 3.8. Create `templates/index.html` for blog homepage
- [x] 3.9. Add post list layout with excerpts
- [x] 3.10. Implement tag filtering UI
- [x] 3.11. Set up Sass: install Sass compiler/package and add `scss/` with `_variables.scss` (design tokens) and `blog.scss` that compiles to `css/blog.css`
- [x] 3.12. Define Sass variables for colors (background, text, links), spacing, and typography (font stack, sizes, line-height) per Design Specs
- [x] 3.13. Implement minimal, clean styling using those variables; white/light background, dark text (#222)
- [x] 3.14. Add responsive typography (18-21px body text) via variables
- [x] 3.15. Style code blocks with syntax highlighting
- [x] 3.16. Ensure mobile responsiveness
- [x] 3.17. Test templates render correctly with build script

**Design Specs (implement via Sass variables):**

- Background: #ffffff or #fafafa
- Text: #222222
- Links: #0066cc (blue, underlined on hover)
- Font: System fonts or Inter/Roboto from Google Fonts
- Max width: 680-720px for readability
- Line height: 1.6-1.8
- Spacing: Generous margins and padding

---

### PR #4: SEO, RSS Feed, and Sitemap Generation

**Priority:** High
**Estimated Time:** 2-3 hours

#### Tasks

- [x] 4.1. Add SEO meta tags to base.html (title, description, keywords)
- [x] 4.2. Implement Open Graph tags for social sharing
- [x] 4.3. Add Twitter Card meta tags
- [x] 4.4. Include canonical URL for each post
- [x] 4.5. Add JSON-LD structured data for articles
- [x] 4.6. Implement RSS feed generation in build.py
- [x] 4.7. Generate feed.xml with RSS 2.0 format
- [x] 4.8. Include post title, description, link, pubDate
- [x] 4.9. Add RSS link to base.html head
- [x] 4.10. Implement sitemap.xml generation
- [x] 4.11. Include all post URLs with lastmod dates
- [x] 4.12. Add priority and changefreq values
- [x] 4.13. Create robots.txt for SEO crawling
- [x] 4.14. Test RSS feed validates (use W3C Feed Validator)
- [x] 4.15. Test sitemap validates

**Structured Data Example:**

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Post Title",
  "datePublished": "2026-01-15",
  "author": {
    "@type": "Person",
    "name": "Victor Goico"
  }
}
```

---

### PR #5: Tags/Categories System

**Priority:** Medium
**Estimated Time:** 2 hours

#### Tasks

- [x] 5.1. Extract tags from post frontmatter in build.py
- [x] 5.2. Build tag index (map tags to posts)
- [x] 5.3. Generate tag pages (optional) or use client-side filtering
- [x] 5.4. Add tag display to post template
- [x] 5.5. Style tags as clickable badges
- [x] 5.6. Implement tag filtering on index page
- [x] 5.7. Add "All tags" view to index page
- [x] 5.8. Test tag filtering works correctly

---

### PR #6: Google Analytics Integration

**Priority:** Medium
**Estimated Time:** 30 minutes

#### Tasks

- [x] 6.1. Create Google Analytics 4 account
- [x] 6.2. Set up new property for blog.victorgoico.com
- [x] 6.3. Get tracking ID (G-XXXXXXXXXX)
- [x] 6.4. Add GA4 tracking code to base.html
- [x] 6.5. Test analytics tracking in real-time view
- [x] 6.6. Set up basic goals/events (optional)
- [x] 6.7. Document analytics setup in README.md

**GA4 Script:**

```html
<!-- Google Analytics -->
<script
  async
  src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"
></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag() {
    dataLayer.push(arguments);
  }
  gtag("js", new Date());
  gtag("config", "G-XXXXXXXXXX");
</script>
```

---

### PR #7: GitHub Pages Deployment Setup

**Priority:** High
**Estimated Time:** 1 hour

**Context:** This repo is the blog-only repo (separate from the portfolio repo) so GitHub Pages can use a single CNAME for blog.victorgoico.com.

#### Tasks

- [ ] 7.1. Push blog code to this repo
- [ ] 7.2. Enable GitHub Pages in repo settings
- [ ] 7.3. Set source to main branch (root or output folder, per build setup)
- [ ] 7.4. Ensure CNAME is at repo root or in deployed output so GitHub Pages serves the custom domain
- [ ] 7.5. Test blog.victorgoico.com loads correctly
- [ ] 7.6. Set up automatic deployment workflow (optional)
- [ ] 7.7. Document deployment process in README.md

---

### PR #9: Create First Blog Post & Documentation

**Priority:** Medium
**Estimated Time:** 1-2 hours (excluding writing time)

#### Tasks

- [ ] 9.1. Write first blog post in markdown
- [ ] 9.2. Add proper frontmatter (title, date, tags, description)
- [ ] 9.3. Test build.py generates HTML correctly
- [ ] 9.4. Review rendered post for formatting issues
- [ ] 9.5. Check SEO meta tags render correctly
- [ ] 9.6. Verify RSS feed includes new post
- [ ] 9.7. Update sitemap includes new post URL
- [ ] 9.8. Create usage documentation in README.md
- [ ] 9.9. Document content creation workflow
- [ ] 9.10. Add markdown syntax guide for reference
- [ ] 9.11. Deploy and test live

**Sample Post Template:**

```markdown
---
title: "My First Blog Post: Why I'm Building in Public"
date: 2026-01-15
tags: [Career, Development, AI]
description: "Lorem ipsum lorem ipsum"
---

Your compelling intro here...

## Why This Blog Exists

Your content...

## What You Can Expect

More content...
```

---

## Deployment Workflow (Final State)

### Writing a New Post

1. Create `posts/YYYY-MM-DD-slug.md`
2. Add frontmatter and content
3. Run `python build.py`
4. Review output in `output/` directory
5. Git commit and push
6. GitHub Pages auto-deploys

### Build Script Usage

```bash
# Generate all posts
python build.py

# Generate specific post (optional feature)
python build.py posts/2026-01-15-my-post.md

# Clean output directory
python build.py --clean
```

---

## Future Enhancements (Not in Initial PRs)

### Phase 2 - Engagement

- [ ] Add comments system (utterances or giscus)
- [ ] Implement reading time estimation
- [ ] Add "Related posts" section
- [ ] Social share buttons

### Phase 3 - Discovery

- [ ] Client-side search with lunr.js
- [ ] Archive page by date
- [ ] Popular posts widget
- [ ] Newsletter signup integration

### Phase 4 - Experience

- [ ] Dark mode toggle
- [ ] Table of contents for long posts
- [ ] Image optimization and lazy loading
- [ ] Print stylesheet

---

## Success Metrics

- Blog deployed and accessible at blog.victorgoico.com
- First post published with proper SEO
- RSS feed functional and validated
- Google Analytics tracking visitors
- Can write and publish new posts in < 5 minutes
- All SEO meta tags render properly

---

## Notes

- Keep design simple and focused on readability
- Prioritize content creation workflow efficiency
- SEO optimization is critical from day one
- Monitor analytics to understand what content resonates
- Plan for cross-posting to Medium and LinkedIn after publishing
