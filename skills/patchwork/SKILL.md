---
name: patchwork
description: Sketch page changes in context. Use when the user wants to wireframe
  or mock up targeted additions, section revisions, or layout changes within an
  existing page, including before/after comparisons when requested.
---

# Patchwork

Sketch page changes in context.

## Overview

Produces self-contained HTML wireframes that communicate proposed page changes through a **fidelity gradient**: existing content renders as low-fidelity placeholders (real headings + gray bars), while proposed content renders as a detailed grayscale wireframe: readable copy, plausible data, and usable controls, with restrained library styling. Detail is informational, not production visual polish. This automatic contrast draws the viewer's eye to what's new without any labels or legends. The wireframe uses a consistent visual language — browser chrome frames, annotation callouts (decisions to evaluate + assumptions), and a "Show proposed" toggle for dashed accent borders around new sections.

## When to Use

- User asks to wireframe, mockup, or sketch a page change
- User wants to visualize proposed new sections or features on an existing page
- User needs before/after comparisons of a UI change (use only when explicitly requested)
- User provides a screenshot and wants to show additions integrated into the real layout
- User asks for layout variations (tabs) of the same concept

## When NOT to Use

- User wants production-ready UI code
- User wants a design system or style guide
- User is asking about UX strategy without needing a visual artifact
- The task is pure content writing with no visual layout component

## Phase 1 — Intake

Read the user's description of what page or feature they're wireframing. Scan for existing screenshots, design artifacts, or scope docs relevant to this work — check `design-artifacts/` and one level of subfolders.

Identify:
- **What exists today** — the current page layout, sections, and structure
- **What's being proposed** — the new content, sections, or changes
- **How many examples/variations** are needed (one tab per variation)
- **Whether a screenshot was provided** — if so, you will match its layout faithfully

If a screenshot is provided, study it carefully. You will reproduce the actual column structure, sidebar placement, section order, and spacing. Don't invent a new layout — integrate proposed additions into the real layout.

If a missing answer would materially change the proposal, ask one concise question using the available question tool or chat. Don't block on minor details — mark gaps as assumptions and move on.

Check for **project templates** in `design-artifacts/wireframes/` — files prefixed with `_` (e.g., `_<project-name>-template.html`). If one exists for the project being wireframed, read it. Reuse project-template layout and components for consistency. Normalize their colors and fidelity to this skill before reuse; a template or screenshot is evidence of layout, not permission to import brand colors, imagery, or production styling. An explicit user instruction can override the default; apply it only to the requested scope.

## Phase 2 — Structure

Decide the wireframe layout before generating:

- **Single page or multi-page flow?** If the proposal involves clicking through to a new page, use a `.page-connector` between `.page-chrome` blocks.
- **How many tab variations?** One tab per location type, approach, or example. Use tabs when showing the same concept across different contexts.
- **What existing sections to show?** Render these as low-fidelity placeholders — real headings, placeholder bars for body content.
- **What new sections to show?** Render these as detailed grayscale wireframes — readable text, supplied or plausible sample data, and concrete structure.
- **Before/after comparison needed?** Use `.comparison-demo` blocks only if the user explicitly requests a before/after comparison.

Classify each region before coding as **existing** or **proposed**. Keep this map in HTML comments so later revisions preserve the boundary. For a change within an existing area, mark only the changed component as proposed; use sibling wrappers for unchanged context and the proposal rather than nesting an entire proposal in an existing wrapper. A wholly new page may be entirely proposed, while reused navigation remains existing. Unknown existing copy becomes placeholders; do not invent a filled-in current page.

Tell the user your proposed structure in 2–3 sentences, then generate.

## Phase 3 — Generate

Produce a single self-contained HTML file using the component library in the reference files. Save to `design-artifacts/wireframes/<descriptive-name>.html`.

Create the `design-artifacts/wireframes/` directory if it doesn't exist.

If a **project template** was found in Phase 1, use it as the foundation: combine the base CSS library with the normalized project-specific layout CSS from the template, use its HTML skeleton, and draw from its reusable components. Add wireframe-specific CSS only for elements not already in the template.

