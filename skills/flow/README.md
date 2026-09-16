# Flow

The idea→ship spine, in order.

## User-invoked

Reachable only when you type them (Claude Code: `disable-model-invocation: true`; Codex: `policy.allow_implicit_invocation: false` in `agents/openai.yaml`).

- **[grill-with-docs](./grill-with-docs/SKILL.md)**: Stateful grilling that sharpens an idea while building the domain model (`CONTEXT.md`, ADRs) as it goes.
- **[to-spec](./to-spec/SKILL.md)**: Turn the current conversation into a spec and publish it to the issue tracker.
- **[to-tickets](./to-tickets/SKILL.md)**: Break a plan, spec, or conversation into tracer-bullet tickets, each declaring its blocking edges.
- **[implement](./implement/SKILL.md)**: Build one ticket or small spec: `/tdd` at pre-agreed seams, `/code-review`, commit.
- **[implement-all](./implement-all/SKILL.md)**: Implement a whole spec on one branch: the tickets as a task graph, implementer subagents across the ready frontier, landing a single PR.

## Model-invoked

Model- or user-reachable (rich trigger phrasing so the model can reach for them).

- **[tdd](./tdd/SKILL.md)**: Test-driven development with a red-green-refactor loop, one vertical slice at a time.
- **[code-review](./code-review/SKILL.md)**: Two-axis review of the diff since a fixed point: Standards and Spec, as parallel sub-agents.
