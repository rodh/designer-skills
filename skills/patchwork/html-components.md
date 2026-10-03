# HTML Components — Patchwork

Component reference for Patchwork. Use these exact HTML structures and classes when generating wireframe content. Each snippet shows the correct semantic elements, class names, and structure. Readable components below are for proposed content; do not copy their labels or values into unchanged areas. Semantic classes such as `success`, `warning`, and `accent` are grayscale by default, including interaction states. They do not authorize color.

Use `.existing-section` for padded existing blocks and `.existing-region` on existing custom layout blocks. Every product region must be classified as existing or proposed; neutral grid/layout wrappers may contain both as siblings. Keep the classification in HTML comments for revisions. Do not nest `.new-section` within an existing wrapper or wrap unchanged content in `.new-section`.

Icons in proposed components, when useful, must be monochrome inline SVG using `currentColor`; omit optional icons rather than inserting emoji. Existing media uses `.placeholder-media` with a short descriptor, never the original colored image.

## HTML Components Reference

**Browser chrome frame** — wraps every wireframed page:
```html
<div class="page-chrome">
  <div class="chrome-header">
    <span class="chrome-dot r"></span><span class="chrome-dot y"></span><span class="chrome-dot g"></span>
    <span class="chrome-url">example.com/page-url</span>
  </div>
  <!-- page content here -->
</div>
```

**Existing section** — low-fidelity placeholder for current content:
```html
<div class="existing-section">
  <div class="existing-label">Section Name</div>
  <div class="placeholder-bar" style="width:90%"></div>
  <div class="placeholder-bar" style="width:70%"></div>
  <div class="placeholder-bar" style="width:55%"></div>
</div>
```

When a screenshot is provided, existing sections should match the actual page's layout structure. Each distinct page area gets its own block — never merge multiple areas into one generic label. Examples of structurally faithful existing content:

```html
<!-- Header — logo shape + search shape, not a generic "Site Header" block -->
<div class="site-header existing-region">
  <div class="site-logo"><div class="site-logo-icon"></div></div>
  <div class="site-search"><div class="placeholder-bar" style="width:140px; height:10px"></div></div>
</div>

<!-- Hero — gray rectangle with alt text, not "Hero Banner" + bars -->
<div class="hero-banner-img existing-region placeholder-media">HERO BANNER IMAGE</div>

<!-- Business identity — real name, gray pill for badge, bars for ratings -->
<div class="biz-identity existing-region">
  <div class="placeholder-bar" style="width:100px; height:18px; border-radius:10px"></div>
  <div class="biz-name">Dunkin'</div>
  <div class="placeholder-bar" style="width:140px"></div>
</div>

<!-- Action buttons — unlabeled gray pill shapes, not a "Action Buttons" block -->
<div class="cta-row existing-region">
  <div class="placeholder-bar" style="width:110px; height:28px; border-radius:20px"></div>
  <div class="placeholder-bar" style="width:70px; height:28px; border-radius:20px"></div>
  <div class="placeholder-bar" style="width:65px; height:28px; border-radius:20px"></div>
  <div class="placeholder-bar" style="width:55px; height:28px; border-radius:20px"></div>
</div>

<!-- Two-column grid — preserve layout, use placeholder bars for data -->
<div class="details-hours-grid existing-region">
  <div class="detail-block">
    <div class="detail-label">Business Details</div>
    <div class="placeholder-bar" style="width:85%"></div>
    <div class="placeholder-bar" style="width:55%"></div>
  </div>
  <div class="detail-block">
    <div class="detail-label">Hours</div>
    <div class="placeholder-bar" style="width:90%"></div>
    <div class="placeholder-bar" style="width:90%"></div>
  </div>
</div>
```

The CSS for these structural elements (`.site-header`, `.hero-banner-img`, `.biz-identity`, `.cta-row`, `.details-hours-grid`, etc.) is defined per-wireframe or in a project template, not in the base CSS library.

**New section** — detailed grayscale proposed content. The library adds a dashed outline (`::before`) and a small orange `PROPOSED` badge (`::after`) at the outline's top-right edge when highlights are on. Both disappear when highlights are off, without moving or hiding product content. These are review overlays, not product labels; do not add a separate badge in the markup. Leave room around the wrapper so the overlay is not clipped or covering nearby content, and keep any scrolling or overflow clipping on an inner element.
```html
<div class="new-section">
  <div class="new-section-title">Section Title</div>
  <!-- compose from atomic components: alerts, chips, badges, data-tables, etc. -->
</div>
```