### Container Width

Default `.container` uses `max-width: 960px`. Override to `1200px` or `100%` for wider layouts, either inline or in a project template.

### Layout and Composition

The base library provides **atomic components** and **navigation primitives** — not layout systems. Multi-column grids, hero layouts, banner compositions, page-specific structures, and other layout patterns should be:

- **Defined per-wireframe** when used only once
- **Extracted into a project template** when shared across 2+ wireframes in the same project

This keeps the base library project-agnostic. Compose layouts from the atomic components in the reference files.

### Fidelity Target

Default to **low-detail context + detailed grayscale proposal**. More detail means more readable information, not more color, decoration, or invented UI.

| Region | Readable content | Rendering |
|---|---|---|
| Existing | Actual section headings and page/business name only; short media descriptors are allowed | Static bars, pills, and gray media blocks; preserve the distinct regions, proportions, and layout |
| Proposed | End-user headings, body copy, values, labels, and necessary states | Neutral library components; supplied facts or plausible sample values identified as assumptions outside the prototype |
| Review UI | Project title, annotations, navigation between frames, highlight toggle | Library orange only in the designated review components |

Do not add decorative illustrations, photos, gradients, expressive shadows, new typography, or extra components to make a proposal look finished. Use only the components needed to evaluate the requested change. Keep this fidelity target through iterations unless the user explicitly changes it; requests like “clean up” or “make clearer” do not promote existing content or authorize color.

### Fidelity Gradient

This is the core visual communication principle. Existing and new content render at different fidelity levels to create automatic contrast between "context" and "the point":

**Existing sections — low fidelity, but structurally faithful to the page:**

*What uses real text:*
- Section headings matching the actual page (e.g., "About", "Hours", "Business Details" — not meta-descriptions like "Business Details + Hours" or "Action Buttons")
- The business/page **name** (e.g., "Dunkin'") — orients the viewer to which page they're looking at

*What becomes placeholder shapes:*
- Body content (paragraphs, descriptions): placeholder bars
- Data values (addresses, phone numbers, URLs, hours, ratings, review text): placeholder bars
- Action buttons: unlabeled gray pill shapes preserving count and layout
- Badges/tags: unlabeled gray pills
- Images/maps: gray rectangles with small centered alt text describing what they represent (e.g., "HERO BANNER IMAGE", "MAP", "PHOTO GALLERY")

*Layout structure — preserve the page skeleton:*
- Render each distinct page area as its own structural block — header, breadcrumbs, hero, name block, button row, details grid, etc.
- Never merge multiple areas into a single generic labeled block
- Preserve column layouts (e.g., two-column grid for details + hours, each with its own heading)
- Preserve spatial relationships (e.g., buttons in a row, social links in a row)
- When a screenshot is provided, match its structure faithfully

*Style constraints:*
- **No color anywhere** in existing sections — use only the neutral tokens listed below
- **No emoji or icons** in existing content
- **Stable classification** — preserve existing placeholders across iterations unless the user explicitly proposes changing that area. Use `.existing-section` for padded blocks or `.existing-region` on custom layout blocks; do not apply these classes to a shared parent containing proposed content.

**New/proposed sections — detailed grayscale, this is the point:**
- Readable text, supplied or plausible sample data, real structure — enough detail to evaluate the proposal
- This is what the wireframe exists to communicate; it should be immediately readable and visually prominent
- Compose proposed content from atomic components: use `.alert` for tips/warnings, `.chip` for tags, `.badge` for status indicators, `.data-table` for tabular data, `.stat-card` for metrics, `.feature-card` for feature descriptions, etc.
- **The "Show proposed" toggle controls a review overlay:** a dashed accent outline and a small orange `PROPOSED` badge at the outline's top-right edge of each `.new-section`. Both are shown by default and hidden together when highlights are off, without changing layout or product content. Use the library's pseudo-elements; do not duplicate the badge in product markup. Keep the overlay clear of nearby content and clipping. Do not add other accent-colored labels, tinted backgrounds, or colored product text unless it meets the explicit color-exception rule below.

