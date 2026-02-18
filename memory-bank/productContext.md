# Product Context

## Why This Project Exists

- Need a dedicated blog to publish technical content and build an audience without depending on Medium or LinkedIn for hosting.
- Portfolio (victorgoico.com) stays focused on projects; the blog is a separate, content-first experience at blog.victorgoico.com.
- Full ownership of content, design, and analytics; no platform lock-in.

## Problems It Solves

- Where to publish long-form technical posts with proper SEO and RSS.
- How to keep a consistent, minimal design and design system (Sass variables for spacing, typography, colors).
- How to ship quickly: static site, Markdown + YAML frontmatter, single build script, GitHub Pages.

## How It Should Work

1. **Authoring:** Write posts as `posts/YYYY-MM-DD-slug.md` with frontmatter (title, date, tags, description). Markdown for body.
2. **Build:** Run `python build.py` to generate HTML (Jinja2), RSS, sitemap; Sass compiles to `css/blog.css`.
3. **Deploy:** Push to GitHub; Pages serves from output. Subdomain blog.victorgoico.com via CNAME.
4. **Readers:** Clean, readable blog (white background, soft black text, gray for metadata and lines). Nav: Home, All Posts; optional tag filtering. Portfolio links to blog and back.

## User Experience Goals

- **Readability first:** White background, soft black text (no pure #000), generous line height and max width (680–720px).
- **Design consistency:** Follow reference designs in `designs/`; implement via Sass variables (colors, spacing, typography).
- **Discoverability:** SEO from day one; RSS for subscribers; tags for filtering.
- **Low friction:** New post in &lt; 5 minutes: create file, add frontmatter, run build, push.