**Partial change within an existing area** — keep unchanged context and the proposal in sibling wrappers. The shared grid is layout only:
```html
<!-- Existing: business details. Proposed: appointment booking only. -->
<div style="display:grid; grid-template-columns:1fr 1fr; gap:32px; padding:24px">
  <section class="existing-region">
    <h2 class="existing-label">Business Details</h2>
    <div class="placeholder-bar" style="width:85%"></div>
    <div class="placeholder-bar" style="width:60%"></div>
  </section>
  <section class="new-section">
    <h2 class="new-section-title">Book an appointment</h2>
    <p>Choose a time for your consultation.</p>
    <button class="action-btn primary">View available times</button>
  </section>
</div>
```

**Requested color exception** — only if evaluating a red overdue indicator is explicitly part of the request. The attribute documents intent; the local rule supplies color. Keep the rest of the proposal neutral and explain the exception in its outside annotation:
```html
<style>
  .new-section .badge[data-color-intent="overdue-indicator"] {
    color: #991b1b;
    background: #fef2f2;
  }
</style>
<!-- Inside a proposed section only -->
<span class="badge" data-color-intent="overdue-indicator">Overdue</span>
```

**Page connector** — between two page-chrome blocks showing navigation flow:
```html
<div class="page-connector">clicks through to</div>
```

**Annotation** — review prompts placed after each page-chrome block:
```html
<div class="annotation">
  <strong>Decisions to evaluate:</strong><br>
  — Should the activity feed be collapsible, or always visible? A long feed could push the member table below the fold.<br>
  — Is sorting/filtering on the member table needed at this fidelity, or does the 4-row default suffice?<br>
  — "Needs support" vs. "At risk" — which label better matches the team's vocabulary?<br><br>
  <strong>Assumptions:</strong><br>
  — Sprint data (completion rate, cycle time) is already available from the task backend — no new integrations needed.<br>
  — The on-time threshold (currently 80%) would be configurable per-project, not hardcoded.<br>
  — Trend sparklines per member were deferred — revisit if the team wants historical context at a glance.
</div>
```

**Before/after comparison** — showing how a proposal changes an outcome. Include only when explicitly requested by the user:
```html
<div class="comparison-demo">
  <div class="comparison-demo-title">Scenario — Before vs. After</div>
  <div class="comparison-query"><span class="prompt">&gt;</span> User question or scenario description</div>
  <div class="comparison-label before">Without proposed change</div>
  <div class="comparison-before">What happens today — the gap or failure.</div>
  <div class="comparison-label after">With proposed change</div>
  <div class="comparison-after">What happens with the proposal — the improvement. <span class="comparison-source">Source: feature name</span></div>
</div>
```

**Navbar** — horizontal navigation bar:
```html
<nav class="navbar">
  <div class="navbar-brand">Brand</div>
  <ul class="navbar-links">
    <li><a href="#" aria-current="page">Active</a></li>
    <li><a href="#">Link</a></li>
    <li><a href="#">Link</a></li>
  </ul>
</nav>
```

**Sidebar nav** — vertical navigation links:
```html
<nav class="sidebar-nav">
  <a href="#" aria-current="page">Active Item</a>
  <a href="#">Menu Item</a>
  <a href="#">Menu Item</a>
</nav>
```

**Bottom nav** — mobile bottom tab bar:
```html
<nav class="bottom-nav">
  <a href="#" class="bottom-nav-item" aria-current="page">
    <svg class="icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 10l9-7 9 7v11h-7v-7h-4v7H3z"/></svg>Home
  </a>
  <a href="#" class="bottom-nav-item">
    <svg class="icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="10" cy="10" r="7"/><path d="M15 15l6 6"/></svg>Search
  </a>
  <a href="#" class="bottom-nav-item">
    <svg class="icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="7" r="4"/><path d="M4 22v-3a8 8 0 0116 0v3"/></svg>Profile
  </a>
</nav>
```

**Breadcrumb nav** — navigation trail with aria-current:
```html
<nav class="breadcrumb-nav" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Home</a></li>
    <li><a href="#">Section</a></li>
    <li><span aria-current="page">Current Page</span></li>
  </ol>
</nav>
```

**Pagination** — page navigation:
```html
<div class="pagination">
  <button disabled>&laquo;</button>
  <button class="active">1</button>
  <button>2</button>
  <button>3</button>
  <button>&raquo;</button>
</div>
```

**Stat card** — KPI/metric display:
```html
<div class="stat-card">
  <div class="stat-card-label">Metric Name</div>
  <div class="stat-card-value">1,234</div>
  <div class="stat-card-delta up">+12% vs last month</div>
</div>
```

**Feature card** — icon + title + description:
```html
<div class="feature-card">
  <div class="feature-card-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M13 2L4 14h7l-1 8 10-13h-7z"/></svg></div>
  <div class="feature-card-title">Feature Name</div>
  <div class="feature-card-desc">Brief description of what this feature does and why it matters.</div>
</div>
```

