# System Patterns

## Architecture

- **Static site:** No server-side runtime. Build produces HTML, CSS, RSS, sitemap; GitHub Pages serves files.
- **Single build script:** `build.py` discovers Markdown in `posts/`, parses frontmatter, renders Jinja2 templates, writes to `output/`. Optional: run Sass as part of build or via separate step (e.g. `sass scss:css`).
- **Templates:** `base.html` (layout, nav, footer), `post.html` (single post), `index.html` (blog homepage with post list and tag filtering). All reference compiled `css/blog.css`.

## Key Technical Decisions

- **Sass over plain CSS:** Design system via variables (colors, spacing, typography). Install Sass tooling as needed (e.g. `sass` npm package) in PR #3.
- **Design reference:** `designs/` (e.g. page-design.png, list-design.png) is the source of truth for layout and visual treatment when implementing templates and Sass.
- **Color system (design specs):**
  - Background: #ffffff (white).
  - Primary text (headings, body, nav): soft black (e.g. #222222 or #1a1a1a), not pure black.
  - Secondary text (date, “By”, metadata): gray.
  - Lines/borders (e.g. nav separator): light gray.
  - Links: primary (soft black) with underline, or distinct link color; align with design reference.
- **Content format:** Markdown + YAML frontmatter; Python `markdown` and `python-frontmatter` for parsing; Jinja2 for HTML.

## Component Relationships

- `build.py` → reads `posts/*.md`, `templates/*.html`, (optionally triggers Sass) → writes `output/` (HTML, feed.xml, sitemap.xml).
- Templates extend `base.html`; base includes `blog.css` and meta/RSS links.
- Tag data comes from frontmatter; build script builds tag index; index template uses it for filtering UI.

## Deployment Flow

Markdown → build.py → HTML + RSS + sitemap (+ Sass → css) → git push → GitHub Pages. CNAME in repo points blog.victorgoico.com to Pages.
