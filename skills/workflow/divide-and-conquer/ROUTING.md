# Routing

Read this when building the routing table, and again when a task fails. Route each unit of work to the least expensive model that can complete it reliably.

## Tiers

When the "Delegation and model routing" rule is installed in your steering file, its tiers and model-version checks govern. Otherwise use these:

- **Light**: small, deterministic, well-scoped, verifiable. Renames, config tweaks, small fixes, test additions.
- **Balanced**: ordinary implementation, debugging, tests, specialized engineering work.
- **Heavy**: ambiguous requirements, architecture, cross-cutting changes, hard debugging, high-risk operations, final integration.
- **Frontier**: the hardest reasoning and the longest-horizon agentic runs, when the tier below has already fallen short or being wrong costs far more than the tokens do.

| Tier | Claude | Codex |
| --- | --- | --- |
| Light | Haiku | Luna |
| Balanced | Sonnet | Terra |
| Heavy | Opus | Sol |
| Frontier | Fable | Astra |

## Route a task

Judge each task by its scoped acceptance and the code it touches, not its title:

- Size and ambiguity set the floor: a task with settled acceptance and one seam is Light or Balanced; a task that still needs interpretation, crosses modules, or touches data, security, or concurrency is Heavy.
- Keep a task **here**, in the coordinating session, when writing its briefing costs more than doing it.
- Merges are Light; a merge with conflicts is Balanced. The final fixes after review are Heavy, since they span the integrated batch.
- Effort follows the tier when the tool offers a per-call effort or reasoning setting: low for Light, default for Balanced, high for Heavy and Frontier. Where effort is a session-level setting, name it in the table and leave the switch to the user.

Read your delegation tool's parameter list in this session before filling the table: trust the models and agents it offers over the names above, and use the latest version within each tier's family. If it takes a per-call model override, pass the exact identifier; otherwise pick the agent whose description matches the tier. With no delegation tool, every task stays here and the table says so.

## Escalate a failure

A task whose implementer reports failing verification, or whose result does not meet its acceptance, is re-dispatched once at the next tier up, with the failure evidence in the briefing. A second failure stops the task: mark it blocked in working state, keep its dependents off the frontier, and report it with both attempts' evidence. Record each escalation in the routing table.