**Data table** — styled table with header formatting and row hover:
```html
<table class="data-table">
  <thead>
    <tr><th>Column A</th><th>Column B</th><th>Column C</th></tr>
  </thead>
  <tbody>
    <tr><td>Value 1</td><td>Value 2</td><td>Value 3</td></tr>
    <tr><td>Value 4</td><td>Value 5</td><td>Value 6</td></tr>
  </tbody>
</table>
```

**Hero banner** — full-width centered heading + subtext + CTA:
```html
<div class="hero-banner">
  <div class="hero-banner-title">Page Headline</div>
  <div class="hero-banner-sub">Supporting text that describes the page purpose.</div>
  <div class="hero-banner-cta">
    <button class="action-btn primary">Primary Action</button>
    <button class="action-btn">Secondary</button>
  </div>
</div>
```

**Chip** — inline tag/pill (use `.chip-group` for multiple):
```html
<div class="chip-group">
  <span class="chip">Air Travel</span>
  <span class="chip">Dining</span>
  <span class="chip">Shopping</span>
</div>
```

**Badge** — inline status indicator:
```html
<span class="badge neutral">Draft</span>
<span class="badge success">Active</span>
<span class="badge warning">Pending</span>
<span class="badge accent">Priority</span>
```

**Avatar** — circular identity placeholder:
```html
<div class="avatar sm">A</div>
<div class="avatar">B</div>
<div class="avatar lg">C</div>
```

**Empty state** — zero-data display:
```html
<div class="empty-state">
  <div class="empty-state-title">No items yet</div>
  <div class="empty-state-desc">Create your first item to get started.</div>
</div>
```

**Skeleton** — static placeholder by default. Add `is-loading` only when demonstrating a proposed loading state; existing context stays static:
```html
<div class="skeleton heading"></div>
<div class="skeleton text"></div>
<div class="skeleton text" style="width:60%"></div>
<div class="skeleton circle"></div>
<div class="skeleton rect"></div>
```

**Alert** — semantic notification (`.info`, `.success`, `.warning`, `.error`):
```html
<div class="alert info">
  <svg class="alert-icon" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 10v7m0-10v1"/></svg>
  <div><strong>Tip:</strong> Helpful information for the user.</div>
</div>
<div class="alert success">
  <svg class="alert-icon" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 12l5 5L20 6"/></svg>
  <div><strong>Done.</strong> The action completed successfully.</div>
</div>
<div class="alert warning">
  <svg class="alert-icon" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3L2 21h20zM12 9v5m0 2v2"/></svg>
  <div><strong>Heads up.</strong> Something to watch out for.</div>
</div>
<div class="alert error">
  <svg class="alert-icon" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19"/></svg>
  <div><strong>Error.</strong> Something went wrong.</div>
</div>
```

**Dropdown menu** — flyout menu with button items:
```html
<div class="dropdown-menu">
  <button>Edit</button>
  <button>Duplicate</button>
  <div class="divider"></div>
  <button>Delete</button>
</div>
```

**Action row** — action buttons:
```html
<div class="action-row">
  <button class="action-btn primary">Primary Action</button>
  <button class="action-btn">Secondary</button>
  <button class="action-btn">Another</button>
</div>
```

**Text input** — labeled input field with neutral focus ring:
```html
<div class="input-container">
  <label for="field-id">Label</label>
  <input type="text" id="field-id" placeholder="Placeholder text">
</div>
```

**Textarea** — multi-line input with vertical resize:
```html
<div class="input-container">
  <label for="notes">Label</label>
  <textarea id="notes" placeholder="Placeholder text" rows="3"></textarea>
</div>
```

**Search field** — input with search icon:
```html
<div class="search-container">
  <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/>
  </svg>
  <input type="search" placeholder="Search...">
</div>
```

**Toggle switch** — on/off toggle with accessible checkbox:
```html
<label class="toggle-label">
  <input type="checkbox" checked>
  <span class="toggle-track"></span>
  Toggle label
</label>
```

**Select dropdown** — styled native select:
```html
<div class="select-container">
  <select>
    <option>Option one</option>
    <option>Option two</option>
    <option>Option three</option>
  </select>
</div>
```

**Accordion** — expandable sections using details/summary:
```html
<div class="accordion">
  <details open>
    <summary>First section title</summary>
    <div class="accordion-body">Content for the first section.</div>
  </details>
  <details>
    <summary>Second section title</summary>
    <div class="accordion-body">Content for the second section.</div>
  </details>
</div>
```

**Checkbox group** — multiple checkboxes with custom styling:
```html
<fieldset class="check-group">
  <legend>Group label</legend>
  <label class="check-label">
    <input type="checkbox" checked>
    <span class="check-box"></span>
    Option one
  </label>
  <label class="check-label">
    <input type="checkbox">
    <span class="check-box"></span>
    Option two
  </label>
</fieldset>
```

