# System Patterns

## Architecture

- **Static site:** No server at runtime. Build produces HTML, CSS, XML (RSS, sitemap).
- **Single build script:** `build.py` owns Markdown discovery, frontmatter parsing, HTML generation, RSS, sitemap. Templates are Jinja2.
- **Styling:** Sass → CSS. Design tokens in `_variables.scss`; single entry `blog.scss` → `css/blog.css`. Variables drive colors, spacing, typography.

## Key Technical Decisions

- **Repo boundary:** Blog-only repo so GitHub Pages can use one CNAME (blog.victorgoico.com). Portfolio is a separate repo.
- **Content format:** Markdown + YAML frontmatter (title, date, tags, description). No CMS.
- **Output:** Generated files in `output/` (gitignored). Workflow copies CNAME into output/ before deploy (`cp CNAME output/`).
- **Tags:** Extracted in build; tag index in build script. Filtering on index (client-side or tag pages) per PR #5.

## Component Relationships

```
posts/*.md  →  build.py  →  templates (base, post, index)  →  output/*.html
                build.py  →  feed.xml, sitemap.xml, robots.txt
scss/*.scss →  (Sass)    →  css/blog.css  →  linked from base.html
CNAME       →  (in repo root or output)  →  GitHub Pages custom domain
```

- **build.py:** Reads `posts/`, uses `templates/`, writes `output/`. Emits RSS and sitemap.
- **templates:** base.html (layout, head, nav, footer); post.html (article); index.html (post list, tag filter).
- **Design:** `designs/` is reference only; implementation follows design specs via Sass variables in `scss/_variables.scss`.
- **Deployment:** GitHub Actions (.github/workflows/deploy.yml) triggers on push to master. Builds Sass + Python, copies CNAME, deploys output/ to Pages via actions/deploy-pages.

## Design Specs (Implementation)

- Background: #fafafa. Text: #222222. Links: #0066cc, underlined on hover.
- Font: Inter + system stack. Max width: 700px. Line height: 1.7. Base font: 18px.
- Code blocks: monospace, #f5f5f5 background with border. Mobile responsive.
- Header: `.site-header-inner` flex row — logo (`GOICOLOG_`) left, nav right. Color inherited from `.site-header-inner` (black). No border-bottom.
- Nav links: `Articles` (links to `/`), `About` (links to `victorgoico.com/#about`, new tab). All black.
- Post meta order: `date · By [Author] · N min read` — appears above `<h1>`. Author links to `victorgoico.com`.
- Tag filter UI: commented out in templates pending redesign Phase 2. Build still generates tag data.
