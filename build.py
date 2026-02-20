#!/usr/bin/env python3
"""
Build script: discover Markdown posts, parse frontmatter, render HTML via Jinja2, write to output/.
Usage:
  python build.py                    # build all
  python build.py posts/2026-01-15-one-post.md   # build one post (and index)
  python build.py --clean           # remove output/ then build all
"""

import argparse
import json
import re
import shutil
from pathlib import Path
from datetime import datetime

import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape


PROJECT_ROOT = Path(__file__).resolve().parent
POSTS_DIR = PROJECT_ROOT / "posts"
TEMPLATES_DIR = PROJECT_ROOT / "templates"
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_POSTS_DIR = OUTPUT_DIR / "posts"

SITE_URL = "https://blog.victorgoico.com"
# GA4 Measurement ID (G-XXXXXXXXXX). Leave empty to disable analytics.
GA4_MEASUREMENT_ID = "G-MQ8Y3G6RKR"


def parse_args():
    parser = argparse.ArgumentParser(description="Build blog from Markdown posts.")
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove output directory before building",
    )
    parser.add_argument(
        "post_path",
        nargs="?",
        type=Path,
        default=None,
        help="Optional path to a single post file (e.g. posts/2026-01-15-slug.md)",
    )
    return parser.parse_args()


def discover_posts(single_path: Path | None) -> list[Path]:
    """Return list of post paths (posts/*.md), sorted by date descending. If single_path given, only that file (if valid)."""
    if single_path is not None:
        path = single_path if single_path.is_absolute() else PROJECT_ROOT / single_path
        if path.exists() and path.suffix.lower() == ".md" and "posts" in path.parts:
            return [path]
        return []

    if not POSTS_DIR.exists():
        return []
    paths = list(POSTS_DIR.glob("*.md"))
    # Sort by filename (YYYY-MM-DD-slug) descending
    paths.sort(key=lambda p: p.name, reverse=True)
    return paths


def slug_from_path(path: Path) -> str:
    """e.g. 2026-01-15-my-post.md -> my-post"""
    stem = path.stem
    match = re.match(r"\d{4}-\d{2}-\d{2}-(.+)", stem)
    return match.group(1) if match else stem


def word_count(text: str) -> int:
    """Approximate word count for read time (strip markdown, count words)."""
    if not text or not text.strip():
        return 0
    # Remove code blocks and inline code to avoid inflating count
    cleaned = re.sub(r"```[\s\S]*?```", " ", text)
    cleaned = re.sub(r"`[^`]+`", " ", cleaned)
    return len(cleaned.split())


def excerpt_from_content(content: str, max_length: int = 160) -> str:
    """Plain-text excerpt: first paragraph or first max_length chars, stripped of markdown."""
    if not content or not content.strip():
        return ""
    # First paragraph (up to double newline)
    para = content.split("\n\n")[0].strip()
    para = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", para)  # links -> text
    para = re.sub(r"[*_`#]+", "", para).strip()
    if len(para) <= max_length:
        return para
    return para[: max_length - 1].rsplit(" ", 1)[0] + "…" if " " in para[:max_length] else para[: max_length - 1] + "…"


