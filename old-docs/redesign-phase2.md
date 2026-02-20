# Redesign Phase 2 — Articles List Page

## Overview

Rebuild the articles list page to match `designs/list-design.png`: wider layout, hero section with headline/subtitle, and article cards with a two-column meta/body layout.

---

## Design analysis

```
┌──────────────────────────────────────────────────┐
│  GOICOLOG_                    Articles   About    │  ← unchanged header
├──────────────────────────────────────────────────┤  ← border-top (will overlap header border)
│                                                  │
│  [Large headline — placeholder text]             │
│  [Subtitle — placeholder text]                   │
│                                                  │
├──────────────────────────────────────────────────┤
│ YY.MM.DD  │  Title                               │
│ Tag[0]    │  Excerpt / description               │
│           │  [Tag badge] [Tag badge]             │
│           │  [ Read Article → ]                  │
│ By Victor │                                      │
├──────────────────────────────────────────────────┤
│  ... next article card ...                       │
```

---

## Key decisions

- **Left column middle slot**: `post.tags[0]` as plain muted text — the "primary category." No new frontmatter field needed. Convention: always put the primary category first in a post's tags list.
- **Date format**: `YY.MM.DD` (e.g. `26.02.20`) — add `date_short` field in `build.py` via `strftime("%y.%m.%d")`.
- **Wider layout**: The articles page needs ~960px. Add a `{% block main_class %}` extension point to `base.html` so `index.html` can inject `main-content--wide` without touching any other page.
- **Tags on cards**: Non-clickable plain badges (no `<a>`, just `<span>`).
- **"Read Article →" button**: Outlined pill button, no fill, just a border and arrow.
- **Tag filter**: Stays commented out. Will live in the hero section when re-enabled in a future phase.

---

## Tasks

### Task 1 — `build.py`: Add `date_short` field ✓

Add one line alongside the existing `date_display`:

```python
"date_short": date_obj.strftime("%y.%m.%d"),
```

**Status:** complete

---

### Task 2 — `templates/base.html`: Add `main_class` extension block ✓

Change the `<main>` tag to accept an optional extra class from child templates:

```html
<main class="main-content {% block main_class %}{% endblock %}">
```

**Status:** complete

---

### Task 3 — `scss/_variables.scss`: Add wide max-width token ✓

```scss
$content-max-width-wide: 960px;
```

**Status:** complete

---

### Task 4 — `scss/blog.scss`: New article list styles ✓

New rules to add:

- `.main-content--wide` — overrides `max-width` to `$content-max-width-wide`
- `.articles-hero` — full-width bordered box (`border-top`), padding, contains headline + subtitle
- `.articles-hero-headline` — large bold display text (~2.5rem)
- `.articles-hero-subtitle` — muted smaller text below headline
- `.article-card` — flex row, `border: 1px solid $color-border`, bottom-only or full border between cards
- `.article-card-meta` — narrow left column (~180px), flex column, `justify-content: space-between` so author pins to bottom
- `.article-card-meta-date` — `YY.MM.DD`, bold, dark
- `.article-card-meta-category` — `tags[0]`, muted, small
- `.article-card-meta-author` — "By Victor M. Goico", small, muted, pushed to bottom via `margin-top: auto`
- `.article-card-body` — flex 1, right column, contains title/excerpt/tags/button
- `.article-card-title` — bold, larger (~1.3rem)
- `.article-card-excerpt` — muted, small
- `.article-card-tags` — flex row of non-clickable `<span>` badges
- `.read-article-btn` — outlined pill: `border: 1px solid $color-text`, `border-radius: 999px`, no background, arrow `→`

**Status:** complete

---

### Task 5 — `templates/index.html`: Rebuild with hero + article cards ✓

Replace the current content block entirely with a hero section and article card list. Tag filter blocks remain commented out with a note that they will live in the hero section when re-enabled.

**Status:** complete
