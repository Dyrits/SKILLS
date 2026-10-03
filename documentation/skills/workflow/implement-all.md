Derived from upstream `implement-spec`, verified at revision `d81f3a1`. The [archived upstream page](../../../.upstream/snapshots/d81f3a1/files/docs/engineering/implement-spec.md) preserves its provenance.

## What it does

`implement-all` coordinates an authorized task graph or living work batch on one integration branch. Tasks are a dependency graph, not a sequential checklist. Independent implementers work at the ready frontier, then their changes merge into the integration branch.

It accepts shared specifications or an explicit approved batch in working state. Local task bodies remain authoritative until authorized publication; afterward the remote tracker owns tasks and local files carry title/link pointers. Shared specifications remain canonical locally.

## When to reach for it

You invoke this by typing `/implement-all`; the agent will not reach for it on its own. Use it for agreed work that benefits from parallel implementation. Use [implement](./implement.md) for one piece of work.

## Common questions

**Must I configure a remote tracker?**

Only for remote tracker work. Local-only batches can proceed without tracker setup. Publishing a request or tasks still needs authorization.

**Does a configured tracker workflow authorize remote changes?**

No. Opening a draft request, making it ready, adding task-closing links, and closing remote tasks require explicit destination-and-scope authorization. Existing instructions can cover those actions, but configuration alone cannot. Without authorization, the implementation branch remains local and publication stays pending. Canonical repository specifications are linked as context, not closed.

**Will parallel branches merge without conflicts?**

No. Implementers synchronize with the integration branch, but concurrent changes can still conflict. Final review and integrated verification catch interactions that individual task checks miss.

**Does living iteration need new specification and task files?**

No. An approved working-state batch can define scope and dependencies without manufacturing those documents.

## It's working if

- Ready tasks progress in parallel without crossing agreed ownership boundaries.
- Working state shows active assignments, blockers, evidence, and unfinished acceptance.
- Final review compares the integrated branch to its pinned starting state and originating agreement.

## Where it fits

This coordinates the implementation stage after [specify](./specify.md) and [taskify](./taskify.md), then calls [review-and-refactor](./review-and-refactor.md) across the integration branch. [guide](../getting-started/guide.md) maps the other routes.
