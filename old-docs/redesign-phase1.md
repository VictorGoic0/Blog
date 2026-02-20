# Page Design Phase 1 Implementation

## Overview

Implement `designs/page-design.png` one-to-one: logo + right-aligned nav in the header, post meta above the title with author attribution, and tag filter UI commented out.

---

## Design deltas vs. current state

- **Header**: currently nav-only on the left. Design has logo left + nav items right.
- **Post meta**: currently `title → meta (date · read time · tags)`. Design has `meta (date · By Author) → title`. Read time stays; tags removed from view.
- **Tag filter / all-tags section**: present in `index.html`, absent from the design — commented out.
- **Header border-bottom**: design has no visible divider; currently has `border-bottom`.

---

## Tasks

### Task 1 — `scss/blog.scss`: Header layout + logo styles ✓

- Remove `border-bottom` from `.site-header`.
- Add `.site-header-inner`: `display: flex; align-items: center; justify-content: space-between;`
- Add `.site-logo`: `font-weight: 700`, `color: $color-text`, font size matched to nav (~`0.9rem`), no underline on hover.
- `.site-nav` needs no structural change — it becomes naturally right-aligned via the parent's `space-between`.

**Status:** complete

---

### Task 2 — `templates/base.html`: Logo + nav restructure ✓

Replace the `<header>` block with a two-column flex layout:

```html
<header class="site-header">
  <div class="site-header-inner">
    <a href="/" class="site-logo">GOICOLOG_</a>
    <nav aria-label="Main">
      <ul class="site-nav">
        <li><a href="/">Articles</a></li>
        <li>
          <a href="https://victorgoico.com" rel="noopener noreferrer" target="_blank">About</a>
        </li>
      </ul>
    </nav>
  </div>
</header>
```

**Status:** complete

---

### Task 3 — `templates/post.html`: Meta above title + author attribution ✓

- Move `post-meta` **above** `post-title` to match the design layout.
- Update meta content to: `date · By Victor M. Goico · N min read`
- Author name links to `https://victorgoico.com`.
- Comment out tag display with `{# ... #}` (re-enable in phase 2).

```html
<header class="post-header">
  <div class="post-meta">
    <time datetime="{{ post.date_iso }}">{{ post.date_display }}</time>
    <span class="meta-sep">·</span>
    By <a href="https://victorgoico.com" rel="noopener noreferrer" target="_blank" class="author-link">Victor M. Goico</a>
    <span class="meta-sep">·</span>
    {{ post.read_time_min }} min read
    {# tags commented out — re-enable with tag filter in phase 2 #}
  </div>
  <h1 class="post-title">{{ post.title }}</h1>
  ...
</header>
```

**Status:** complete

---

### Task 4 — `templates/index.html`: Comment out tag filter UI ✓

Comment out with `{# #}`:

- The entire `{% if all_tags %}` tag-filter + all-tags section.
- Tags display inside each `.post-list-item`.
- The inline `<script>` tag filter JS.

The post list (`<ul class="post-list">`), title, excerpt, date, and read-time rows remain untouched.

**Status:** complete
