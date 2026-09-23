## What it does

`optimize-process` maps a recurring process, finds the work and waiting that slow it down, and recommends a sequence to try on the next cycle. Its impact comparison accounts for work an agent can complete in hours or minutes, plus the human time needed to set it up, make decisions, and review the result.

## When to reach for it

Type `/optimize-process`, or the agent reaches for it automatically when you describe a recurring workflow with delays, rework, or too many handoffs. It suits a process you can trace from a trigger to a finished result. For a specific broken behavior in software, use [debug](../upkeep/debug.md). For a change to one codebase's module structure, use [improve-codebase-architecture](../upkeep/improve-codebase-architecture.md).

## Time in the loop

The useful split is **effort versus elapsed time**. An agent may draft an artifact in minutes while a human spends an hour checking it, and an approval queue may still make the cycle take two days. The recommendation should show these separately so a faster step does not masquerade as a faster process.

When timing data is absent, the skill names the likely direction of change and the assumption behind it. A small trial can then supply real timings. It does not turn an imagined human-only workload into a claim that an agent needs weeks to finish it.

## Common questions

**Do I need detailed metrics before using it?**

No. One recent cycle and its steps are enough to start. The skill marks uncertain parts and only uses numbers when their assumptions are defensible.

**Will it remove approvals or reviews?**

It checks why they exist and keeps the decisions and controls that affect the outcome. It may change where they happen or what material reaches the reviewer.

## It's working if

- You can see the current and proposed steps side by side, including who or what does each one.
- The impact separates agent runtime, human attention, and queue time instead of reporting one vague duration.
- The first recommendation includes a small trial you can run on the next cycle.

## Where it fits

`optimize-process` is a standalone productivity skill. A recommendation that calls for a software change can enter the main build flow at [grill-with-documentation](../workflow/grill-with-documentation.md) or [to-specifications](../workflow/to-specifications.md). [What-is-next](../getting-started/what-is-next.md) maps the rest of the skills.