**The test:** If you turned off the outlines and badges, could a viewer still instantly tell which content is proposed vs. existing? Existing sections should feel like the page's gray skeleton — recognizable layout and shapes, with readable headings and the page name, but no body copy or data. If existing sections have color or filled-in data, the fidelity gradient is broken. Conversely, if existing sections are collapsed into generic labeled blocks that all look the same, the wireframe loses the page's identity and the viewer can't orient themselves.

### Color Contract

- **Neutral by default:** inside `.page-chrome`, use `--bg`, `--surface`, `--border`, `--text`, `--text-secondary`, `--existing-bg`, `--existing-border`, `--tag-bg`, `--hover-bg`, and `--link`. Semantic aliases (`--green`, `--red`, etc.) and the legacy `--accent` aliases resolve to neutrals in the library. Success, warning, selected, and focus states stay grayscale; communicate meaning with text, shape, weight, or borders.
- **Review orange has a fixed scope:** `--review-accent`, `--review-light`, and `--review-border` are reserved for the topbar project name, “Show proposed” control, `.new-section::before` outline and `.new-section::after` review badge, page connectors, and annotations. Never use these tokens for product copy, buttons, product badges, links, or charts. Browser chrome dots are gray.
- **No hidden color sources:** no emoji, colored images, hardcoded SVG fills, external icon fonts, or browser-default blue links/controls. Proposed icons, if necessary, use inline SVG with `currentColor`; existing content uses shapes instead of icons. Check hover, focus, checked, selected, visited, and open states as well as the initial view.
- **Color exceptions:** only when the user explicitly requests color or the specific design question is about color. Scope the exception to the smallest proposed element with `data-color-intent="[specific reason]"` and a local CSS rule. Record its purpose in the outside annotation. A success badge, screenshot palette, brand template, or desire to make content “pop” is not sufficient. Do not redefine the global palette or color existing content. Broader fidelity overrides require an explicit user request.
- **Fix the source:** remove or normalize conflicting template styles and inline colors. Do not conceal them with a blanket grayscale filter, opacity, or `!important` override; those leave the underlying fidelity errors and may obscure deliberate exceptions.

### Prototype Boundary

Readable proposed copy inside `.page-chrome` must read as if a real end user is looking at the product. Existing placeholder shapes, short media descriptors, and the simulated browser URL are intentional wireframe conventions. Hard rules:

- **No product meta-labels** — never write "NEW:", "PROPOSED", "UPDATED", "EXAMPLE:", or similar tags in product content. The library's toggle-controlled `PROPOSED` review badge is the sole exception; it belongs to the review overlay, not the product.
- **No design rationale sentences** — explanations of why a choice matters belong in annotations outside `.page-chrome`, never inline
- **No placeholder-as-explanation** — never write "metrics would appear here" or "this section shows…". Populate with realistic mock data instead
- **No section-purpose descriptions** — a heading like "Team Performance" is fine; a heading like "Team Performance (proposed new section to help managers track sprint health)" is not

**The test:** Read every line inside `.page-chrome` aloud. If proposed copy talks about the design rather than being the design, move it to the outside annotation.

### Pre-generation Check

Before writing HTML, check the region map against the request: unchanged regions remain placeholders, only requested changes are detailed, and any color exception has a specific reason. Read both references below before selecting components; do not rely on remembered defaults.

### Screenshot Fidelity

When a screenshot of the existing page is provided, **match its layout faithfully**:
- Reproduce the actual column structure, sidebar placement, section order, and spacing
- Don't invent a new layout — integrate proposed additions into the real layout
- Only deviate from the screenshot layout if the user explicitly asks for layout changes

### Component Library Reference

**You must Read these two files during generation:**

1. **[css-library.md](css-library.md)** (resolve relative to this skill) — contains the full CSS template (Google Fonts link + `<style>` block). Copy the entire code block verbatim into the wireframe's `<head>`.

