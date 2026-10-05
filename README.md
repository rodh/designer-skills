# Designer Skills

Skills by [Rod Howard](https://rodhoward.design) for exploring ideas before building them. Install one skill or the collection in Claude Code or Codex.

| Skill | Use it when | What you get |
| --- | --- | --- |
| [Patchwork](skills/patchwork) | You want to see how a change fits into an existing page. | An HTML wireframe with simplified existing content and a detailed grayscale proposal. |
| [Spike](skills/spike) | You need to test an uncertain idea before committing to implementation. | An isolated experiment, a comparison, and a written verdict. |

Each folder is self-contained. Neither skill requires the other.

## Install

Run these commands in your terminal. They use the [open-source skills CLI](https://github.com/vercel-labs/skills), which requires Node.js 22.20 or later. The installer lets you choose your agent and installation method.

**Patchwork**

```sh
npx skills add rodh/designer-skills --skill patchwork
```

**Spike**

```sh
npx skills add rodh/designer-skills --skill spike
```

**The complete collection**

```sh
npx skills add rodh/designer-skills --skill '*'
```

Keep the quotes around `'*'` so your shell does not expand it. By default, installation applies to the current project. Add `--global` to make the skills available across your projects.

To select an agent explicitly:

```sh
# Both skills, available across Claude Code projects
npx skills add rodh/designer-skills --skill '*' --agent claude-code --global

# Both skills, available across Codex projects
npx skills add rodh/designer-skills --skill '*' --agent codex --global

# Inspect the collection without installing
npx skills add rodh/designer-skills --list
```

You can also ask Codex: “Use $skill-installer to install skills/patchwork from rodh/designer-skills.” Specify both `skills/patchwork` and `skills/spike` to install both.

### Download instead

- [Download Patchwork](https://github.com/rodh/designer-skills/releases/latest/download/patchwork.zip)
- [Download Spike](https://github.com/rodh/designer-skills/releases/latest/download/spike.zip)
- [Download the collection](https://github.com/rodh/designer-skills/releases/latest/download/designer-skills.zip)

Unzip the download and move the skill folders into the appropriate location. Each folder must directly contain its `SKILL.md` and supporting files.

| Agent | One project | All your projects |
| --- | --- | --- |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Codex | `.agents/skills/` | `~/.agents/skills/` |

For example, a global Patchwork install for Claude Code has `~/.claude/skills/patchwork/SKILL.md`. The collection ZIP contains `patchwork/` and `spike/`; move both folders. If a folder is already installed, preserve any local edits before replacing it.

### Updates

For CLI installations, run `npx skills update` and select the installation scope. For manual installations, download the latest ZIP and replace the old skill folder after preserving local edits.

## Use

In Claude Code, invoke `/patchwork` or `/spike`. In Codex, refer to `$patchwork` or `$spike`. Start a fresh conversation if an installed skill is not visible.

**Patchwork:** attach a screenshot of an existing page, then ask:

> Use Patchwork to add appointment booking to this page. Show two options: below the business details and in the sidebar.

**Spike:** open the project you want to investigate, then ask:

> Use Spike to compare two ways of previewing search results: a side panel and an expanded row. Build a small comparison so I can choose before we change the app.

See [example prompts](examples/README.md) for follow-ups and expected outputs.

These are instruction files, not hosted services. Your agent needs access to project files and the ability to create artifacts; viewing HTML output requires a browser. Patchwork's default CSS loads Google Fonts, with local fallback fonts. Spike's dependencies depend on the experiment you request. Agent capabilities and model behavior affect results.

## Maintain the collection

This repository is the source for future skill edits. Edit files under `skills/<name>/`, then reinstall or refresh local copies. Keep screenshots, generated artifacts, and test runs outside those installable folders. Add a new skill by creating its folder with a `SKILL.md` and all resources it references, and update the catalog above.

Validate and build release ZIPs with Python 3.10 or later:

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests
python3 scripts/package.py
```

Packaging writes one ZIP per skill, `designer-skills.zip`, and `SHA256SUMS` to `dist/`. Each ZIP includes the license; generated archives are not committed. CI validates and packages every push and pull request. Pushing a version tag such as `v1.0.1` runs those checks and publishes a GitHub release with the downloads attached.

Before tagging a release, test the changed skill with a realistic request. Packaging checks establish that files are valid and complete; they do not evaluate the agent's output quality.

## License

[MIT](LICENSE). Copyright © 2026 Rod Howard.
