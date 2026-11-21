English · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Español](README.es.md)

<p align="center">
  <img src="assets/pika-ui-logo.png" width="300" alt="Pika UI colorful pickup truck logo">
</p>

<h1 align="center">Pika UI</h1>

<p align="center"><strong>Start with the real task. Design the interface clearly. Build it for the project at hand.</strong></p>

Pika UI is a cross-platform interface design and implementation skill for AI coding agents. It supports the full path from new interfaces and redesigns to screenshot recreation and UI review across web, desktop, mobile, and other software surfaces.

React Bits is an optional source of visual and interaction ideas, not a framework requirement. React projects can evaluate its components when useful; other stacks can adapt the effect to their target platform.

## Installation

### Install from the terminal

Run this from any directory. It installs only the `pika-ui` skill for Codex and makes it available across your projects:

```bash
npx skills add lbxx-13/pika-ui --skill pika-ui -g -a codex
```

This repository is private. The command works when your machine already has access to it through Git credentials, GitHub CLI authentication, or SSH. If prompted, choose the Codex agent and global installation.

### Ask an agent to install it

In an agent that can run terminal commands, send:

```text
Please install the Pika UI skill for Codex by running: npx skills add lbxx-13/pika-ui --skill pika-ui -g -a codex
```

The machine running the agent still needs access to this private GitHub repository. If the CLI cannot authenticate, configure GitHub access first, then rerun the command.

### Update later

```bash
npx skills update pika-ui -g
```

If you installed it by cloning the repository manually instead, update it with:

```bash
git -C ~/.codex/skills/pika-ui pull --ff-only
```

For a custom `CODEX_HOME`, replace `~/.codex` with your Codex home directory.

## Using Pika UI

Start a new Codex turn after installation. Invoke the skill explicitly with `$pika-ui`, or describe the task in plain language and ask Codex to use Pika UI. Give it the project, screenshot, brand assets, and constraints that matter; it will inspect the existing stack and load only the relevant guides.

## What you can do

- **Design a new interface:** Set a clear visual direction and implement a product page, workspace, mobile view, or component.
- **Refresh an existing interface:** Understand the project's pages, design tokens, shared components, and interactions before changing them.
- **Recreate a reference:** Rebuild layout, proportions, type, color, and hierarchy, then inspect the result at the target viewport.
- **Compare directions:** When requested, create up to three genuinely distinct candidates and view them side by side in the local comparison page.
- **Review an experience:** Check hierarchy, responsive layouts, interaction states, keyboard access, and reduced-motion behavior.
- **Explore motion and media:** Use React Bits as an optional component reference, or choose suitable imagery, icons, and motion for the page.

## Example prompts

```text
$pika-ui Design a previewable landing page for this course-booking product. Choose a direction based on its audience and course content, then build desktop and mobile layouts.
```

```text
Use Pika UI to recreate this screenshot. First inspect the project's framework and styling conventions, then implement the page and check its narrow layout.
```

```text
Review this page with Pika UI. Report only issues supported by screenshot or code evidence, suggest concrete fixes, and leave the files untouched.
```

## Workflow

1. **Understand the context:** Identify the audience, primary task, device, existing interface, and project stack.
2. **Make design decisions:** Define the focal point, primary action, visual direction, type and color, key imagery, and important states.
3. **Build for the project:** Follow its existing components, design tokens, dependencies, and platform conventions.
4. **Inspect the real interface:** Check the target viewport, important states, and primary actions; refine the result and remove unnecessary detail.

Load references only when the task needs them. Small, explicit changes can be handled directly without the full direction-setting process.

## Guide map

| Task | Guide |
| --- | --- |
| New interface, redesign, and implementation | [`references/design-workflow.md`](references/design-workflow.md) |
| Visual direction and concept exploration | [`references/design-direction.md`](references/design-direction.md), [`references/task-explore.md`](references/task-explore.md) |
| Marketing, brand, and launch pages | [`references/direction-persuasion.md`](references/direction-persuasion.md) |
| Screenshot recreation, layout, and viewport | [`references/layout-and-viewport.md`](references/layout-and-viewport.md) |
| Type, color, surfaces, and hierarchy | [`references/visual-language.md`](references/visual-language.md) |
| Design tokens and system maintenance | [`references/design-system.md`](references/design-system.md) |
| Forms, dialogs, and complex states | [`references/interaction-states.md`](references/interaction-states.md) |
| Motion and reduced-motion behavior | [`references/motion.md`](references/motion.md) |
| Images, icons, and media sources | [`references/media.md`](references/media.md) |
| UX flow walkthrough | [`references/ux-review.md`](references/ux-review.md) |
| Read-only UI review | [`references/task-review.md`](references/task-review.md), [`references/review-checklist.md`](references/review-checklist.md) |
| Candidate comparison | [`references/style-explorer.md`](references/style-explorer.md) |
| Browsers and development tools | [`references/tools.md`](references/tools.md) |

### How React Bits fits

[React Bits](https://reactbits.dev/) offers text animations, backgrounds, components, and micro-interactions. Pika UI treats it as an optional source of visual and interaction ideas. Before using or adapting an example, read [`references/react-bits.md`](references/react-bits.md). Its React source components should be integrated directly only when the target project uses React and the fit makes sense; other platforms can adapt the interaction intent and visual effect.

## Repository layout

```text
SKILL.md                          Skill entry point and task routing
references/                       Design, implementation, and review guides
assets/style-explorer.html        Local candidate comparison page
assets/pika-ui-logo.png           Pika UI pickup truck logo
scripts/create_style_explorer.py  Script for creating comparison-page links
```

The comparison page is for viewing candidates that already exist. It does not replace design exploration or generate concepts on its own.

## Design boundaries

- Follow the project's real brand, stack, components, and platform conventions instead of forcing a fixed style.
- Use product facts supplied by the project or verified elsewhere; do not invent metrics, testimonials, or feature claims.
- React Bits is neither a cross-platform component library nor the only source of components. Adapt ideas to the target stack.
- Review visual design, interaction, and functionality separately. State what has not been verified when the interface has not been run.

