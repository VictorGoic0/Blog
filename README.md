# Blog (blog.victorgoico.com)

Custom markdown-based blog built with a Python script, Jinja2 templates, and Sass. Deployed via GitHub Pages. This repo is dedicated to the blog only (one CNAME per GitHub Pages repo; portfolio uses a separate repo).

## DNS setup

The blog is served at the `blog` subdomain (blog.victorgoico.com). To point it at GitHub Pages:

1. In **SquareSpace DNS** for the root domain (victorgoico.com), open **Custom Records** and add:
   - **Type:** CNAME  
   - **Host:** `blog`  
   - **Alias Data:** `victorgoic0.github.io` (or this repo’s GitHub Pages hostname)  
   - **TTL:** 30 minutes (or minimum available)

2. The repo contains `CNAME` at the root with the custom domain. That file must be present in the deployed output root so GitHub Pages can serve the site on the subdomain.

3. After saving, allow time for DNS propagation (often 5–15 minutes; sometimes longer). Verify with:
   - `dig blog.victorgoico.com CNAME`
   - or `nslookup blog.victorgoico.com`

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
python build.py posts/2026-02-18-hello-world.md

# Remove output/ and rebuild from scratch
python build.py --clean
```

Generated files go into **`output/`**: `index.html`, `posts/<slug>.html`, `css/blog.css`. This folder is gitignored, so it may be **hidden in your editor’s file explorer**; the files are still there. To confirm: `ls output/` in the terminal. We don’t commit `output/`: deployment (e.g. GitHub Actions in PR #7) will run the build and deploy that folder.

**Preview locally:** Serve the built site so CSS and links work, then open in your browser:

```bash
python -m http.server 8080 --directory output
```

Then open **http://localhost:8080**. The build script copies the compiled stylesheet into `output/css/` so the site works when GitHub Pages is set to serve from `output/`. Ensure `CNAME` is present in the deployed root.

**Sass:** Edit `scss/_variables.scss` for design tokens and `scss/blog.scss` for layout and components. Run `npm run build:css` after changes; use `npm run watch:css` during development.