2. **[html-components.md](html-components.md)** (resolve relative to this skill) — contains all HTML component snippets, interactive component guidelines, and tab switching JS. Use these exact structures and classes when building wireframe content.

### Output File Structure

Every wireframe follows this skeleton:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Wireframe — [Descriptive Title]</title>
<!-- Google Fonts link from css-library.md -->
<!-- Full CSS from css-library.md -->
</head>
<body>

<div class="topbar">
  <div class="topbar-title">
    <div><span>[Project]</span> — [Design Concept Name]</div>
    <div class="topbar-subtitle">[Page/Area Context]</div>
  </div>
  <!-- If multiple variations: .tab-nav with .tab-btn buttons -->
  <label class="toggle-label highlights-toggle">
    <input type="checkbox" id="highlights-toggle" checked>
    <span class="toggle-track"></span>
    Show proposed
  </label>
</div>

<div class="container">
  <!-- If tabs: wrap each variation in <div id="tab-[name]" class="tab-content"> -->
  <!-- Page chrome blocks, new sections, annotations -->
</div>

<!-- Highlights toggle JS (always included) -->
<script>
const ht = document.getElementById('highlights-toggle');
function updateHighlights() {
  document.body.classList.toggle('highlights-on', ht.checked);
}
ht.addEventListener('change', updateHighlights);
updateHighlights();
</script>
<!-- If tabs: include tab switching JS from html-components.md -->
</body>
</html>
```

## Phase 4 — Annotate

After generating the wireframe HTML, add **one annotation per page-chrome block** (`.annotation`), placed immediately after it. Each annotation has two sections:

1. **Decisions to evaluate** — real open questions for the reviewer. These should be genuine choices the reviewer needs to weigh, not rhetorical questions with obvious answers. Format each as a dash-prefixed line using `<br>`.

2. **Assumptions** — what the wireframe takes for granted (data availability, configurability, scope boundaries) and what was explicitly deferred. Format each as a dash-prefixed line using `<br>`.

Bold the section headings with `<strong>`. Separate the two sections with `<br><br>`.

**Anti-patterns — do not write annotations that:**
- Describe what the wireframe already shows ("The stat cards surface sprint-level metrics")
- Explain why a design choice matters ("This helps managers spot issues faster")
- Restate the user's request as an insight ("Adding team performance to the dashboard addresses the visibility gap")

**Before/after comparisons** (`.comparison-demo`) — include only when the user explicitly requests one. Do not include by default.

This phase is a checklist to confirm annotations are present, useful, and contain no design rationale.

## Phase 5 — Verify the Rendered Result

Open the final HTML in an available browser and inspect every variation at the intended viewport. Compare screenshot-based layouts at a comparable width. If browser inspection is unavailable, inspect the source and state that visual verification was not performed.

- **Highlights off:** both outlines and `PROPOSED` badges disappear. Existing regions show only the allowed orientation text and static placeholders. Proposed regions are readable, without unnecessary polish. Columns, area boundaries, and proportions still match the source. Turning highlights off must not change layout or hide product content.
- **Highlights on:** only proposed regions receive dashed orange outlines and `PROPOSED` review badges. No outline encloses unchanged content. Badges sit at the outline's top-right edge without clipping, covering content, or intercepting clicks; no other design labels or explanations appear in the product.
- **Color and states:** inspect computed text, background, border, outline, shadow, SVG fill/stroke, and pseudo-element colors, including hover/focus and controls in their checked/open states. Inspect links and browser chrome too. Non-neutral colors must belong to designated review UI or a documented local exception.
- **Interaction and revisions:** switch every tab, operate the highlight toggle, and exercise controls needed for the proposal. Ensure no clipping or overlap. On revisions, compare the region map with the earlier version so existing regions do not gain body text, imagery, or color accidentally.

Fix failures in the source and recheck the affected states before delivering the file. Do not claim the prose instructions alone guarantee fidelity.

## Quick Reference

| Category | Components |
|---|---|
| **Navigation** | Navbar, Sidebar nav, Bottom nav, Breadcrumb nav, Tab navigation, Pagination |
| **Wireframe Structure** | Page chrome, Existing section, New section, Page connector, Annotation (decisions + assumptions), Before/after comparison (on request) |
| **Content** | Stat card, Feature card, Data table, Hero banner, Chip/chip-group, Badge (4 variants), Avatar (3 sizes), Empty state, Skeleton (4 types) |
| **Forms** | Text input, Textarea, Search field, Toggle switch, Select dropdown, Accordion, Checkbox group, Radio group |
| **Feedback** | Alert (info/success/warning/error), Progress bar |
| **Overlays** | Modal dialog, Dropdown menu |
| **Actions** | Action buttons (primary + secondary), Action row |

## Common Mistakes

| Don't | Do |
|---|---|
| Use accent orange on content elements (links, labels, arrows, body text) | Reserve accent orange for wireframe structure only (dashed outlines, `PROPOSED` review badges, page connectors, topbar project name). Content links use neutral `var(--link)`, labels use `var(--text-secondary)`; review controls and annotations use review tokens |
| Add section-divider borders between every section | Only use borders when the original design has them or they serve a specific structural purpose (e.g., separating a two-column grid from the next area). Spacing and padding create sufficient separation |
| Use `<div>` or `<span>` for interactive elements | Use `<button>` for actions, `<input>`/`<textarea>`/`<select>` for form fields, `<details>`/`<summary>` for accordions, `<dialog>` for modals |
| Skip the highlights toggle | Always include the "Show proposed" toggle in the topbar. It defaults to on, showing dashed outlines and `PROPOSED` review badges together |
| Render existing sections at full fidelity | Existing sections get section headings + business name as real text, everything else as gray placeholder shapes. Detailed grayscale content is reserved for proposed changes |
| Use color in existing sections (green badges, purple logos, colored banners) | All existing content uses the neutral tokens in the Color Contract |
| Put emoji icons in existing buttons or labels | Existing buttons are unlabeled gray pill shapes. No emoji anywhere in existing content |
| Write readable body text in existing sections (addresses, phone numbers, hours, URLs) | Replace all body content and data values with placeholder bars. Only section headings and the business name use real text |
| Collapse multiple distinct page areas into a single labeled block (e.g., "Site Header + Breadcrumbs + Hero") | Render each area as its own structural block — header, breadcrumbs, hero, name, buttons, details grid are all separate |
| Reproduce full data structures (hours tables, review bar charts, ratings) in existing sections | A few placeholder bars convey "there's a table here" without competing with proposed content |
| Add background colors or accent-colored product labels to proposed sections to make them "pop" | The toggle-controlled outline and `PROPOSED` badge are the review markers. Fidelity contrast does the rest. Other color requires a scoped, documented exception under the Color Contract |
| Add meta-labels to product copy ("NEW:", "PROPOSED", "EXAMPLE:") | Proposed copy reads as product copy; only the library's toggle-controlled `PROPOSED` review badge is allowed as an overlay. Existing placeholders and media descriptors remain allowed |
| Write placeholder-as-explanation text ("metrics would appear here", "this section shows…") | Populate with realistic mock data. If the data shape is unclear, use plausible values |
| Write annotations that describe what the wireframe shows ("The stat cards surface sprint metrics") | Annotations contain decisions to evaluate + assumptions to validate — not narration |
| Include before/after comparison by default | Only include `.comparison-demo` when the user requests it |

## Rules

1. **Self-contained HTML** — must work by opening the file in a browser. No build step, no external dependencies except Google Fonts.
2. **One file per concept** — use tabs for variations within a single concept.
3. **Match screenshot layout when provided** — reproduce actual column structure, sidebar placement, section order, and spacing. Don't invent a new layout.
4. **Use the component library** — preserve component structures, fonts, and default palette; scope any explicit color exception under the Color Contract. Consistency IS the value. Read `css-library.md` and `html-components.md` for the full reference.
