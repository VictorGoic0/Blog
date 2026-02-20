# Blog (blog.victorgoico.com)

Custom markdown-based blog built with a Python script, Jinja2 templates, and Sass. Deployed via GitHub Pages at blog.victorgoico.com.

## Writing posts

### Markdown and HTML

Posts are written in Markdown. You can also use raw HTML inline — the Markdown parser passes it through untouched.

| What you want | Markdown | HTML equivalent |
|---|---|---|
| Heading | `## My Heading` → `<h2>` | `<h2>My Heading</h2>` |
| Bold | `**bold**` | `<strong>bold</strong>` |
| Image | `![alt](url)` | `<img src="url" alt="alt">` |
| Link | `[text](url)` | `<a href="url">text</a>` |

Both produce identical HTML output — `##` compiles to exactly `<h2>`, so semantic HTML and SEO are not affected by which you use.

**Gotcha:** if you open a block-level HTML tag (e.g. `<div>`, `<section>`), Markdown stops processing inside it. Inline HTML tags (e.g. `<img>`, `<strong>`, `<span>`) inside a Markdown paragraph work fine.

## Build and deploy

### Prerequisites

- Python 3
- Node.js and npm (for compiling Sass to CSS)

### Build the site

```bash
# 1. Compile Sass (design tokens and layout in scss/) to css/blog.css
npm install
npm run build:css

# 2. Python build: HTML from Markdown, copies css into output/
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Generate all posts and index
python build.py

# Build a single post (and refresh index)
python build.py posts/2026-02-20-why-is-bitcoin-king-part-one.md

# Remove output/ and rebuild from scratch
python build.py --clean
```

Generated files go into **`output/`**: `index.html`, `posts/<slug>.html`, `css/blog.css`. This folder is gitignored, so it may be **hidden in your editor's file explorer**; the files are still there. To confirm: `ls output/` in the terminal. We don't commit `output/`: the GitHub Actions workflow builds and deploys it on every push to `master`.

**Preview locally:** Serve the built site so CSS and links work, then open in your browser:

```bash
python -m http.server 8080 --directory output
```

Then open **http://localhost:8080**.

**Sass:** Edit `scss/_variables.scss` for design tokens and `scss/blog.scss` for layout and components. Run `npm run build:css` after changes; use `npm run watch:css` during development.

### Deployment (GitHub Actions)

Every push to `master` automatically builds and deploys the site. The workflow (`.github/workflows/deploy.yml`):

1. Compiles Sass → `css/blog.css`
2. Runs `python build.py` → generates `output/` (HTML, CSS, feed.xml, sitemap.xml, robots.txt, CNAME)
3. Deploys `output/` to GitHub Pages

You can also trigger a deploy manually from the **Actions** tab → **Deploy to GitHub Pages** → **Run workflow**.

### Google Analytics (GA4)

1. In GA4: **Admin** (gear) → select your **Property** → **Data streams** → click your **Web** stream.
2. Copy the **Measurement ID** (e.g. `G-XXXXXXXXXX`).
3. In `build.py`, set `GA4_MEASUREMENT_ID = "G-XXXXXXXXXX"`. Leave as `""` to disable.
4. Rebuild and deploy. Verify in GA4 under **Reports → Realtime**.
