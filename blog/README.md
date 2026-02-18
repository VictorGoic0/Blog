# Blog (blog.victorgoico.com)

Custom markdown-based blog built with a Python script, Jinja2 templates, and Sass. Deployed via GitHub Pages.

## DNS setup

The blog is served at the `blog` subdomain (blog.victorgoico.com). To point it at GitHub Pages:

1. In **SquareSpace DNS** for the root domain (victorgoico.com), open **Custom Records** and add:
   - **Type:** CNAME  
   - **Host:** `blog`  
   - **Alias Data:** `victorgoic0.github.io`  
   - **TTL:** 30 minutes (or minimum available)

2. The repo contains `blog/CNAME` with the custom domain. That file must be present in the deployed output root so GitHub Pages can serve the site on the subdomain.

3. After saving, allow time for DNS propagation (often 5–15 minutes; sometimes longer). Verify with:
   - `dig blog.victorgoico.com CNAME`
   - or `nslookup blog.victorgoico.com`

## Build and deploy

(To be added with PR #2 and later: how to run the build script, Sass compile, and deploy to GitHub Pages.)
