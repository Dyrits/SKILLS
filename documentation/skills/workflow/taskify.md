Upstream skill: `to-tickets`, renamed here as `taskify`.

## What it does

`taskify` decomposes approved work into coherent tasks with acceptance criteria and explicit blockers. Each task describes an outcome someone can verify, rather than an arbitrary layer or group of edits.

Local drafting is tracker-neutral. Remote publication requires explicit approval, and the published remote task becomes authoritative.

## When to reach for it

Type `/taskify`, or an agent or another skill can reach for it when the task fits. Use it when work benefits from sequencing or parallel delivery. If the whole change fits a small batch, [iterate](../workflow/iterate.md) or [implement](implement.md) may be enough.

## Tracer bullets and blocking edges

A tracer bullet is a narrow end-to-end slice with its own verifiable result. Blockers state what genuinely gates it. The frontier is the set of tasks whose prerequisites are complete.

Wide mechanical refactors can use expand-contract instead: introduce the compatible new form, migrate bounded batches, then remove the old form. The task graph makes the final integration check explicit when intermediate batches cannot pass independently.

## Common questions

**It made twelve tasks for a three-line change.**
Ask it to merge them, or skip taskify. Tasks should reduce coordination costs, not turn every edit into administration.

**Where do local tasks go?**
New local task bodies live under `documentation/capabilities/<capability>/tasks/`. After approved remote publication, the local file becomes a title and link to the authoritative remote task. Existing histories are preserved.

**Does a published task replace the repository specification?**
No. The task points to applicable requirements and specifications; the agreed specification remains canonical in the repository.

**What if a skill it calls is not installed?**
It names the missing skill with its install command, carries out that step from its stated intent, and tells you the step ran without it. Without `document` it waits instead, because its rules use that skill's terms: install it, or tell it to proceed anyway. The skills involved are listed at the top of its [`SKILL.md`](../../../skills/workflow/taskify/SKILL.md).

## It's working if

- Every task has an observable outcome and acceptance it owns.
- The proposed breakdown and blockers reach you before publication.
- Tasks with no incomplete prerequisites can start independently.
- Published tasks have verified dependency links, and local pointers lead to their authoritative records.

## Where it fits

Taskify is an optional chain step after [specify](specify.md) and before [implement](implement.md) or [divide-and-conquer](divide-and-conquer.md). It produces a task graph, not an execution run. [Guide](../productivity/guide.md) maps the alternatives.
