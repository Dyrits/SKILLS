# Workflow

The idea→ship spine, in order.

## User-invoked

Reachable only when you type them (Claude Code: `disable-model-invocation: true`; Codex: `policy.allow_implicit_invocation: false` in `agents/openai.yaml`).

- **[grill-with-documentation](./grill-with-documentation/SKILL.md)**: Stateful grilling that sharpens an idea while building the domain model (`CONTEXT.md`, architecture decision records) as it goes.
- **[design-workflow](./design-workflow/SKILL.md)**: Stateful grilling that turns the recurring loops in your work into implementable workflow specifications.
- **[to-specifications](./to-specifications/SKILL.md)**: Turn the current conversation into a local draft specification, or publish it to the issue tracker when requested.
- **[to-tickets](./to-tickets/SKILL.md)**: Break a plan, specification, or conversation into tracer-bullet tickets, each declaring its blocking edges.
- **[implement](./implement/SKILL.md)**: Build one ticket or small specification: `/test-driven-development` at pre-agreed seams, `/code-review`, commit.
- **[implement-all](./implement-all/SKILL.md)**: Implement a whole specification on one branch: the tickets as a task graph, implementer subagents across the ready frontier, landing a single PR.

## Model-invoked

Model- or user-reachable (rich trigger phrasing so the model can reach for them).

- **[test-driven-development](./test-driven-development/SKILL.md)**: Test-driven development with a red-green-refactor loop, one vertical slice at a time.
- **[code-review](./code-review/SKILL.md)**: Two-axis review of the diff since a fixed point: Standards and Specification, as parallel sub-agents.
- **[to-pull-request](./to-pull-request/SKILL.md)**: Write the body of a pull or merge request: a summary visual, before/after evidence, and the merge danger.