**Radio group** — single-select with custom styling:
```html
<fieldset class="radio-group">
  <legend>Group label</legend>
  <label class="radio-label">
    <input type="radio" name="group-name" checked>
    <span class="radio-dot"></span>
    Option one
  </label>
  <label class="radio-label">
    <input type="radio" name="group-name">
    <span class="radio-dot"></span>
    Option two
  </label>
</fieldset>
```

**Modal dialog** — use `open` attribute for static wireframe display:
```html
<dialog class="wf-dialog" open>
  <div class="wf-dialog-header">
    <h2>Dialog title</h2>
    <button class="wf-dialog-close">&times;</button>
  </div>
  <div class="wf-dialog-body">
    Dialog body content goes here.
  </div>
  <div class="wf-dialog-footer">
    <button class="action-btn">Cancel</button>
    <button class="action-btn primary">Confirm</button>
  </div>
</dialog>
```

**Progress bar** — visual progress indicator:
```html
<div class="progress-bar">
  <div class="progress-bar-fill" style="width: 65%"></div>
</div>
```

#### Interactive Components Guidelines

When a wireframe includes interactive elements, follow these rules:

1. **Semantic elements are mandatory.** Use `<button>` for actions, `<input>`/`<textarea>`/`<select>` for form fields, `<details>`/`<summary>` for accordions, `<dialog>` for modals. Never use styled `<div>` or `<span>` as a substitute for an interactive element.

2. **Hover and focus states are built in.** All interactive components in the library include `:hover` and `:focus-visible` styles. No additional CSS is needed — just use the correct HTML elements and classes.

3. **Buttons use `<button>`, not `<span>` or `<div>`.** This includes `.action-btn`, `.wf-dialog-close`, `.dropdown-menu` items, `.pagination` buttons, and any clickable control.

4. **Form inputs are always inside `.input-container` or `.search-container`.** These containers provide the border, focus glow, and layout. The input element itself is reset to borderless/backgroundless.

5. **Toggle, checkbox, and radio use hidden native inputs.** The real `<input>` is visually hidden but remains in the DOM for accessibility and form semantics. The visual indicator (`.toggle-track`, `.check-box`, `.radio-dot`) is styled via the adjacent sibling selector.

6. **Accordion uses native `<details>`/`<summary>`.** No JavaScript required — the browser handles open/close. Use `open` attribute on the first item if it should default open.

7. **Dialog uses `<dialog>` with `open` attribute.** For static wireframes, the `open` attribute displays the dialog inline. The backdrop style applies when opened programmatically with `.showModal()`.

8. **Data table rows have CSS hover states.** `.data-table tbody tr:hover` applies a background highlight — no additional styling needed.

9. **Navigation links use `aria-current="page"`.** `.navbar-links a`, `.sidebar-nav a`, and `.bottom-nav-item` all style active state via `a[aria-current="page"]`. Use `<a>` elements for navigation items.

10. **Pagination uses `<button>` elements.** Use the `disabled` attribute for unavailable pages and `.active` class for the current page.

11. **Component inventory.** The full set of components available: stat card, feature card, data table, hero banner, chip/chip-group, badge (neutral/success/warning/accent), avatar (sm/default/lg), empty state, skeleton (text/heading/circle/rect), alert (info/success/warning/error), dropdown menu, pagination, navbar, sidebar nav, bottom nav, breadcrumb nav, text input, textarea, search field, toggle switch, select dropdown, accordion, checkbox group, radio group, modal dialog, progress bar, action buttons (primary + secondary), tab navigation.

#### Tab Switching JS

Include at the bottom of the `<body>` when using tabs:
```html
<script>
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.getElementById('tab-' + btn.dataset.tab).classList.add('active');
    btn.classList.add('active');
  });
});
</script>
```

## Component Inventory

| Category | Components |
|---|---|
| **Navigation** | Navbar, Sidebar nav, Bottom nav, Breadcrumb nav, Tab navigation, Pagination |
| **Wireframe Structure** | Page chrome, Existing section, New section, Page connector, Annotation (decisions + assumptions), Before/after comparison (on request) |
| **Content** | Stat card, Feature card, Data table, Hero banner, Chip/chip-group, Badge (neutral/success/warning/accent), Avatar (sm/default/lg), Empty state, Skeleton (text/heading/circle/rect) |
| **Forms** | Text input, Textarea, Search field, Toggle switch, Select dropdown, Accordion, Checkbox group, Radio group |
| **Feedback** | Alert (info/success/warning/error), Progress bar |
| **Overlays** | Modal dialog, Dropdown menu |
| **Actions** | Action buttons (primary + secondary), Action row |
