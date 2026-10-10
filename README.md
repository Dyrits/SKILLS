# Skills For Real Engineers

[![skills.sh](https://skills.sh/b/Dyrits/SKILLS)](https://skills.sh/Dyrits/SKILLS)

Agent skills for real engineering.

These skills are small, editable, and composable. Use explicit planning phases or develop a living application in just-in-time increments. Both workflows maintain the same project documents.

## Installation

[skills.sh](https://skills.sh/Dyrits/SKILLS) copies editable skill files into your project across supported agent clients.

```bash
npx skills@latest add Dyrits/SKILLS
```

Pick the skills you want, and which coding agents to install them on. **The installer lets you choose which skills to take: install `setup` first.**

Run `/setup` once per repository, or in an empty project, to configure local or remote task tracking, task-writing conventions, triage roles, commit-time checks, Git guardrails, and AI tooling. It asks which of these you want.

Specifications stay authoritative in the repository. Draft remote tasks remain local until you explicitly publish them; their local files then link to the authoritative tracker records. Agents maintain local documentation autonomously within the authorized scope.

To install with Microsoft APM instead, register the marketplace once, then name a skill. Every skill is its own APM package with its own `apm.yml`, and comes with every skill it references.

```bash
apm marketplace add Dyrits/SKILLS
apm install <name>@dyrits
```

To install all skills for your user account rather than one project (the root `apm.yml` depends on every skill):

```bash
apm install Dyrits/SKILLS --global
```

APM selects the target agent clients from its configuration or auto-detection. Add `--target claude,codex` to select them explicitly. If existing skills cause conflicts, add `--force` only when you intend to replace them. It permits overwriting locally authored files and also bypasses blocking security findings.

Install `setup` first.

### Updating installed skills

For skills installed with skills.sh:

```bash
npx skills@latest update
```

Choose the installation scope when prompted. Add `--global` to update only user-wide skills.

For skills installed globally with APM:

```bash
apm update --global
```

Review the update plan and confirm it. For project installations, run `apm update` from that project instead. Without `--global`, APM checks the project's dependencies, not your user-wide installation.

## Two workflows, shared documents

| Approach | Route |
| --- | --- |
| Planned development | Once per system, `delineate → architect`; then per capability, `specify → engineer → taskify → implement → review-and-refactor`. Skip any step whose result already exists or that small work does not need. |
| Just-in-time development | [iterate](./skills/workflow/iterate/SKILL.md) clarifies, builds, and validates the next useful increment. |

Each skill carries the project-document rules it needs and finds a document through the project's `AGENTS.md`.

To see what each skill reads and writes and which skills it works with, open the [skills page](./index.html) in a browser: every skill has a small graph.

```text
documentation/
├── requirements.md
├── backlog.md
├── work-in-progress.md
├── changelog.md
├── glossary.md
├── conventions.md
├── architecture-decision-record/
└── capabilities/
    └── <capability>/
        ├── requirements.md
        ├── specifications.md
        ├── draft.md
        └── tasks/
```

A capability is anything with lasting agreed behavior: a user-facing feature, an integration, an infrastructure area, or a concern such as security. A bugfix or chore is a task under the capability it changes, not a folder of its own. Folder names are kebab-case glossary terms and stay fixed once referenced; see [architecture decision record 0003](./documentation/architecture-decision-record/0003-group-specifications-by-capability.md).

Create files when useful, not as empty scaffolding. Requirements protect obligations and constraints; specifications describe agreed behavior and design; drafts hold unresolved proposals. The backlog does not authorize implementation. Working state records unfinished work and resumption details. The changelog distinguishes agreement changes from validated deliveries.

With local tracking, `documentation/backlog.md` contains the candidate backlog. With a remote tracker, it contains only a name and link to the authoritative backlog or board. `documentation/work-in-progress.md` stays local in both cases for active execution, verification, and resumption, without duplicating remote task status.

`iterate` primarily uses the backlog, working state, and changelog. It respects existing requirements and specifications without requiring new capability documents or tasks for every batch.

During specification work, a [prototype](./skills/shaping/prototype/SKILL.md) is a scoped experiment you request or approve. Its validated result can feed implementation, including useful code after production checks. Iteration develops the living application directly.

## Design decisions

The decisions behind the skills are recorded in [architecture decision records](./documentation/architecture-decision-record/):

- Both workflows use one set of project-owned documents ([0002](./documentation/architecture-decision-record/0002-share-project-documents-across-workflows.md)), with specifications grouped by capability ([0003](./documentation/architecture-decision-record/0003-group-specifications-by-capability.md)).
- Every skill completes its task when installed alone, and skills connect through project artifacts rather than calls ([0005](./documentation/architecture-decision-record/0005-make-skills-autonomous.md)); the migration is not yet complete.
- The system and each capability are described functionally and technically, by `delineate`, `architect`, `specify`, and `engineer` ([0006](./documentation/architecture-decision-record/0006-describe-systems-and-capabilities-functionally-and-technically.md)).
- One `setup` skill configures a repository, installing tools through their own command-line installers from a dated catalogue ([0007](./documentation/architecture-decision-record/0007-merge-project-setup-into-one-skill.md)).
- Tasks can be local Markdown or native remote issues, and skills are grouped by purpose. Every skill ships in the plugin.

## Plugin skills

The manifest is the source of truth for this list; it holds every skill in the repository. Every skill can be run by you or reached by an agent, and a skill can call any other skill.

### Setup

- [setup](./skills/setup/setup/SKILL.md): Configure a repository or an empty project: task tracking, triage roles, commit-time checks, Git guardrails, and AI tooling.
- [setup-delegation-policy](./skills/setup/setup-delegation-policy/SKILL.md): Install, reconfigure, or remove the delegation and model-tier rule for each agent harness you use.

### Workflow

- [delineate](./skills/workflow/delineate/SKILL.md): Outline the system functionally: purpose, actors, contexts, capabilities, system-wide requirements, and glossary.
- [architect](./skills/workflow/architect/SKILL.md): Decide or assess the system's technical shape: stack, parts, data ownership, integrations, and deployment.
- [specify](./skills/workflow/specify/SKILL.md): Resolve outstanding decisions and maintain a capability's observable behavior, acceptance, and requirements.
- [engineer](./skills/workflow/engineer/SKILL.md): Design one capability's modules, interfaces, data, and test seams inside the architecture.
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
- [interview](./skills/shaping/interview/SKILL.md): Settle decisions through rounds of questions, each with a recommended answer.

### Upkeep

- [triage](./skills/upkeep/triage/SKILL.md): Verify and classify requests, recording actionable briefs or decisions.
- [improve-codebase-architecture](./skills/upkeep/improve-codebase-architecture/SKILL.md): Present deepening opportunities in a visual audit.
- [improve-skills](./skills/upkeep/improve-skills/SKILL.md): Review a session's skill use and report it as an issue on this repository.
- [improve-environment](./skills/upkeep/improve-environment/SKILL.md): Trace a session's friction to the project's environment and fix it there.
- [monitor-ai-tooling](./skills/upkeep/monitor-ai-tooling/SKILL.md): Report observed tool benefits, estimates, and quality gaps.
- [debug](./skills/upkeep/debug/SKILL.md): Build a tight reproduction loop, diagnose the cause, and verify the fix.
- [codify](./skills/upkeep/codify/SKILL.md): Draft the project's code conventions from how its code is written, confirm each rule and its reason, or audit existing conventions.

### Version control

- [work-in-tree](./skills/version-control/work-in-tree/SKILL.md): Carry out work in an isolated checkout with a verified return destination.
- [sync-tree](./skills/version-control/sync-tree/SKILL.md): Transfer committed work to the verified corresponding local branch.
- [rebase](./skills/version-control/rebase/SKILL.md): Rebase local branches with recovery records, checks, and separately approved publication.
- [draft-merge-request](./skills/version-control/draft-merge-request/SKILL.md): Write a request body with a summary visual, before/after evidence, and merge danger.
- [resolve-merge-conflicts](./skills/version-control/resolve-merge-conflicts/SKILL.md): Resolve conflicts by intent and finish the operation.

### Productivity

- [re-explain](./skills/productivity/re-explain/SKILL.md): Re-explain a message with the missing context.
- [teach](./skills/productivity/teach/SKILL.md): Maintain a stateful teaching workspace.
- [design-workflow](./skills/productivity/design-workflow/SKILL.md): Turn recurring work loops into implementable workflow specifications.
- [publish-message](./skills/productivity/publish-message/SKILL.md): Publish established conclusions to any connected service after approval of exact text and destination.
- [hand-off](./skills/productivity/hand-off/SKILL.md): Save a versioned handoff with pointers to authoritative artifacts.
- [illustrate](./skills/productivity/illustrate/SKILL.md): Explain a topic with the smallest useful visual.
- [optimize-process](./skills/productivity/optimize-process/SKILL.md): Improve a recurring process using observed friction.
- [walk-through](./skills/productivity/walk-through/SKILL.md): Generate a guided script for steps only a human can perform.
- [write-for-agents](./skills/productivity/write-for-agents/SKILL.md): Write predictable agent instructions with clear completion criteria.
- [unslop](./skills/productivity/unslop/SKILL.md): Remove filler and recurring AI writing patterns.
- [memorize](./skills/productivity/memorize/SKILL.md): File lessons where the next agent will look, and reuse saved scripts before writing new ones.
- [swarm](./skills/productivity/swarm/SKILL.md): Fan independent pieces of a task out to fast, low-cost agents you select, then merge and spot-check their reports.
