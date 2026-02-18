# Active Context

## Current Focus

- **Planning complete:** PRD (PRD.md) defines the custom blog system, 9 PRs, design approach, and color/styling specs.
- **Design reference:** Designs in `designs/` (e.g. page-design.png, list-design.png) are the guideline for styles; PR #3 owns implementing templates and Sass to match.
- **Styling decisions locked:** Sass (not plain CSS); design tokens in `_variables.scss`. Colors: white background (#ffffff), soft black for primary text (#222222 or #1a1a1a, not pure black), gray for secondary text (date, “By”) and for lines (e.g. nav separator). Links: soft black with underline or distinct color per design.

## Recent Changes

- PRD updated to: reference `designs/` in overview and in PR #3; use Sass with variables for design system; document color variables (white, soft black, gray for secondary and lines).
- Memory Bank created and populated from PRD and these decisions.

## Next Steps

- Execute PRs in order: start with **PR #1 (DNS)** if subdomain is needed first, then **PR #2 (structure + build script)**, then **PR #3 (templates + Sass + design)**. PR #8 (portfolio nav) after PR #1 and PR #7.

## Active Decisions

- **Design system:** Sass variables for spacing, typography, colors; install Sass tooling in PR #3.
- **Design reference:** All visual and layout choices in PR #3 must align with `designs/`.
- **Color palette:** White bg; soft black (readability); gray for metadata and borders. No pure black.
