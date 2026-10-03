# CSS Library — Patchwork

Base CSS library for Patchwork. Copy verbatim into every generated wireframe. Combine with project-template layout CSS when one exists; normalize its colors to this palette. Product components are neutral by default, including semantic variants and interaction states. Orange belongs only to review UI. A requested product-color exception must be scoped to the smallest proposed component with `data-color-intent`; never recolor `:root` or an existing region.

## Full CSS Template

```html
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  /* ═══════════════════════════════════════
     FOUNDATION — resets, variables, base
     ═══════════════════════════════════════ */
  *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

  :root {
    --bg: #f5f5f5;
    --surface: #ffffff;
    --border: #d4d4d4;
    --text: #1a1a1a;
    --text-secondary: #6b6b6b;
    --review-accent: #e85d26;
    --review-light: #fff4ef;
    --review-border: #f4a67a;
    --accent: var(--text);
    --accent-light: var(--bg);
    --accent-border: var(--border);
    --existing-bg: #ffffff;
    --existing-border: #e0e0e0;
    --tag-bg: #ebebeb;
    --green: var(--text);
    --green-light: var(--bg);
    --yellow: var(--text);
    --yellow-light: var(--bg);
    --red: var(--text);
    --red-light: var(--bg);
    --blue: var(--text);
    --blue-light: var(--bg);
    --hover-bg: #efefef;
    --link: var(--text);
    color-scheme: light;
    accent-color: var(--text);
  }

  body {
    font-family: 'DM Sans', sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
  }

  a { color: var(--link); }
  a:visited { color: var(--link); }

  /* Button & input resets */
  button {
    border: none; background: none; padding: 0;
    font: inherit; color: inherit; cursor: pointer;
  }
  input, textarea, select {
    border: none; background: none; padding: 0;
    font: inherit; color: inherit; outline: none;
  }

  /* Focus states */
  button:focus-visible, a:focus-visible {
    outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 4px;
  }
  .input-container:focus-within {
    border-color: var(--accent-border);
    box-shadow: 0 0 0 2px var(--accent-light);
  }

  /* ═══════════════════════════════════════
     NAVIGATION — topbar, navbar, sidebar,
     bottom nav, breadcrumbs, tabs, pagination
     ═══════════════════════════════════════ */

  /* Topbar (wireframe header) */
  .topbar {
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    padding: 16px 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 100;
  }
  .topbar-title { font-size: 18px; font-weight: 600; color: var(--text-secondary); display: flex; flex-direction: column; gap: 2px; }
  .topbar-title span { color: var(--review-accent); font-weight: 700; }
  .topbar-subtitle {
    font-family: 'IBM Plex Mono', monospace; font-size: 13px; font-weight: 400;
    letter-spacing: 0.04em; text-transform: uppercase; color: var(--text-secondary);
  }
  .highlights-toggle {
    --accent: var(--review-accent);
    font-size: 14px;
    color: var(--text-secondary);
    white-space: nowrap;
  }

  /* Navbar — horizontal navigation */
  .navbar {
    display: flex; align-items: center; justify-content: space-between;
    padding: 12px 20px; background: var(--surface);
    border-bottom: 1px solid var(--border);
  }
  .navbar-brand { font-size: 18px; font-weight: 700; letter-spacing: -0.02em; }
  .navbar-links { display: flex; gap: 4px; list-style: none; }
  .navbar-links a {
    padding: 6px 12px; border-radius: 6px; font-size: 16px; font-weight: 500;
    color: var(--text-secondary); text-decoration: none; transition: background 0.15s ease;
  }
  .navbar-links a:hover { background: var(--hover-bg); color: var(--text); }
  .navbar-links a[aria-current="page"] {
    background: var(--tag-bg); color: var(--text); font-weight: 600;
  }

  /* Sidebar nav — vertical navigation */
  .sidebar-nav { display: flex; flex-direction: column; gap: 2px; padding: 8px 0; }
  .sidebar-nav a {
    display: block; padding: 8px 16px; border-radius: 6px; font-size: 16px;
    color: var(--text-secondary); text-decoration: none; transition: background 0.15s ease;
  }
  .sidebar-nav a:hover { background: var(--hover-bg); color: var(--text); }
  .sidebar-nav a[aria-current="page"] {
    background: var(--hover-bg); color: var(--text); font-weight: 600;
    border-left: 3px solid var(--text-secondary);
  }

  /* Bottom nav — mobile tab bar */
  .bottom-nav {
    display: flex; justify-content: space-around; align-items: center;
    padding: 8px 0; background: var(--surface);
    border-top: 1px solid var(--border);
    position: fixed; bottom: 0; left: 0; right: 0; z-index: 100;
  }
  .bottom-nav-item {
    display: flex; flex-direction: column; align-items: center; gap: 2px;
    padding: 4px 12px; font-size: 12px; color: var(--text-secondary);
    text-decoration: none; transition: color 0.15s ease;
  }
  .bottom-nav-item .icon { font-size: 20px; }
  .bottom-nav-item[aria-current="page"] { color: var(--text); font-weight: 600; }

  /* Breadcrumb nav */
  .breadcrumb-nav { font-size: 17px; }
  .breadcrumb-nav ol {
    list-style: none; display: flex; flex-wrap: wrap; align-items: center; gap: 0;
    padding: 0; margin: 0;
  }
  .breadcrumb-nav li { display: flex; align-items: center; }
  .breadcrumb-nav li + li::before {
    content: '/'; color: var(--text-secondary); margin: 0 8px; font-weight: 400;
  }
  .breadcrumb-nav a {
    color: var(--link); text-decoration: none; transition: color 0.15s ease;
  }
  .breadcrumb-nav a:hover { text-decoration: underline; }
  .breadcrumb-nav [aria-current="page"] {
    color: var(--text); font-weight: 600;
  }

  /* Tabs */
  .tab-nav { display: flex; gap: 4px; background: var(--tag-bg); border-radius: 8px; padding: 3px; }
  .tab-btn {
    font-family: 'DM Sans', sans-serif; font-size: 17px; font-weight: 500;
    padding: 8px 16px; border: none; background: transparent; color: var(--text-secondary);
    border-radius: 6px; cursor: pointer; transition: all 0.15s ease; white-space: nowrap;
  }
  .tab-btn:hover { color: var(--text); background: rgba(255,255,255,0.5); }
  .tab-btn.active { background: var(--surface); color: var(--text); box-shadow: 0 1px 3px rgba(0,0,0,0.08); }

  /* Pagination */
  .pagination {
    display: flex; align-items: center; gap: 4px;
  }
  .pagination button {
    min-width: 36px; height: 36px; border-radius: 6px; font-size: 15px; font-weight: 500;
    display: flex; align-items: center; justify-content: center;
    border: 1px solid var(--border); background: var(--surface); color: var(--text-secondary);
    transition: background 0.15s ease, border-color 0.15s ease;
  }
  .pagination button:hover:not(:disabled):not(.active) { background: var(--hover-bg); border-color: var(--border); }
  .pagination button.active {
    background: var(--text); color: var(--surface); border-color: var(--text);
  }
  .pagination button:disabled {
    opacity: 0.4; cursor: not-allowed;
  }

  /* ═══════════════════════════════════════
     WIREFRAME — chrome, connectors,
     containers, fidelity markers
     ═══════════════════════════════════════ */

  .container { max-width: 960px; margin: 0 auto; padding: 32px 24px 80px; }
  .tab-content { display: none; }
  .tab-content.active { display: block; }

  /* Page chrome */
  .page-chrome {
    background: var(--surface); border: 1px solid var(--border); border-radius: 12px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
  }
  .chrome-header {
    background: #fafafa; border-bottom: 1px solid var(--existing-border); padding: 10px 16px;
    display: flex; align-items: center; gap: 6px; font-size: 15px;
    color: var(--text-secondary); font-family: 'IBM Plex Mono', monospace;
  }
  .chrome-dot { width: 8px; height: 8px; border-radius: 50%; display: inline-block; }
  .chrome-dot.r, .chrome-dot.y, .chrome-dot.g { background: var(--border); }
  .chrome-url { margin-left: 12px; opacity: 0.6; }

  /* Existing sections */
  .existing-section {
    padding: 16px 20px;
    background: var(--existing-bg);
  }
  /* Use on custom layout blocks without adding existing-section padding. */
  .existing-region { color: var(--text-secondary); }
  .existing-label { font-size: 16px; font-weight: 600; color: var(--text-secondary); margin-bottom: 4px; }
  .placeholder-bar { height: 8px; background: var(--existing-border); border-radius: 3px; margin-bottom: 4px; }
  .placeholder-media {
    min-height: 120px; background: var(--tag-bg); color: var(--text-secondary);
    display: flex; align-items: center; justify-content: center;
    font-family: 'IBM Plex Mono', monospace; font-size: 12px;
  }

  /* Proposed review overlay — outline + badge, zero layout impact */
  .new-section {
    position: relative;
  }
  .new-section::before {
    content: '';
    position: absolute;
    top: -12px;
    bottom: -12px;
    left: -12px;
    right: -12px;
    border: 4px dashed var(--review-border);
    pointer-events: none;
    z-index: 0;
    display: none;
  }
  .new-section::after {
    content: 'PROPOSED';
    position: absolute;
    top: -12px;
    right: 0;
    transform: translateY(-50%);
    padding: 2px 6px;
    border-radius: 3px;
    background: var(--review-accent);
    color: var(--surface);
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    font-weight: 500;
    line-height: 1.4;
    letter-spacing: 0.04em;
    white-space: nowrap;
    pointer-events: none;
    z-index: 1;
    display: none;
  }
  body.highlights-on .new-section::before,
  body.highlights-on .new-section::after {
    display: block;
  }
  .new-section-title { font-size: 18px; font-weight: 700; margin-bottom: 12px; display: flex; align-items: center; gap: 8px; }

  /* Page connector */
  .page-connector {
    text-align: center; padding: 12px 0;
    font-family: 'IBM Plex Mono', monospace; font-size: 15px; color: var(--review-accent);
    display: flex; align-items: center; justify-content: center; gap: 8px;
  }
  .page-connector::before, .page-connector::after {
    content: ''; height: 1px; width: 40px; background: var(--review-border);
  }

  /* Annotation callout */
  .annotation {
    background: var(--review-light); border: 1px dashed var(--review-border); border-radius: 6px;
    padding: 10px 14px; margin-top: 16px; font-family: 'IBM Plex Mono', monospace;
    font-size: 15px; color: var(--review-accent); line-height: 1.6;
  }
  .annotation strong { font-weight: 600; }

  /* Before/after comparison */
  .comparison-demo {
    background: var(--surface); border: 1px solid var(--border); border-radius: 10px;
    padding: 20px 24px; margin-top: 24px;
  }
  .comparison-demo-title {
    font-family: 'IBM Plex Mono', monospace; font-size: 15px; font-weight: 500;
    letter-spacing: 0.04em; text-transform: uppercase; color: var(--text-secondary); margin-bottom: 14px;
  }
  .comparison-query {
    background: var(--text); color: var(--surface); border-radius: 8px; padding: 12px 14px;
    font-size: 18px; margin-bottom: 12px;
  }
  .comparison-query .prompt { color: inherit; font-weight: 600; margin-right: 6px; }
  .comparison-label {
    font-family: 'IBM Plex Mono', monospace; font-size: 14px; text-transform: uppercase;
    letter-spacing: 0.05em; margin-bottom: 6px; font-weight: 500;
  }
  .comparison-label.before { color: var(--text-secondary); }
  .comparison-label.after { color: var(--text); }
  .comparison-before {
    background: var(--bg); border: 1px solid var(--border); border-radius: 8px; padding: 12px 14px;
    font-size: 18px; line-height: 1.6; color: var(--text-secondary); margin-bottom: 12px;
  }
  .comparison-after {
    background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 12px 14px;
    font-size: 18px; line-height: 1.6; color: var(--text);
  }
  .comparison-source {
    display: inline; background: var(--tag-bg); padding: 1px 5px; border-radius: 3px;
    font-weight: 600; font-size: 16px;
  }

  /* ═══════════════════════════════════════
     CONTENT — cards, tables, chips, badges,
     avatars, empty states, skeletons, hero
     ═══════════════════════════════════════ */

  /* Stat card — KPI/metric display */
  .stat-card {
    background: var(--surface); border: 1px solid var(--border); border-radius: 10px;
    padding: 16px 20px;
  }
  .stat-card-label {
    font-family: 'IBM Plex Mono', monospace; font-size: 13px; font-weight: 500;
    text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-secondary);
    margin-bottom: 4px;
  }
  .stat-card-value { font-size: 28px; font-weight: 700; letter-spacing: -0.02em; }
  .stat-card-delta { font-size: 14px; font-weight: 600; margin-top: 4px; }
  .stat-card-delta.up { color: var(--green); }
  .stat-card-delta.down { color: var(--red); }
  .stat-card-delta.flat { color: var(--text-secondary); }

  /* Feature card — icon + title + description */
  .feature-card {
    background: var(--surface); border: 1px solid var(--border); border-radius: 10px;
    padding: 20px;
  }
  .feature-card-icon {
    width: 40px; height: 40px; border-radius: 8px; background: var(--tag-bg);
    display: flex; align-items: center; justify-content: center;
    font-size: 20px; margin-bottom: 12px;
  }
  .feature-card-title { font-size: 17px; font-weight: 700; margin-bottom: 4px; }
  .feature-card-desc { font-size: 15px; color: var(--text-secondary); line-height: 1.5; }

  /* Data table — styled table */
  .data-table { width: 100%; border-collapse: collapse; font-size: 16px; }
  .data-table thead th {
    text-align: left; padding: 10px 12px; font-size: 13px; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-secondary);
    font-family: 'IBM Plex Mono', monospace;
    border-bottom: 2px solid var(--border); background: var(--bg);
  }
  .data-table tbody td {
    padding: 10px 12px; border-bottom: 1px solid var(--existing-border);
  }
  .data-table tbody tr:hover { background: var(--hover-bg); }
  .data-table tbody tr:last-child td { border-bottom: none; }

  /* Hero banner — full-width heading + subtext + CTA */
  .hero-banner {
    padding: 32px 24px; text-align: center;
    background: var(--surface); border-bottom: 1px solid var(--border);
  }
  .hero-banner-title { font-size: 28px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 8px; }
  .hero-banner-sub { font-size: 18px; color: var(--text-secondary); margin-bottom: 16px; line-height: 1.5; }
  .hero-banner-cta { display: inline-flex; gap: 8px; }

  /* Chip — inline tag/pill */
  .chip {
    display: inline-flex; align-items: center; gap: 5px;
    background: var(--surface); border: 1px solid var(--border); border-radius: 6px;
    padding: 5px 10px; font-size: 15px; font-weight: 500;
  }
  .chip .chip-icon { font-size: 14px; }
  .chip-group { display: flex; flex-wrap: wrap; gap: 6px; }

  /* Badge — inline status indicator */
  .badge {
    display: inline-block; font-size: 13px; font-weight: 600;
    padding: 2px 8px; border-radius: 4px;
  }
  .badge.neutral { background: var(--tag-bg); color: var(--text-secondary); }
  .badge.success { background: var(--green-light); color: var(--green); }
  .badge.warning { background: var(--yellow-light); color: var(--yellow); }
  .badge.accent { background: var(--accent-light); color: var(--accent); }

  /* Avatar — circular identity placeholder */
  .avatar {
    width: 36px; height: 36px; border-radius: 50%;
    background: var(--tag-bg); display: flex; align-items: center; justify-content: center;
    font-size: 15px; font-weight: 600; color: var(--text-secondary); flex-shrink: 0;
  }
  .avatar.sm { width: 28px; height: 28px; font-size: 12px; }
  .avatar.lg { width: 48px; height: 48px; font-size: 20px; }

  /* Empty state — zero-data display */
  .empty-state {
    text-align: center; padding: 40px 20px;
  }
  .empty-state-icon { font-size: 36px; margin-bottom: 12px; color: var(--text-secondary); }
  .empty-state-title { font-size: 18px; font-weight: 700; margin-bottom: 4px; }
  .empty-state-desc { font-size: 15px; color: var(--text-secondary); line-height: 1.5; }

  /* Skeleton — static by default; animate only a proposed loading state. */
  .skeleton {
    background: var(--tag-bg); border-radius: 4px;
  }
  .new-section .skeleton.is-loading {
    animation: shimmer 1.5s infinite;
    background: linear-gradient(90deg, var(--tag-bg) 25%, var(--existing-border) 50%, var(--tag-bg) 75%);
    background-size: 200% 100%;
  }
  .skeleton.text { height: 14px; width: 80%; margin-bottom: 8px; }
  .skeleton.heading { height: 22px; width: 50%; margin-bottom: 12px; }
  .skeleton.circle { width: 40px; height: 40px; border-radius: 50%; }
  .skeleton.rect { height: 120px; width: 100%; border-radius: 8px; }
  @keyframes shimmer { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }

  /* ═══════════════════════════════════════
     FORMS — inputs, search, selects,
     toggles, checkboxes, radios
     ═══════════════════════════════════════ */

  /* Text input */
  .input-container {
    display: flex; align-items: center; gap: 8px;
    border: 1px solid var(--border); border-radius: 8px; padding: 10px 14px;
    background: var(--surface); transition: border-color 0.15s ease, box-shadow 0.15s ease;
  }
  .input-container label {
    font-size: 16px; font-weight: 600; color: var(--text-secondary); white-space: nowrap;
  }
  .input-container input {
    flex: 1; font-size: 18px; min-width: 0;
  }
  .input-container input::placeholder { color: var(--text-secondary); opacity: 0.6; }

  /* Textarea */
  .input-container textarea {
    flex: 1; font-size: 18px; min-width: 0; resize: vertical; min-height: 60px;
  }
  .input-container textarea::placeholder { color: var(--text-secondary); opacity: 0.6; }

  /* Search field */
  .search-container {
    display: flex; align-items: center; gap: 8px;
    border: 1px solid var(--border); border-radius: 8px; padding: 10px 14px;
    background: var(--surface); transition: border-color 0.15s ease, box-shadow 0.15s ease;
  }
  .search-container:focus-within {
    border-color: var(--accent-border);
    box-shadow: 0 0 0 2px var(--accent-light);
  }
  .search-container .search-icon {
    width: 16px; height: 16px; flex-shrink: 0; color: var(--text-secondary);
  }
  .search-container input[type="search"] {
    flex: 1; font-size: 18px; min-width: 0;
  }
  .search-container input[type="search"]::placeholder { color: var(--text-secondary); opacity: 0.6; }
  .search-container input[type="search"]::-webkit-search-cancel-button { -webkit-appearance: none; }

  /* Toggle switch */
  .toggle-label {
    display: inline-flex; align-items: center; gap: 10px; cursor: pointer;
    font-size: 18px;
  }
  .toggle-label input[type="checkbox"] {
    position: absolute; opacity: 0; width: 0; height: 0;
  }
  .toggle-track {
    width: 38px; height: 22px; border-radius: 11px; background: var(--border);
    position: relative; transition: background 0.2s ease; flex-shrink: 0;
  }
  .toggle-track::after {
    content: ''; position: absolute; top: 3px; left: 3px;
    width: 16px; height: 16px; border-radius: 50%; background: var(--surface);
    box-shadow: 0 1px 3px rgba(0,0,0,0.15); transition: transform 0.2s ease;
  }
  .toggle-label input[type="checkbox"]:checked + .toggle-track {
    background: var(--accent);
  }
  .toggle-label input[type="checkbox"]:checked + .toggle-track::after {
    transform: translateX(16px);
  }
  .toggle-label input[type="checkbox"]:focus-visible + .toggle-track {
    outline: 2px solid var(--accent); outline-offset: 2px;
  }

  /* Select dropdown */
  .select-container {
    display: inline-flex; align-items: center; position: relative;
    border: 1px solid var(--border); border-radius: 8px;
    background: var(--surface); transition: border-color 0.15s ease, box-shadow 0.15s ease;
  }
  .select-container:focus-within {
    border-color: var(--accent-border);
    box-shadow: 0 0 0 2px var(--accent-light);
  }
  .select-container select {
    appearance: none; -webkit-appearance: none;
    padding: 10px 36px 10px 14px; font-size: 18px; background: transparent;
    cursor: pointer; min-width: 140px;
  }
  .select-container::after {
    content: ''; position: absolute; right: 12px; top: 50%; transform: translateY(-50%);
    border-left: 4px solid transparent; border-right: 4px solid transparent;
    border-top: 5px solid var(--text-secondary); pointer-events: none;
  }

  /* Accordion */
  .accordion { border: 1px solid var(--border); border-radius: 8px; overflow: hidden; }
  .accordion details { border-bottom: 1px solid var(--border); }
  .accordion details:last-child { border-bottom: none; }
  .accordion summary {
    display: flex; align-items: center; justify-content: space-between;
    padding: 14px 16px; font-size: 18px; font-weight: 600; cursor: pointer;
    background: var(--surface); transition: background 0.15s ease;
    list-style: none;
  }
  .accordion summary::-webkit-details-marker { display: none; }
  .accordion summary::after {
    content: ''; width: 8px; height: 8px;
    border-right: 2px solid var(--text-secondary); border-bottom: 2px solid var(--text-secondary);
    transform: rotate(-45deg); transition: transform 0.2s ease; flex-shrink: 0;
  }
  .accordion details[open] > summary::after {
    transform: rotate(45deg);
  }
  .accordion summary:hover { background: var(--hover-bg); }
  .accordion .accordion-body { padding: 0 16px 14px; font-size: 18px; line-height: 1.55; }

  /* Checkbox group */
  .check-group { border: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 10px; }
  .check-group legend {
    font-size: 16px; font-weight: 600; color: var(--text-secondary);
    text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 6px;
    font-family: 'IBM Plex Mono', monospace;
  }
  .check-label {
    display: inline-flex; align-items: center; gap: 10px; cursor: pointer;
    font-size: 18px;
  }
  .check-label input[type="checkbox"] {
    position: absolute; opacity: 0; width: 0; height: 0;
  }
  .check-box {
    width: 18px; height: 18px; border: 2px solid var(--border); border-radius: 4px;
    display: flex; align-items: center; justify-content: center; flex-shrink: 0;
    transition: background 0.15s ease, border-color 0.15s ease;
  }
  .check-box::after {
    content: ''; width: 10px; height: 6px;
    border-left: 2px solid var(--surface); border-bottom: 2px solid var(--surface);
    transform: rotate(-45deg) translateY(-1px); opacity: 0; transition: opacity 0.15s ease;
  }
  .check-label input[type="checkbox"]:checked + .check-box {
    background: var(--accent); border-color: var(--accent);
  }
  .check-label input[type="checkbox"]:checked + .check-box::after { opacity: 1; }
  .check-label input[type="checkbox"]:focus-visible + .check-box {
    outline: 2px solid var(--accent); outline-offset: 2px;
  }

  /* Radio group */
  .radio-group { border: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 10px; }
  .radio-group legend {
    font-size: 16px; font-weight: 600; color: var(--text-secondary);
    text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 6px;
    font-family: 'IBM Plex Mono', monospace;
  }
  .radio-label {
    display: inline-flex; align-items: center; gap: 10px; cursor: pointer;
    font-size: 18px;
  }
  .radio-label input[type="radio"] {
    position: absolute; opacity: 0; width: 0; height: 0;
  }
  .radio-dot {
    width: 18px; height: 18px; border: 2px solid var(--border); border-radius: 50%;
    display: flex; align-items: center; justify-content: center; flex-shrink: 0;
    transition: border-color 0.15s ease;
  }
  .radio-dot::after {
    content: ''; width: 8px; height: 8px; border-radius: 50%;
    background: var(--accent); opacity: 0; transition: opacity 0.15s ease;
  }
  .radio-label input[type="radio"]:checked + .radio-dot {
    border-color: var(--accent);
  }
  .radio-label input[type="radio"]:checked + .radio-dot::after { opacity: 1; }
  .radio-label input[type="radio"]:focus-visible + .radio-dot {
    outline: 2px solid var(--accent); outline-offset: 2px;
  }

  /* ═══════════════════════════════════════
     FEEDBACK — alerts, progress bar
     ═══════════════════════════════════════ */

  /* Alert — semantic notifications */
  .alert {
    border-radius: 8px; padding: 14px 16px; font-size: 18px; line-height: 1.55;
    display: flex; gap: 10px; align-items: flex-start;
  }
  .alert-icon { font-size: 22px; flex-shrink: 0; }
  .alert strong { font-weight: 600; }
  .alert.info {
    background: var(--blue-light); border: 1px solid var(--border); color: var(--blue);
  }
  .alert.success {
    background: var(--green-light); border: 1px solid var(--border); color: var(--green);
  }
  .alert.warning {
    background: var(--yellow-light); border: 1px solid var(--border); color: var(--yellow);
  }
  .alert.warning strong { color: inherit; }
  .alert.error {
    background: var(--red-light); border: 1px solid var(--border); color: var(--red);
  }

  /* Progress bar */
  .progress-bar {
    height: 8px; background: var(--tag-bg); border-radius: 4px; overflow: hidden;
  }
  .progress-bar-fill {
    height: 100%; background: var(--accent); border-radius: 4px;
    transition: width 0.3s ease;
  }

  /* ═══════════════════════════════════════
     OVERLAYS — dialog, dropdown menu
     ═══════════════════════════════════════ */

  /* Modal dialog */
  .wf-dialog {
    border: 1px solid var(--border); border-radius: 12px; padding: 0;
    background: var(--surface); box-shadow: 0 8px 32px rgba(0,0,0,0.12);
    max-width: 480px; width: 100%;
  }
  .wf-dialog::backdrop { background: rgba(0,0,0,0.3); }
  .wf-dialog-header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 16px 20px; border-bottom: 1px solid var(--border);
  }
  .wf-dialog-header h2 { font-size: 20px; font-weight: 700; }
  .wf-dialog-close {
    width: 28px; height: 28px; border-radius: 6px; display: flex;
    align-items: center; justify-content: center; font-size: 18px;
    color: var(--text-secondary); transition: background 0.15s ease;
  }
  .wf-dialog-close:hover { background: var(--hover-bg); }
  .wf-dialog-body { padding: 20px; font-size: 18px; line-height: 1.55; }
  .wf-dialog-footer {
    display: flex; justify-content: flex-end; gap: 8px;
    padding: 16px 20px; border-top: 1px solid var(--border);
  }

  /* Dropdown menu */
  .dropdown-menu {
    background: var(--surface); border: 1px solid var(--border); border-radius: 8px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.1); padding: 4px 0; min-width: 180px;
  }
  .dropdown-menu button {
    display: block; width: 100%; text-align: left;
    padding: 8px 14px; font-size: 16px; color: var(--text);
    transition: background 0.15s ease;
  }
  .dropdown-menu button:hover { background: var(--hover-bg); }
  .dropdown-menu .divider {
    height: 1px; background: var(--border); margin: 4px 0;
  }

  /* ═══════════════════════════════════════
     ACTIONS — buttons
     ═══════════════════════════════════════ */

  /* Action row */
  .action-row {
    display: flex; gap: 8px; flex-wrap: wrap; padding: 14px 20px;
    background: var(--existing-bg);
  }
  .action-btn {
    display: inline-flex; align-items: center; gap: 5px;
    padding: 7px 14px; border-radius: 6px; font-size: 16px; font-weight: 500;
    border: 1px solid var(--existing-border); background: var(--surface); color: var(--text-secondary);
    transition: background 0.15s ease, border-color 0.15s ease;
  }
  .action-btn:hover { background: var(--bg); border-color: var(--border); }
  .action-btn.primary { background: var(--text); color: var(--surface); border-color: var(--text); }
  .action-btn.primary:hover { background: #333; }

  /* ═══════════════════════════════════════
     RESPONSIVE
     ═══════════════════════════════════════ */
  @media (max-width: 700px) {
    .topbar { flex-direction: column; gap: 10px; padding: 12px 16px; }
    .container { padding: 16px 12px 60px; }
    .tab-nav { overflow-x: auto; }
    .wf-dialog { max-width: calc(100vw - 32px); }
    .navbar { flex-direction: column; gap: 8px; }
    .navbar-links { flex-wrap: wrap; }
  }
</style>
```
