# Skills For Real Engineers

[![skills.sh](https://skills.sh/b/Dyrits/SKILLS)](https://skills.sh/Dyrits/SKILLS)

Agent skills for real engineering, maintained as an independent fork.

Developing real applications is hard. Approaches like GSD, BMAD, and Specification-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve.

These skills are designed to be small, easy to adapt, and composable. They work with any model.

## Installation (30-second setup)

One way in: [skills.sh](https://skills.sh/Dyrits/SKILLS) copies editable skill files into your project, so you can hack on them and make them your own.

### 1. Get the skills

```bash
npx skills@latest add Dyrits/SKILLS
```

Pick the skills you want, and which coding agents to install them on. **The installer lets you choose which skills to take, so make sure `setup-custom-skills` is one of them.**

It writes the skills into your repository as ordinary files you own and can edit. Nothing updates behind your back; pull the latest changes when you want them with `npx skills update`.

### 2. Run `/setup-custom-skills`

In your agent, run it once per repository. It will:

- Ask where published issues live: local markdown under `backlog/`, or a remote tracker (GitHub, GitLab, Jira, or another workflow you describe)
- Ask whether tickets should follow an existing repository template or ticket-writing skill
- Ask what strings you use for the triage roles (`/triage` reads them)
- Ask where you want to save any documentation we create

Whichever tracker you pick, drafting happens in `.refinement/` and reaches the tracker only when you ask to publish.

### 3. Bam - you're ready to go.

## Why This Fork Exists

This repository forked from [Matt Pocock's skills](https://aihero.dev/skills) at a known commit, and diverges deliberately rather than tracking upstream, so that site does not document this repository's behavior. Upstream's naming, layout, and publication flow reflect its author's own needs; this fork reshapes them for sustained use inside a working engineering team. The full reasoning lives in [architecture decision record 0001](./documentation/architecture-decision-record/0001-maintain-as-an-independent-fork.md); the concrete differences:

- **Tracker flexibility**: drafting happens in a local `.refinement/` workspace and reaches GitHub, GitLab, Jira, or plain markdown under `backlog/`, whichever you choose at setup, instead of assuming GitHub issues.
- **Semantic bucket layout**: skills sit in `workflow/`, `shaping/`, `upkeep/`, `productivity/`, and `reference/`, so the idea-to-ship spine is readable from the directory tree.
- **An experimental layer**: skills that post to pull requests, issues, or Jira (`address-feedback`, `publish-message`, `publish-review`) and the delegation and model routing policy install deliberately, not by default.
- **No site coupling**: documentation lives in this repository, published through `skills.sh`; nothing depends on the upstream website.
- **Deliberate porting**: upstream history stays reachable, but adopting an upstream change is a separate, deliberate port into this fork's structure. Deciding something is not worth porting is a normal outcome.

The core skills keep upstream's intent: grilling sessions to close the alignment gap, a shared language to cut verbosity, red-green-refactor feedback loops, and daily investment in module design. What changed is the packaging around them.

## Reference

These split on one axis: who can invoke them. **User-invoked** skills are reachable only when you type them (e.g. `/grill-me`); their job is to orchestrate. **Model-invoked** skills can be invoked by you _or_ reached for automatically by the agent when the task fits; they hold the reusable discipline. A user-invoked skill may invoke model-invoked skills, but never another user-invoked one.

### Getting Started

Set up once, then find your way around.

- **[setup-custom-skills](./skills/getting-started/setup-custom-skills/SKILL.md)**: Configure this repository for the workflow skills (issue tracker: local markdown or remote, ticket-writing convention, triage roles, domain documentation layout). Run once per repository.
- **[what-is-next](./skills/getting-started/what-is-next/SKILL.md)**: The router: which skill or flow fits your situation, or which boundary option (continue, clear, hand-off, compact) fits the moment.

### Workflow

The idea→ship spine, in order.

- **[grill-with-documentation](./skills/workflow/grill-with-documentation/SKILL.md)**: Grilling session that also builds your project's domain model, sharpening terminology and updating `CONTEXT.md` and architecture decision records inline.
- **[design-workflow](./skills/workflow/design-workflow/SKILL.md)**: Grilling session that turns the recurring loops in your work into implementable workflow specifications, using the current directory as a stateful workspace.
- **[to-specifications](./skills/workflow/to-specifications/SKILL.md)**: Turn the current conversation into a local draft specification, or publish it to the issue tracker when requested. No interview, just synthesizes what you've already discussed.
- **[to-tickets](./skills/workflow/to-tickets/SKILL.md)**: Break any plan, specification, or conversation into a set of tracer-bullet tickets, each declaring its blocking edges, written as text in a local file, or as native blocking links on a real tracker.
- **[implement](./skills/workflow/implement/SKILL.md)**: Build the work described by a specification or set of tickets, driving `/test-driven-development` at pre-agreed seams and closing out with `/code-review` before committing.
- **[implement-all](./skills/workflow/implement-all/SKILL.md)**: Implement a whole specification on one branch: works the tickets as a task graph, running implementer subagents across the ready frontier for concurrency, landing a single PR.
- **[test-driven-development](./skills/workflow/test-driven-development/SKILL.md)**: Test-driven development with a red-green-refactor loop. Builds features or fixes bugs one vertical slice at a time.
- **[code-review](./skills/workflow/code-review/SKILL.md)**: Two-axis review of the diff since a fixed point: **Standards** (does it follow the repository's coding standards, plus a Fowler smell baseline?) and **Specification** (does it faithfully implement the originating issue/specification?), run as parallel sub-agents so neither pollutes the other.
- **[to-pull-request](./skills/workflow/to-pull-request/SKILL.md)**: Write the body of a pull request or merge request so a reviewer can read the change without reading the diff: one summary visual sized to the point, before/after evidence, and the merge danger (one-way or two-way door, and the blast radius).

### Shaping

Explore an open question and produce a decision or answer that feeds the flow.

- **[wayfinder](./skills/shaping/wayfinder/SKILL.md)**: Plan a huge chunk of work, more than one agent session can hold, as a shared map of decision tickets on the issue tracker, and resolve them one at a time until the way to the destination is clear.
- **[research](./skills/shaping/research/SKILL.md)**: Investigate a question against high-trust primary sources and capture the findings as a cited Markdown file in the repository, run as a background agent.
- **[prototype](./skills/shaping/prototype/SKILL.md)**: Build a throwaway prototype to answer a design question, either a single shareable HTML file for state/logic questions, or several radically different UI variations toggleable from one route.

### Upkeep

Keep the codebase and issue list healthy; generates work for the flow.

- **[triage](./skills/upkeep/triage/SKILL.md)**: Move issues through a state machine of triage roles.
- **[debug](./skills/upkeep/debug/SKILL.md)**: Disciplined diagnosis loop for hard bugs and performance regressions: build a feedback loop that goes red on this bug → minimise → hypothesise → instrument → fix → regression-test.
- **[improve-codebase-architecture](./skills/upkeep/improve-codebase-architecture/SKILL.md)**: Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
- **[resolve-merge-conflicts](./skills/upkeep/resolve-merge-conflicts/SKILL.md)**: Work through an in-progress git merge or rebase conflict hunk by hunk, resolving by intent traced to each side's primary source, then finish the operation (never `--abort`).

### Productivity

Human-facing workflows you run, not about code.

- **[grill-me](./skills/productivity/grill-me/SKILL.md)**: Get relentlessly interviewed about a plan or design until every branch of the design tree is resolved.
- **[ask-someone-else](./skills/productivity/ask-someone-else/SKILL.md)**: Turn a decision you can't answer alone into a Markdown questionnaire for the one person who can, filled in async, or together over a meeting. It grills you about the send (who it's for, what you need back), not the subject.
- **[wait-what](./skills/productivity/wait-what/SKILL.md)**: Fire this the moment a message doesn't land. The agent re-pitches it with the context you were missing, in plain English, using your `CONTEXT.md` vocabulary.
- **[hand-off](./skills/productivity/hand-off/SKILL.md)**: Compact the current conversation into a versioned handoff document in `.agents/handoffs/`.
- **[take-over](./skills/productivity/take-over/SKILL.md)**: Resume work from the latest handoff in `.agents/handoffs/`, following the supersedes chain deeper only when needed.
- **[teach](./skills/productivity/teach/SKILL.md)**: Teach the user a new skill or concept over multiple sessions, using the current directory as a stateful teaching workspace.

### Reference

The reusable layer other skills invoke or cite.

- **[grilling](./skills/reference/grilling/SKILL.md)**: Interview the user relentlessly about a plan, decision, or idea until every branch of the design tree is resolved. The reusable interview primitive behind `grill-me`, `grill-with-documentation`, `triage`, `wayfinder` and `improve-codebase-architecture`.
- **[domain-modeling](./skills/reference/domain-modeling/SKILL.md)**: Actively build and sharpen a project's domain model: challenge terms against the glossary, stress-test with edge-case scenarios, and update `CONTEXT.md` and ADRs inline.
- **[codebase-design](./skills/reference/codebase-design/SKILL.md)**: Shared discipline and vocabulary for designing deep modules: a lot of behaviour behind a small interface, placed at a clean seam, testable through that interface.
- **[documentation](./skills/reference/documentation/SKILL.md)**: Write and maintain technical documentation for README files, API references, runbooks, architecture documents, and onboarding guides.
- **[writing-for-agents](./skills/reference/writing-for-agents/SKILL.md)**: Writing documents for agents: skills, AGENTS.md/CLAUDE.md, and any doc an agent reaches by a pointer.
- **[wizard](./skills/reference/wizard/SKILL.md)**: Generate an interactive bash wizard that walks a human through steps only they can perform: provisioning infrastructure, setting up credentials or CI secrets, walking an unfamiliar third-party dashboard, or running a one-off migration or cutover.
- **[unslop](./skills/reference/unslop/SKILL.md)**: Edit writing to remove AI patterns while preserving its meaning and tone. Apply it to all writing.

### Experimental

These skills take externally visible actions on pull requests, merge requests, issues, or tickets, or send your text to a third-party API. They are available for direct installation, but are not included in the plugin while their workflows are being proven.

- **[address-feedback](./skills/experimental/address-feedback/SKILL.md)**: Assess every substantive comment on a pull request, merge request, issue, or ticket; implement the approved change plan; then draft and post a reply to each comment.
- **[publish-message](./skills/experimental/publish-message/SKILL.md)**: Post a short comment to a GitHub or GitLab pull request or merge request, or a Jira issue, leading with the reason rather than restating the diff or ticket.
- **[publish-review](./skills/experimental/publish-review/SKILL.md)**: Publish a finished code review to the tracker as a summary comment and, on GitHub or GitLab, concretely fixable inline suggestions.
- **[setup-delegation-policy](./skills/experimental/setup-delegation-policy/SKILL.md)**: Install the delegation and model routing rule (Light, Balanced, Heavy, Frontier tiers, with a per-harness model table) into the global steering files on this machine, and give every harness that binds models per agent one subagent per tier, so every session decides where a task runs and on which model tier.
- **[classify](./skills/experimental/classify/SKILL.md)**: Classify text against your own labels with classifier.dev, a keyless HTTP API that returns a calibrated confidence per verdict: triage, filter or bucket many items without reading each one, or decide between named options.
