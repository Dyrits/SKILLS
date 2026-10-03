# Skills For Real Engineers

[![skills.sh](https://skills.sh/b/Dyrits/SKILLS)](https://skills.sh/Dyrits/SKILLS)

Agent skills for real engineering, maintained as an independent fork.

These skills are small, editable, and composable. Use explicit planning phases or develop a living application in just-in-time increments. Both workflows maintain the same project documents.

## Installation

[skills.sh](https://skills.sh/Dyrits/SKILLS) copies editable skill files into your project across supported agent clients.

```bash
npx skills@latest add Dyrits/SKILLS
```

Pick the skills you want, and which coding agents to install them on. **The installer lets you choose which skills to take: make sure `setup-ai-workspace` is one of them.**

Run `/setup-ai-workspace` once per repository to configure local or remote task tracking, task-writing conventions, triage roles, domain documentation, and optional tooling.

Specifications stay authoritative in the repository. Draft remote tasks remain local until you explicitly publish them; their local files then link to the authoritative tracker records. Agents maintain local documentation autonomously within the authorized scope.

## Two workflows, shared documents

| Approach | Route |
| --- | --- |
| Planned development | `specify → taskify → implement → code-review-and-refactor`; skip decomposition for small work that does not need separate tasks. |
| Just-in-time development | [iterate](./skills/workflow/iterate/SKILL.md), installed separately from the plugin, clarifies, builds, and validates the next useful increment. |

The [documentation](./skills/reference/documentation/SKILL.md) skill owns the [shared project-document rules](./skills/reference/documentation/PROJECT-DOCUMENTS.md).

```text
CHANGELOG.md
documentation/
├── requirements.md
├── backlog.md
├── work-in-progress.md
└── <feature>/
    ├── requirements.md
    ├── specifications.md
    ├── draft.md
    └── tasks/
```

Create files when useful, not as empty scaffolding. Requirements protect obligations and constraints; specifications describe agreed behavior and design; drafts hold unresolved proposals. The backlog does not authorize implementation. Working state records unfinished work and resumption details. Root `CHANGELOG.md` distinguishes agreement changes from validated deliveries.

With local tracking, `documentation/backlog.md` contains the candidate backlog. With a remote tracker, it contains only a name and link to the authoritative backlog or board. `documentation/work-in-progress.md` stays local in both cases for active execution, verification, and resumption, without duplicating remote task status.

`iterate` primarily uses the backlog, working state, and changelog. It respects existing requirements and specifications without requiring new feature documents or tasks for every batch.

During specification work, a [prototype](./skills/shaping/prototype/SKILL.md) is a scoped experiment you request or approve. Its validated result can feed implementation, including useful code after production checks. Iteration develops the living application directly.

## Why this fork exists

This repository forked from [Matt Pocock's skills](https://aihero.dev/skills) at a known commit and diverges deliberately. The upstream website does not document this fork's behavior. See [architecture decision record 0001](./documentation/architecture-decision-record/0001-maintain-as-an-independent-fork.md) and the [upstream archive index](./.upstream/README.md).

Not every retained skill comes from that upstream repository. The [primary-source provenance audit](./documentation/research/2026-10-03-retained-skill-provenance.md) traces all 47 retained skills: 29 Matt-derived, three other external adaptations, and 15 created in this fork. Original names and sources are identified on promoted skill pages. Removed upstream skills remain absent; the archive is evidence, not an install inventory.

- Tasks can be local Markdown or native remote issues.
- Both workflows use project-owned documents rather than separate artifact systems.
- Skills are grouped by purpose, not publication status. Moving a skill does not promote it.
- Upstream changes are adopted deliberately. Historical names remain in provenance notes, not as active aliases.

### Intentional workflow drift

| Upstream skill or split | Current form | Why it differs |
| --- | --- | --- |
| `grill-me` wrapper and `grilling` primitive | [refine](./skills/reference/refine/SKILL.md) | One general interview skill is reachable by both people and agents; the duplicate wrapper adds no discipline. |
| `grill-with-docs`, then `to-spec` | [specify](./skills/workflow/specify/SKILL.md) | Clarification and recording belong to one selected-scope operation. Already settled context goes straight to synthesis. |
| `to-tickets` | [taskify](./skills/workflow/taskify/SKILL.md) | Task is a tracker-neutral word for delivery, investigation, enabling, or maintenance work. |
| `wait-what` | [re-explain](./skills/productivity/re-explain/SKILL.md) | The name describes the requested action while retaining the context-aware explanation discipline. |
| `wayfinder` | [graphify](./skills/shaping/graphify/SKILL.md) | The name emphasizes the decision graph; native tracker labels remain compatible with existing records. |
| HumanLayer's `show-me` | [illustrate](./skills/productivity/illustrate/SKILL.md) | The name describes the visual explanation action without changing the external source or delivery discipline. |
| Separate planning snapshots and iterative working records | Shared project documents | Switching development approaches should not duplicate or discard obligations, agreements, or progress. |
| Prototype code retained only outside the application | Approved experiment with a productionization path | Validation should preserve useful work; experimental success does not itself establish production readiness. |

`iterate` is a fork-specific just-in-time workflow, not an upstream rename. Skills formerly under `experimental/` now live in purpose buckets and keep their individual plugin status. Human-facing pages identify verified original names or an explicit fork-specific origin. See [architecture decision record 0002](./documentation/architecture-decision-record/0002-share-project-documents-across-workflows.md) for the document-authority decision.

## Plugin skills

The manifest is the source of truth for this list. **User-invoked** skills run only when you ask; **model-invoked** skills can also be reached automatically. A skill can call model-invoked skills, not user-only workflows.

### Getting started

- [setup-ai-workspace](./skills/getting-started/setup-ai-workspace/SKILL.md): Configure project documents, task tracking, triage roles, and optional tooling. User-invoked.
- [what-is-next](./skills/getting-started/what-is-next/SKILL.md): Choose the next skill, workflow, or session boundary. User-invoked.

### Workflow

#### User-invoked

- [specify](./skills/workflow/specify/SKILL.md): Resolve outstanding decisions and maintain feature requirements and specifications.
- [taskify](./skills/workflow/taskify/SKILL.md): Decompose work into tasks with acceptance criteria and dependencies.
- [implement](./skills/workflow/implement/SKILL.md): Build authorized work, validate it, review it, and maintain project documents.
- [implement-all](./skills/workflow/implement-all/SKILL.md): Implement a task graph on one integration branch, with concurrent work and an optional request.
- [design-workflow](./skills/workflow/design-workflow/SKILL.md): Turn recurring work loops into implementable workflow specifications.

#### Model-invoked

- [test-driven-development](./skills/workflow/test-driven-development/SKILL.md): Establish behavior through red/green, one vertical slice at a time.
- [code-review-and-refactor](./skills/workflow/code-review-and-refactor/SKILL.md): Independently review Standards and Specifications, refactor, and verify.
- [to-pull-request](./skills/workflow/to-pull-request/SKILL.md): Write a request body with a summary visual, before/after evidence, and merge danger.

### Shaping

#### User-invoked

- [graphify](./skills/shaping/graphify/SKILL.md): Map a large uncertain effort and resolve its decision tasks.

#### Model-invoked

- [research](./skills/shaping/research/SKILL.md): Investigate primary sources and save cited findings.
- [prototype](./skills/shaping/prototype/SKILL.md): Settle a design question with a scoped experiment and validate before integration.

### Upkeep

#### User-invoked

- [triage](./skills/upkeep/triage/SKILL.md): Verify and classify requests, recording actionable briefs or decisions.
- [improve-codebase-architecture](./skills/upkeep/improve-codebase-architecture/SKILL.md): Present deepening opportunities in a visual audit.
- [improve-agent-environment](./skills/upkeep/improve-agent-environment/SKILL.md): Suggest improvements based on session evidence.

#### Model-invoked

- [debug](./skills/upkeep/debug/SKILL.md): Build a tight reproduction loop, diagnose the cause, and verify the fix.
- [resolve-merge-conflicts](./skills/upkeep/resolve-merge-conflicts/SKILL.md): Resolve conflicts by intent and finish the operation.

### Productivity

#### User-invoked

- [ask-someone-else](./skills/productivity/ask-someone-else/SKILL.md): Write a questionnaire for the person who holds missing knowledge.
- [re-explain](./skills/productivity/re-explain/SKILL.md): Re-explain a message with the missing context.
- [hand-off](./skills/productivity/hand-off/SKILL.md): Save a versioned handoff with pointers to authoritative artifacts.
- [take-over](./skills/productivity/take-over/SKILL.md): Resume from the latest handoff and its primary sources.
- [teach](./skills/productivity/teach/SKILL.md): Maintain a stateful teaching workspace.

#### Model-invoked

- [illustrate](./skills/productivity/illustrate/SKILL.md): Explain a topic with the smallest useful visual.
- [optimize-process](./skills/productivity/optimize-process/SKILL.md): Improve a recurring process using observed friction.

### Reference

All promoted reference skills are model- or user-reachable.

- [refine](./skills/reference/refine/SKILL.md): Resolve decisions through recommended questions in dependency-aware rounds.
- [domain-modeling](./skills/reference/domain-modeling/SKILL.md): Maintain domain vocabulary, consequential decisions, and guidelines.
- [codebase-design](./skills/reference/codebase-design/SKILL.md): Design deep modules with clear interfaces and useful seams.
- [documentation](./skills/reference/documentation/SKILL.md): Maintain technical documentation and shared project-document rules.
- [writing-for-agents](./skills/reference/writing-for-agents/SKILL.md): Write predictable agent instructions with clear completion criteria.
- [wizard](./skills/reference/wizard/SKILL.md): Generate a guided script for steps only a human can perform.
- [unslop](./skills/reference/unslop/SKILL.md): Remove filler and recurring AI writing patterns.

## Separately installed skills

Skills outside the plugin remain in their purpose buckets. Each bucket's **Not in the plugin** section lists them:

- [Getting started](./skills/getting-started/README.md#not-in-the-plugin): tooling, delegation policy, Git hooks/guardrails, and compaction handoff setup.
- [Workflow](./skills/workflow/README.md#not-in-the-plugin): iteration, feedback/publication, and Git worktree/branch workflows.
- [Shaping](./skills/shaping/README.md#not-in-the-plugin): outcome decomposition.
- [Upkeep](./skills/upkeep/README.md#not-in-the-plugin): tooling measurement reports.
- [Reference](./skills/reference/README.md#not-in-the-plugin): classification and script reuse.

## Credits

- [illustrate](./skills/productivity/illustrate/SKILL.md) adapts [Dex Horthy](https://github.com/dexhorthy)'s original [`show-me` skill from HumanLayer](https://github.com/humanlayer/skills/tree/main/plugins/show-me/skills/show-me).
- [to-pull-request](./skills/workflow/to-pull-request/SKILL.md) came from [`mattpocock/skills`](https://github.com/mattpocock/skills), where it was named `pr`; its summary visual guidance comes from HumanLayer's original `show-me`, now [illustrate](./skills/productivity/illustrate/SKILL.md) in this fork.
- [unslop](./skills/reference/unslop/SKILL.md) adapts the [`unslop` skill in Cursor's `pstack` plugin](https://github.com/cursor/plugins/tree/main/pstack/skills/unslop).
- [documentation](./skills/reference/documentation/SKILL.md) adapts [Anthropic's `documentation` skill](https://github.com/anthropics/knowledge-work-plugins/blob/1bd42820da111e5f0206e570bf5228a1c35839c7/engineering/skills/documentation/SKILL.md), extended here with the shared project-document model.
