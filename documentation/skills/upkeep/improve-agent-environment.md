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

Therefore, rules that govern code style belong to the review agent or automated tooling, not the implementation agent. Steering files loaded on every turn (`CLAUDE.md`, `AGENTS.md`) stay minimal and contain primarily **navigation pointers** rather than comprehensive rulebooks.

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
[setup-ai-workspace](../getting-started/setup-ai-workspace.md), [improve-codebase-architecture](./improve-codebase-architecture.md), and [code-review-and-refactor](../workflow/code-review-and-refactor.md) also offer to create it through the [domain-modeling](../reference/domain-modeling.md) interview, and the last two read it once it exists.
An existing standards document such as `CONTRIBUTING.md` works too.

## It's working if

- Candidates classify mechanical violations into concrete automated checks rather than vague steering lines.
- It identifies unwired or missing pre-commit and CI guardrails when errors occur that automation could have prevented.
- Suggestions for `CLAUDE.md` and `AGENTS.md` prune dead text and replace inlined instructions with navigation pointers.
- Findings are ranked by severity without modifying any repository files.

## Where it fits

`improve-agent-environment` closes the main flow after a session worth learning from. Run it before clearing the session, or point it at the session log from a fresh window. It is also periodic maintenance whenever accumulated session friction needs review. Its nearest neighbours are [improve-codebase-architecture](./improve-codebase-architecture.md), which audits codebase structure rather than the agent's working environment, and [writing-for-agents](../reference/writing-for-agents.md), which provides the underlying style guide for steering files and documentation. For the full map of skills, see [what-is-next](../getting-started/what-is-next.md).
