# Skills For Real Engineers

[![skills.sh](https://skills.sh/b/Dyrits/SKILLS)](https://skills.sh/Dyrits/SKILLS)

Agent skills for real engineering, maintained as an independent fork.

These skills are small, editable, and composable. Use explicit planning phases or develop a living application in just-in-time increments. Both workflows maintain the same project documents.

## Installation

[skills.sh](https://skills.sh/Dyrits/SKILLS) copies editable skill files into your project across supported agent clients.

```bash
npx skills@latest add Dyrits/SKILLS
```

Pick the skills you want, and which coding agents to install them on. **The installer lets you choose which skills to take: make sure `setup-ai-workspace` and `document` are among them, since most workflows rely on `document`.**

Run `/setup-ai-workspace` once per repository to configure local or remote task tracking, task-writing conventions, triage roles, domain documentation, and the optional setups (tooling, commit hooks, Git guardrails, automatic handoff, delegation policy).

Specifications stay authoritative in the repository. Draft remote tasks remain local until you explicitly publish them; their local files then link to the authoritative tracker records. Agents maintain local documentation autonomously within the authorized scope.

## Two workflows, shared documents

| Approach | Route |
| --- | --- |
| Planned development | `specify → taskify → implement → review-and-refactor`; skip decomposition for small work that does not need separate tasks. |
| Just-in-time development | [iterate](./skills/workflow/iterate/SKILL.md) clarifies, builds, and validates the next useful increment. |

The [document](./skills/reference/document/SKILL.md) skill owns the [shared project-document rules](./skills/reference/document/PROJECT-DOCUMENTS.md).

To see what each skill reads and writes and which skills it works with, open the [skills page](./index.html) in a browser: every skill has a small graph.

```text
CHANGELOG.md
documentation/
├── requirements.md
├── backlog.md
├── work-in-progress.md
└── capabilities/
    └── <capability>/
        ├── requirements.md
        ├── specifications.md
        ├── draft.md
        └── tasks/
```

A capability is anything with lasting agreed behavior: a user-facing feature, an integration, an infrastructure area, or a concern such as security. A bugfix or chore is a task under the capability it changes, not a folder of its own. Folder names are kebab-case glossary terms and stay fixed once referenced; see [architecture decision record 0003](./documentation/architecture-decision-record/0003-group-specifications-by-capability.md).

Create files when useful, not as empty scaffolding. Requirements protect obligations and constraints; specifications describe agreed behavior and design; drafts hold unresolved proposals. The backlog does not authorize implementation. Working state records unfinished work and resumption details. Root `CHANGELOG.md` distinguishes agreement changes from validated deliveries.

With local tracking, `documentation/backlog.md` contains the candidate backlog. With a remote tracker, it contains only a name and link to the authoritative backlog or board. `documentation/work-in-progress.md` stays local in both cases for active execution, verification, and resumption, without duplicating remote task status.

`iterate` primarily uses the backlog, working state, and changelog. It respects existing requirements and specifications without requiring new capability documents or tasks for every batch.

During specification work, a [prototype](./skills/shaping/prototype/SKILL.md) is a scoped experiment you request or approve. Its validated result can feed implementation, including useful code after production checks. Iteration develops the living application directly.

## Why this fork exists

This repository forked from [Matt Pocock's skills](https://aihero.dev/skills) at a known commit and diverges deliberately. The upstream website does not document this fork's behavior. See [architecture decision record 0001](./documentation/architecture-decision-record/0001-maintain-as-an-independent-fork.md) and the [upstream archive index](./.upstream/README.md).

Not every retained skill comes from that upstream repository. The [primary-source provenance audit](./documentation/research/2026-10-03-retained-skill-provenance.md) traces the 47 skills retained on that date: 29 Matt-derived, three other external adaptations, and 15 created in this fork. [improve-environment](./skills/upkeep/improve-environment/SKILL.md), added later, ports upstream `retro`. Original names and sources are identified on promoted skill pages. Removed upstream skills remain absent; the archive is evidence, not an install inventory.

- Tasks can be local Markdown or native remote issues.
- Both workflows use project-owned documents rather than separate artifact systems.
- Skills are grouped by purpose. Every skill outside `deprecated/` ships in the plugin.
- Upstream changes are adopted deliberately. Historical names remain in provenance notes, not as active aliases.

### Intentional workflow drift

| Upstream skill or split | Current form | Why it differs |
| --- | --- | --- |
| `grill-me` wrapper and `grilling` primitive | [refine](./skills/reference/refine/SKILL.md) | One general interview skill is reachable by both people and agents; the duplicate wrapper adds no discipline. |
| `grill-with-docs`, then `to-spec` | [specify](./skills/workflow/specify/SKILL.md) | Clarification and recording belong to one selected-scope operation. Already settled context goes straight to synthesis. |
| `to-tickets` | [taskify](./skills/workflow/taskify/SKILL.md) | Task is a tracker-neutral word for delivery, investigation, enabling, or maintenance work. |
| `wait-what` | [re-explain](./skills/productivity/re-explain/SKILL.md) | The name describes the requested action while retaining the context-aware explanation discipline. |
| `wayfinder` | [graphify](./skills/shaping/graphify/SKILL.md) | The name emphasizes the decision graph; tracker labels use the `graphify:` prefix. |
| `tdd` | [test-first](./skills/workflow/test-first/SKILL.md) | Skill names read as commands; the description keeps the TDD and red-green-refactor triggers. |
| `codebase-design` | [design-modules](./skills/reference/design-modules/SKILL.md) | The name reads as a command and leads with the skill's subject, deep modules. |
| `domain-modeling` | [model-domain](./skills/reference/model-domain/SKILL.md) | The name reads as a command; the discipline is unchanged. |
| `wizard` | [walk-through](./skills/productivity/walk-through/SKILL.md) | The name describes the action; the script it produces is still called a wizard. |
| HumanLayer's `show-me` | [illustrate](./skills/productivity/illustrate/SKILL.md) | The name describes the visual explanation action without changing the external source or delivery discipline. |
| Separate planning snapshots and iterative working records | Shared project documents | Switching development approaches should not duplicate or discard obligations, agreements, or progress. |
| Prototype code retained only outside the application | Approved experiment with a productionization path | Validation should preserve useful work; experimental success does not itself establish production readiness. |
| `retro` | [improve-environment](./skills/upkeep/improve-environment/SKILL.md) and [improve-skills](./skills/upkeep/improve-skills/SKILL.md) | One retrospective changes the project's environment after agreeing each change with you; the other reports how the skills behaved as an issue on this repository. Written project lessons go through [memorize](./skills/reference/memorize/SKILL.md). |

`iterate` is a fork-specific just-in-time workflow, not an upstream rename. Skills formerly under `experimental/` now live in purpose buckets and ship in the plugin. Human-facing pages identify verified original names or an explicit fork-specific origin. See [architecture decision record 0002](./documentation/architecture-decision-record/0002-share-project-documents-across-workflows.md) for the document-authority decision.

## Plugin skills

The manifest is the source of truth for this list; it holds every skill outside `deprecated/`. Every skill can be run by you or reached by an agent, and a skill can call any other skill.

### Setup

- [setup-ai-workspace](./skills/setup/setup-ai-workspace/SKILL.md): Configure project documents, task tracking, triage roles, and the optional setups.
- [setup-delegation-policy](./skills/setup/setup-delegation-policy/SKILL.md): Configure machine-wide delegation and model-tier rules.
- [setup-ai-tooling](./skills/setup/setup-ai-tooling/SKILL.md): Configure and verify selected development tools and their measurement baseline.
- [setup-git-hooks](./skills/setup/setup-git-hooks/SKILL.md): Configure versioned commit hooks with formatting, linting, typechecking, and builds.
- [setup-git-guardrails](./skills/setup/setup-git-guardrails/SKILL.md): Ask before destructive Git commands with client permissions and hooks.

### Workflow

- [specify](./skills/workflow/specify/SKILL.md): Resolve outstanding decisions and maintain capability requirements and specifications.
- [taskify](./skills/workflow/taskify/SKILL.md): Decompose work into tasks with acceptance criteria and dependencies.
- [implement](./skills/workflow/implement/SKILL.md): Build authorized work, validate it, review it, and maintain project documents.
- [divide-and-conquer](./skills/workflow/divide-and-conquer/SKILL.md): Route each task to the least expensive capable agent, build a task graph in parallel on one integration branch, then review once.
- [test-first](./skills/workflow/test-first/SKILL.md): Establish behavior through red/green, one vertical slice at a time.
- [review-and-refactor](./skills/workflow/review-and-refactor/SKILL.md): Independently review Standards and Specifications, refactor, and verify.
- [iterate](./skills/workflow/iterate/SKILL.md): Develop the living application just in time, maintaining backlog, working state, and root changelog.
- [address-feedback](./skills/workflow/address-feedback/SKILL.md): Assess review feedback from any source, implement approved changes, and deliver approved replies.

### Shaping

- [graphify](./skills/shaping/graphify/SKILL.md): Map a large uncertain effort and resolve its decision tasks.
- [research](./skills/shaping/research/SKILL.md): Investigate primary sources and save cited findings.
- [prototype](./skills/shaping/prototype/SKILL.md): Settle a design question with a scoped experiment and validate before integration.
- [prioritize](./skills/shaping/prioritize/SKILL.md): Organize candidate outcomes and agree on one focus, keeping the rest in the backlog.

### Upkeep

- [triage](./skills/upkeep/triage/SKILL.md): Verify and classify requests, recording actionable briefs or decisions.
- [improve-codebase-architecture](./skills/upkeep/improve-codebase-architecture/SKILL.md): Present deepening opportunities in a visual audit.
- [improve-skills](./skills/upkeep/improve-skills/SKILL.md): Review a session's skill use and report it as an issue on this repository.
- [improve-environment](./skills/upkeep/improve-environment/SKILL.md): Trace a session's friction to the project's environment and fix it there.
- [monitor-ai-tooling](./skills/upkeep/monitor-ai-tooling/SKILL.md): Report observed tool benefits, estimates, and quality gaps.
- [debug](./skills/upkeep/debug/SKILL.md): Build a tight reproduction loop, diagnose the cause, and verify the fix.

### Version control

- [work-in-tree](./skills/version-control/work-in-tree/SKILL.md): Carry out work in an isolated checkout with a verified return destination.
- [sync-tree](./skills/version-control/sync-tree/SKILL.md): Transfer committed work to the verified corresponding local branch.
- [rebase](./skills/version-control/rebase/SKILL.md): Rebase local branches with recovery records, checks, and separately approved publication.
- [draft-merge-request](./skills/version-control/draft-merge-request/SKILL.md): Write a request body with a summary visual, before/after evidence, and merge danger.
- [resolve-merge-conflicts](./skills/version-control/resolve-merge-conflicts/SKILL.md): Resolve conflicts by intent and finish the operation.

### Productivity

- [guide](./skills/productivity/guide/SKILL.md): Choose the next skill, workflow, or session boundary.
- [ask-someone-else](./skills/productivity/ask-someone-else/SKILL.md): Write a questionnaire for the person who holds missing knowledge.
- [re-explain](./skills/productivity/re-explain/SKILL.md): Re-explain a message with the missing context.
- [take-over](./skills/productivity/take-over/SKILL.md): Resume from the latest handoff and its primary sources.
- [teach](./skills/productivity/teach/SKILL.md): Maintain a stateful teaching workspace.
- [design-workflow](./skills/productivity/design-workflow/SKILL.md): Turn recurring work loops into implementable workflow specifications.
- [publish-message](./skills/productivity/publish-message/SKILL.md): Publish established conclusions to any connected service after approval of exact text and destination.
- [hand-off](./skills/productivity/hand-off/SKILL.md): Save a versioned handoff with pointers to authoritative artifacts.
- [illustrate](./skills/productivity/illustrate/SKILL.md): Explain a topic with the smallest useful visual.
- [optimize-process](./skills/productivity/optimize-process/SKILL.md): Improve a recurring process using observed friction.
- [walk-through](./skills/productivity/walk-through/SKILL.md): Generate a guided script for steps only a human can perform.
- [classify](./skills/productivity/classify/SKILL.md): Classify safe-to-send text with classifier.dev and retain uncertain results.

### Reference

Disciplines other skills call; each can also be run directly by you or an agent.

- [refine](./skills/reference/refine/SKILL.md): Resolve decisions through recommended questions in dependency-aware rounds.
- [model-domain](./skills/reference/model-domain/SKILL.md): Maintain domain vocabulary, consequential decisions, and domain-agnostic code conventions.
- [design-modules](./skills/reference/design-modules/SKILL.md): Design deep modules with clear interfaces and useful seams.
- [document](./skills/reference/document/SKILL.md): Maintain technical documentation and shared project-document rules.
- [write-for-agents](./skills/reference/write-for-agents/SKILL.md): Write predictable agent instructions with clear completion criteria.
- [unslop](./skills/reference/unslop/SKILL.md): Remove filler and recurring AI writing patterns.
- [memorize](./skills/reference/memorize/SKILL.md): File lessons where the next agent will look, and reuse saved scripts before writing new ones.

## Credits

- [illustrate](./skills/productivity/illustrate/SKILL.md) adapts [Dex Horthy](https://github.com/dexhorthy)'s original [`show-me` skill from HumanLayer](https://github.com/humanlayer/skills/tree/main/plugins/show-me/skills/show-me).
- [draft-merge-request](./skills/version-control/draft-merge-request/SKILL.md) came from [`mattpocock/skills`](https://github.com/mattpocock/skills), where it was named `pr`; its summary visual guidance comes from HumanLayer's original `show-me`, now [illustrate](./skills/productivity/illustrate/SKILL.md) in this fork.
- [unslop](./skills/reference/unslop/SKILL.md) adapts the [`unslop` skill in Cursor's `pstack` plugin](https://github.com/cursor/plugins/tree/main/pstack/skills/unslop).
- [document](./skills/reference/document/SKILL.md) adapts [Anthropic's `documentation` skill](https://github.com/anthropics/knowledge-work-plugins/blob/1bd42820da111e5f0206e570bf5228a1c35839c7/engineering/skills/documentation/SKILL.md), extended here with the shared project-document model.