def extract_post(path: Path, md: markdown.Markdown) -> dict:
    """Load post file, parse frontmatter, convert body to HTML. Return dict for template."""
    raw = path.read_text(encoding="utf-8")
    post = frontmatter.loads(raw)
    title = post.get("title") or slug_from_path(path).replace("-", " ").title()
    date_val = post.get("date")
    if hasattr(date_val, "strftime"):
        date_obj = date_val
    elif isinstance(date_val, str):
        try:
            date_obj = datetime.fromisoformat(date_val.replace("Z", "+00:00")).replace(tzinfo=None)
        except ValueError:
            date_obj = datetime.now()
    else:
        # Try filename YYYY-MM-DD
        match = re.match(r"(\d{4}-\d{2}-\d{2})", path.stem)
        date_obj = datetime.strptime(match.group(1), "%Y-%m-%d") if match else datetime.now()

    tags = post.get("tags") or []
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",")]
    description = post.get("description") or ""
    content = post.content or ""
    excerpt = description or excerpt_from_content(content)

    html_content = md.convert(content)
    words = word_count(content)
    read_time_min = max(1, (words + 199) // 200)  # ~200 wpm, at least 1 min

    slug = slug_from_path(path)
    return {
        "title": title,
        "date_iso": date_obj.strftime("%Y-%m-%d"),
        "date_display": date_obj.strftime("%b %d, %Y"),
        "tags": list(tags),
        "description": description,
        "excerpt": excerpt,
        "html_content": html_content,
        "slug": slug,
        "url": f"posts/{slug}.html",
        "read_time_min": read_time_min,
    }


def build(single_path: Path | None = None) -> None:
    """Discover posts, parse, render, write to output/."""
    md = markdown.Markdown(extensions=["fenced_code", "tables"])
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(("html",)),
    )
    env.globals["current_year"] = datetime.now().year
    env.globals["site_url"] = SITE_URL
    env.globals["ga4_measurement_id"] = GA4_MEASUREMENT_ID

    post_paths = discover_posts(single_path)
    if not post_paths:
        print("No posts found.")
        return

    posts_data = []
    for path in post_paths:
        try:
            data = extract_post(path, md)
            posts_data.append(data)
        except Exception as e:
            print(f"Warning: skip {path}: {e}")
            continue

    # Newest first for index
    posts_data.sort(key=lambda p: p["date_iso"], reverse=True)

    # JSON-LD for each post (safe for script tag)
    for p in posts_data:
        ld = {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": p["title"],
            "datePublished": p["date_iso"],
            "url": f"{SITE_URL}/{p['url']}",
            "author": {"@type": "Person", "name": "Victor Goico"},
        }
        p["json_ld"] = json.dumps(ld, ensure_ascii=False)

    OUTPUT_POSTS_DIR.mkdir(parents=True, exist_ok=True)

    base_template = env.get_template("base.html")
    post_template = env.get_template("post.html")
    index_template = env.get_template("index.html")

    for post in posts_data:
        html = post_template.render(post=post)
        out_path = OUTPUT_DIR / post["url"]
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html, encoding="utf-8")
        print(f"  {post['url']}")

    all_tags = sorted(set(t for p in posts_data for t in p["tags"]))
    # Tag index: map each tag to list of posts (for "All tags" counts and tag pages)
    tag_index: dict[str, list[dict]] = {}
    for tag in all_tags:
        tag_index[tag] = [p for p in posts_data if tag in p["tags"]]
    index_html = index_template.render(
        posts=posts_data, all_tags=all_tags, tag_index=tag_index
    )
    (OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print("  index.html")

    # Copy compiled CSS so deployed site (output/ as Pages source) has styles
    css_src = PROJECT_ROOT / "css" / "blog.css"
    if css_src.exists():
        css_dst = OUTPUT_DIR / "css"
        css_dst.mkdir(parents=True, exist_ok=True)
        shutil.copy2(css_src, css_dst / "blog.css")
        print("  css/blog.css")

    # RSS 2.0 feed
    def rfc2822(date_iso: str) -> str:
        d = datetime.strptime(date_iso, "%Y-%m-%d")
        return d.strftime("%a, %d %b %Y 12:00:00 +0000")

    feed_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">',
        "  <channel>",
        "    <title>blog.victorgoico.com</title>",
        f"    <link>{SITE_URL}/</link>",
        "    <description>Victor Goico's blog — technical writing and development.</description>",
        f'    <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>',
    ]
    for p in posts_data:
        link = f"{SITE_URL}/{p['url']}"
        desc = (p.get("description") or p.get("excerpt") or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
        title = p["title"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
        feed_lines.append("    <item>")
        feed_lines.append(f"      <title>{title}</title>")
        feed_lines.append(f"      <link>{link}</link>")
        feed_lines.append(f"      <pubDate>{rfc2822(p['date_iso'])}</pubDate>")
        feed_lines.append(f"      <guid isPermaLink=\"true\">{link}</guid>")
        feed_lines.append(f"      <description>{desc}</description>")
        feed_lines.append("    </item>")
    feed_lines.append("  </channel>")
    feed_lines.append("</rss>")
    (OUTPUT_DIR / "feed.xml").write_text("\n".join(feed_lines), encoding="utf-8")
    print("  feed.xml")

    # Sitemap
    sitemap_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        f"  <url><loc>{SITE_URL}/</loc><lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod><changefreq>daily</changefreq><priority>1.0</priority></url>",
    ]
    for p in posts_data:
        sitemap_lines.append(
            f"  <url><loc>{SITE_URL}/{p['url']}</loc><lastmod>{p['date_iso']}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>"
        )
    sitemap_lines.append("</urlset>")
    (OUTPUT_DIR / "sitemap.xml").write_text("\n".join(sitemap_lines), encoding="utf-8")
    print("  sitemap.xml")

    # robots.txt
    (OUTPUT_DIR / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: " + SITE_URL + "/sitemap.xml\n",
        encoding="utf-8",
    )
    print("  robots.txt")

    print(f"Done. {len(posts_data)} post(s) built.")


def main():
    args = parse_args()
    if args.clean and OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
        print("Cleaned output/")
    build(args.post_path)


if __name__ == "__main__":
    main()
