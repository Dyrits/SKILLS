Upstream skill: `to-tickets`, renamed here as `taskify`.

## What it does

`taskify` decomposes approved work into coherent tasks with acceptance criteria and explicit blockers. Each task describes an outcome someone can verify, rather than an arbitrary layer or group of edits.

Local drafting is tracker-neutral. Remote publication requires explicit approval, and the published remote task becomes authoritative.

## When to reach for it

Type `/taskify`, or an agent can reach for it when the task fits. Use it when work benefits from sequencing or parallel delivery. If the whole change fits a small batch, [iterate](../workflow/iterate.md) or [implement](implement.md) may be enough.

## Tracer bullets and blocking edges

A tracer bullet is a narrow end-to-end slice with its own verifiable result. Blockers state what genuinely gates it. The frontier is the set of tasks whose prerequisites are complete.

Wide mechanical refactors can use expand-contract instead: introduce the compatible new form, migrate bounded batches, then remove the old form. The task graph makes the final integration check explicit when intermediate batches cannot pass independently.

## Common questions

**It made twelve tasks for a three-line change.**
Ask it to merge them, or skip taskify. Tasks should reduce coordination costs, not turn every edit into administration.

**Where do local tasks go?**
New local task bodies live in the capability's task files, where `AGENTS.md` or the tracker configuration says, by default under `documentation/capabilities/<capability>/tasks/`. After approved remote publication, the local file becomes a title and link to the authoritative remote task. Existing histories are preserved.

**Does a published task replace the repository specification?**
No. The task points to applicable requirements and specifications; the agreed specification remains canonical in the repository.

**What happens after the tasks are saved?**
It reports the saved paths or links, the remaining blockers, and the frontier of tasks whose prerequisites are complete, and stops there. The frontier is what an implementer reads next: [implement](./implement.md) can take one task, and [divide-and-conquer](./divide-and-conquer.md) the whole graph. Taskify does not start or suggest either.

## It's working if

- Every task has an observable outcome and acceptance it owns, verifiable with only that task and its blockers.
- The proposed breakdown and blockers reach you before publication.
- Tasks with no incomplete prerequisites can start independently.
- Published tasks have verified dependency links, and local pointers lead to their authoritative records.

## Where it fits

Taskify is an optional chain step after [specify](specify.md) and before [implement](implement.md) or [divide-and-conquer](divide-and-conquer.md). It produces a task graph, not an execution run. [Guide](../productivity/guide.md) maps the alternatives.
