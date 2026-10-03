Upstream source: `retro`, verified in the `d81f3a1` tree.

## What it does

`improve-agent-environment` conducts a retrospective on a coding agent's session and recommends targeted improvements to the repository's steering, standards, and tooling. It audits session friction across seven categories: navigation, automated checks, coding standards, global steering files, tool economy, no-ops, and information access.

It never modifies steering or configuration files directly. The entire run produces ranked, prioritised candidates for human review, distinguishing mechanical violations that warrant deterministic checks from genuine judgement calls that belong in standards documentation.

## When to reach for it

You invoke this by typing `/improve-agent-environment`, and the agent will not reach for it on its own.

Reach for it after completing a non-trivial coding session, especially when an agent stumbled, took excessive turns finding files, missed an existing project convention, or incurred unnecessary token costs.

| Situation | Action |
| --- | --- |
| After a session where the agent made avoidable mistakes | Run `/improve-agent-environment` to identify preventative guardrails |
| The reviewer agent repeatedly flags the same syntactic pattern | Run `/improve-agent-environment` to turn it into an automated check |
| Steering files (`CLAUDE.md`, `AGENTS.md`) have grown noisy | Run `/improve-agent-environment` to prune no-ops and extract standards |
| Code architecture or module seams need review | Use [improve-codebase-architecture](./improve-codebase-architecture.md) instead |
| A specific defect needs root-cause diagnosis | Use [debug](./debug.md) instead |

## The deterministic check over the written rule

The skill's defining lever is **mechanical classification**. When an agent repeatedly misses a convention, the default instinct is to write another line in `GUIDELINES.md` or `AGENTS.md`. That forces every future agent to re-derive the rule on every turn, paying recurring context load and attention cost for what should be automatic.

`improve-agent-environment` enforces a strict hierarchy:

- **Mechanical rules** (fixed syntax, banned imports, naming conventions, file placement): build an automated check. Add a rule to the project's linter, wire a pre-commit hook, or add a CI step.
- **Judgement calls** (idiomatic style, balance of abstraction, readability): reserve `GUIDELINES.md` strictly for rules no linter could ever verify.
- **Missing guardrails**: if a repository lacks pre-commit or CI checks altogether, the skill flags the missing guardrail as a primary finding rather than asking instructions to compensate.

## Context pressure and the review boundary

The skill evaluates suggestions through the lens of **context pressure**. Implementation agents operate under heavy context pressure: they explore files, run commands, and write code. Reviewer agents operate under low context pressure: they inspect an isolated diff.

Put mechanical checks in tooling and judgement-call standards where the review can apply them. Steering files loaded on every turn (`CLAUDE.md`, `AGENTS.md`) stay small and primarily carry navigation pointers. This division reduces context load; it does not excuse an implementation agent from applicable requirements or repository rules.

## Documentation as reference

Use existing Documentation as reference material, reached through useful pointers, before proposing another file. A recommendation to reorganize documents must preserve requirements, agreed behavior, and validation evidence. Local upkeep within approved work can update those records autonomously; this retrospective itself only recommends changes and does not authorize implementation.

## Common questions

**Where does it read session logs from?**

It inspects the current session's transcript or local agent run logs on your machine. If you want to audit a specific prior session, specify its path, session ID, or date when invoking the skill.

**Does it apply the improvements automatically?**

No. It presents candidates ordered by severity, leaving you to decide which automated checks, hooks, or steering adjustments to implement.

**What happened to the `/retro` skill?**

`retro` was the upstream working name. This fork renamed it to `/improve-agent-environment` to use explicit naming and place it under the `upkeep/` bucket.

**Will it keep adding checks forever?**

It can identify no-ops in steering prose, but it does not audit every lint rule, hook, or CI job proposed in previous sessions.
Review checks that start rejecting valid changes; one session cannot establish whether an old rule still earns its cost.

**What if the suggestions are generic?**

Require each candidate to point to a specific difficulty in the session record.
Discard advice that cannot be traced to the session, and review the severity order yourself.

**Where does `GUIDELINES.md` come from?**

No skill ships the file for your project.
The retrospective can propose creating it for a judgement-call rule.
[setup-ai-workspace](../getting-started/setup-ai-workspace.md), [improve-codebase-architecture](./improve-codebase-architecture.md), and [review-and-refactor](../workflow/review-and-refactor.md) also offer to create it through the [model-domain](../reference/model-domain.md) interview, and the last two read it once it exists.
An existing standards document such as `CONTRIBUTING.md` works too.

## It's working if

- Candidates classify mechanical violations into concrete automated checks rather than vague steering lines.
- It identifies unwired or missing pre-commit and CI guardrails when errors occur that automation could have prevented.
- Suggestions for `CLAUDE.md` and `AGENTS.md` prune dead text and replace inlined instructions with navigation pointers.
- Findings are ranked by severity without modifying any repository files.

## Where it fits

`improve-agent-environment` is periodic maintenance after useful work in either development workflow. Run it before clearing the session, or point a new session at the log. [improve-codebase-architecture](./improve-codebase-architecture.md) surveys code structure; [write-for-agents](../reference/write-for-agents.md) guides steering instructions. [document](../reference/document.md) owns the project-document model so improvements do not create competing sources of truth. [guide](../getting-started/guide.md) maps the whole set.
