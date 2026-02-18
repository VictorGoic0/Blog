# Product Context

## Why This Project Exists

- Need a professional blog to share technical knowledge and build an audience.
- Goal: thought leadership, visibility for job opportunities, full control over design and content.
- GitHub Pages allows one CNAME per repo, so the blog uses this dedicated repo; portfolio uses another.

## Problems It Solves

- **Ownership:** No dependency on Medium/Substack for hosting or branding.
- **SEO:** Full control over meta tags, structured data, sitemap, RSS.
- **Workflow:** Write in Markdown, run one build, push — content lives in git.
- **Discovery:** Tags and (optional) tag pages for filtering and navigation.

## How It Should Work

1. **Author:** Create `posts/YYYY-MM-DD-slug.md` with YAML frontmatter and Markdown body.
2. **Build:** Run `python build.py` → HTML in `output/`, plus `feed.xml`, `sitemap.xml`.
3. **Deploy:** Push to this repo; GitHub Pages serves from configured source (root or output).
4. **Reader:** Visits blog.victorgoico.com — index with post list and tag filtering; post pages with metadata, readable typography, code highlighting.
5. **Discovery:** RSS for subscribers; sitemap and meta tags for search and social sharing.

## User Experience Goals

- **Readability:** Clean, minimal layout; 680–720px max width; 18–21px body text; generous spacing.
- **Speed:** Static site; no client-side framework required for core experience.
- **Findability:** Tags, RSS, sitemap, and SEO from day one.
- **Cross-post:** Content can be republished to Twitter, Medium, LinkedIn after publishing.

## Success Criteria (from PRD)

- Blog live at blog.victorgoico.com.
- First post published with proper SEO.
- RSS feed valid; GA4 tracking; new post publishable in &lt; 5 minutes.
- Portfolio repo nav links to blog; SEO meta tags render correctly.
