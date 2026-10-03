# Example prompts

These are illustrative starting points, not recorded test results. Use `/patchwork` or `/spike` in Claude Code, or `$patchwork` and `$spike` in Codex.

## Patchwork

Attach a screenshot of an existing business listing page:

> Use Patchwork to add appointment booking to this page. Show two options: below the business details and in the sidebar. Include service selection and available times.

Expected output: a shareable HTML wireframe under `design-artifacts/wireframes/`, with layout options, simplified existing content, a detailed grayscale booking proposal, and review notes. The “Show proposed” toggle controls the proposal highlights.

Follow up:

> Keep the sidebar option. Show the next three available times with a link to see the full schedule.

## Spike

Open a project whose search interface you want to investigate:

> Use Spike to compare a side panel and an expanded row for previewing search results. Use a small synthetic dataset. Show both on one comparison page so I can choose before we change the app.

Expected output: a self-contained experiment under `studies/<slug>/`, a comparison artifact, and a README recording the question, method, results, and recommendation. Implementation waits for your choice.

Follow up:

> Park this experiment for now. Record what we learned and what would need to change before we revisit it.

Expected follow-up: a dated PARKED outcome in the experiment README, preserving the comparison and reasoning.
