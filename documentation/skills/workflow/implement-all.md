## What it does

`implement-all` implements an entire specification on a single branch, as one draft PR that closes the specification and its tickets. The defining constraint is that it treats the tickets as a **task graph** rather than a list: with blocking edges resolved, there is always a **frontier** of tickets that are ready, and background implementer subagents grab them concurrently, each in its own git worktree.

It is [implement](./implement.md) at specification scale. `/implement` builds one ticket in one session with you in the loop; `implement-all` builds every ticket, and you watch an orchestrated pipeline.

## When to reach for it

You invoke this by typing `/implement-all`; the agent won't reach for it on its own. Reach for it when a specification plus its tickets already exist (from [to-specifications](./to-specifications.md) and [to-tickets](./to-tickets.md)) and you want the whole set driven to one PR without driving each ticket yourself. For a single ticket, or when you want to stay hands-on per ticket, use [implement](./implement.md) instead.

## The pipeline

Read the specification and tickets as a graph. (Optional) an exploration subagent digests the codebase and docs into shared notes outside the repository, so implementers implement rather than explore. Create the branch and draft PR. Then the loop: for each ticket on the frontier, an **implementer subagent** works in its own worktree; when it finishes, a **merger subagent** folds the work into the PR branch; the merge recomputes the frontier and unblocked tickets get new implementers. When the graph is empty, [code-review](./code-review.md) runs over the PR, its findings are fixed in one final implementer pass, the PR goes ready, and the worktrees are cleaned up.

Communication between agents is deliberately sparse: **context pointers** to the specification, tickets, research notes and previous commits, never duplicated prose. The graph and the files carry the state.

## It's working if

- Implementer subagents are running concurrently, not one-at-a-time.
- No subagent re-explains what a pointer already reaches: the specification, tickets, and notes are referenced, not restated.
- The PR branch accumulates merged ticket work, and the draft PR closes the specification issue.
- Worktrees are gone when it finishes.

## Where it fits

`implement-all` is the parallel end of the main flow: [what-is-next](../getting-started/what-is-next.md) routes the multi-session build through `/to-specifications` → `/to-tickets` → per-ticket `/implement`, and `implement-all` is the alternative when you want that whole stretch driven concurrently to a single PR instead of worked ticket by ticket.
