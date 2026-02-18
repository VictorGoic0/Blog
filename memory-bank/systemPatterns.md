# System Patterns

## Architecture

- **Static site:** No server at runtime. Build produces HTML, CSS, XML (RSS, sitemap).
- **Single build script:** `build.py` owns Markdown discovery, frontmatter parsing, HTML generation, RSS, sitemap. Templates are Jinja2.
- **Styling:** Sass → CSS. Design tokens in `_variables.scss`; single entry `blog.scss` → `css/blog.css`. Variables drive colors, spacing, typography.

## Key Technical Decisions

- **Repo boundary:** Blog-only repo so GitHub Pages can use one CNAME (blog.victorgoico.com). Portfolio is a separate repo; PR #8 changes are in the portfolio repo.
- **Content format:** Markdown + YAML frontmatter (title, date, tags, description). No CMS.
- **Output:** Generated files in `output/` (gitignored). CNAME must be at repo root or copied into output so Pages serves the custom domain.
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
- **Design:** `designs/` is reference only; implementation follows PRD design specs via Sass variables.

## Design Specs (Implementation)

- Background: #ffffff or #fafafa. Text: #222222. Links: #0066cc, underlined on hover.
- Font: system fonts or Inter/Roboto. Max width: 680–720px. Line height: 1.6–1.8. Generous margins/padding.
- Code blocks: syntax highlighting. Mobile responsive.
