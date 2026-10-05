Derived from upstream `implement-spec`, verified at revision `d81f3a1`, and renamed in this fork from `implement-all` to `divide-and-conquer` when it gained per-task model routing. The [archived upstream page](../../../.upstream/snapshots/d81f3a1/files/docs/engineering/implement-spec.md) preserves its provenance.

## What it does

`divide-and-conquer` builds an authorized task graph or living work batch on one integration branch, in three phases:

- **Divide**: every task is routed to the least expensive model that can do it reliably (Light, Balanced, Heavy, or Frontier), with an effort level and a reason. Tasks too small to be worth a briefing stay in the coordinating session. You approve this routing table before anything is dispatched.
- **Conquer**: implementer subagents, each at its routed tier, build the ready tasks in parallel, each calling [implement](./implement.md) in its own worktree. A task that fails is retried once at the next tier up, then marked blocked.
- **Combine**: finished tasks merge into the integration branch, and one [review-and-refactor](./review-and-refactor.md) runs over the whole batch.

It accepts shared specifications or an explicit approved batch in working state. Local task bodies remain authoritative until authorized publication; afterward the remote tracker owns tasks and local files carry title/link pointers.

## When to reach for it

Type `/divide-and-conquer`, or let an agent or another skill reach for it; [iterate](./iterate.md) does when a batch splits into independent tasks. Use it for agreed work that benefits from parallel implementation. Use [implement](./implement.md) for one piece of work, which is usually cheaper.

## Common questions

**How much will it cost?**

It depends on the number of tasks and their tiers, since every subagent reloads its own context. The routing table shows both before dispatch, so you can lower a tier, keep a task in the coordinating session, or cut scope. The agent quotes measured costs only.

**Which models does it pick?**

The ones your delegation tool actually offers, at the latest version within each tier's family. When the delegation and model routing rule from [setup-delegation-policy](../setup/setup-delegation-policy.md) is installed, it governs; otherwise the skill carries the same tiers.

**Must I configure a remote tracker?**

Only for remote tracker work. Local-only batches proceed without tracker setup. Publishing a request or tasks still needs authorization.

**Does a configured tracker workflow authorize remote changes?**

No. Opening a draft request, making it ready, adding task-closing links, and closing remote tasks require explicit destination-and-scope authorization. Without it, the integration branch stays local and publication stays pending.

**Will parallel branches merge without conflicts?**

No. Implementers synchronize with the integration branch, but concurrent changes can still conflict. Merges with conflicts get a stronger tier, and the final review catches interactions that individual task checks miss.

**What if a skill it calls or hands over to is not installed?**
It names the missing skill with its install command, carries out that step from its stated intent, and tells you the step ran without it. Without `document` it waits instead, because its rules use that skill's terms: install it, or tell it to proceed anyway. When it tells you to run a skill you don't have, it gives the install command with it. The skills involved are listed at the top of its [`SKILL.md`](../../../skills/workflow/divide-and-conquer/SKILL.md).

**What about a task I keep in the coordinating session?**
It follows the same path without the subagents: built on its own task branch cut from the integration branch, with the integration branch tip merged in, and merged into the integration branch only after its verification passes.

## It's working if

- You saw and approved the routing table before any subagent started.
- Ready tasks progress in parallel without crossing agreed ownership boundaries.
- The final report names the tier and model behind each task, including escalations.
- One review compares the integrated branch to its pinned starting state and originating agreement.

## Where it fits

This coordinates the implementation stage after [specify](./specify.md) and [taskify](./taskify.md), or for a batch inside [iterate](./iterate.md), then calls [review-and-refactor](./review-and-refactor.md) across the integration branch. [guide](../productivity/guide.md) maps the other routes.
