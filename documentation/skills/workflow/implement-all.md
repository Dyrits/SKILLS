## What it does

`implement-all` implements an entire specification on one **integration branch**, with each ticket built by an implementer subagent in its own git worktree.
It treats the tickets as a **task graph**: blocking edges determine the **frontier** of work that can run concurrently, and a merger subagent integrates each completed ticket.

It is [implement](./implement.md) at specification scale.
You review the combined branch after the tickets land, instead of driving one session per ticket yourself.

## When to reach for it

You invoke this by typing `/implement-all`; the agent won't reach for it on its own.
Use it when a specification and tickets with blocking edges already exist, and you want the whole graph built in one orchestrated run.
For a single ticket or a build you want to guide directly, use [implement](./implement.md).
If the specification has no tickets yet, use [to-tickets](./to-tickets.md) first.

## Prerequisites

- A tracker workflow configured through [setup-custom-skills](../getting-started/setup-custom-skills.md), describing where tickets live and how completed work is resolved.
- A specification and its tickets, with blocking edges.
- A harness that can run subagents and give each implementer its own worktree.

## The integration branch

The optional exploration subagent writes shared notes outside the repository.
Each implementer starts from the integration branch, calls [test-driven-development](./test-driven-development.md) to build its ticket, and merges the integration branch tip into its ticket branch before reporting completion.
A merger subagent then lands that work on the integration branch, and newly unblocked tickets start.
Agents communicate through **context pointers** to specifications, tickets, shared notes, and commits.

A draft pull or merge request opens after the first ticket merge when your tracker closes work through requests, or when you ask for one.
[to-pull-request](./to-pull-request.md) supplies its body.
Otherwise, the run can finish on the integration branch using a local markdown tracker, with no online request.

Once every ticket has landed and its behavior passes the checks, [code-review-and-refactor](./code-review-and-refactor.md) runs the refactor phase over the integration branch.
Its coordinator applies supported refactors and reuses the reviewers for verification.
One implementer addresses remaining implementation issues after the refactor phase.
The draft request then becomes ready for review, or the tickets are resolved through the configured tracker workflow.
The implementer worktrees are cleaned up at the end.

## Common questions

**Does it require GitHub or a pull request?**

No.
The goal is the integration branch, and a request is conditional on the tracker workflow or your instruction.
This works with GitLab merge requests and with a local markdown tracker.

**Does each implementer use test-driven development?**

Yes, each implementer explicitly calls `test-driven-development`.
Name agreed seams in the specification or tickets so each agent tests at the same interfaces.

**Why did its review report tickets that had not been built yet?**

The whole-specification review belongs after every ticket has landed.
Running it earlier treats unbuilt requirements as missing implementation.
The skill specifies one final review and one fix pass; it does not define a repeated review loop or a stopping rule after that fix.
If a broad review starts again, direct the agent to verify the specific findings and finish.

**Can parallel tickets still collide?**

Yes.
Worktrees isolate edits, but shared files and domain names can still conflict at integration time.
Add a blocking edge when two tickets need to change the same shared surface in sequence, or pin the shared names in the exploration notes.
Merging the integration branch before completion reduces drift but cannot guarantee that concurrent work lands without conflicts.

**A blocker landed, but its dependants still did not start.**

Some trackers keep the blocker open until the final request merges.
The graph starts from the tracker, but progress during the run must be computed from tickets already merged into the integration branch.
A stale blocked-by count can otherwise stall the remaining tickets.

**A worktree reported green while its key test was skipped.**

Worktrees contain tracked files; ignored fixtures, credentials, and local databases may be missing.
Check that required tests actually ran, and supply the required local resources or use the main checkout for verification that depends on them.

## It's working if

- Independent tickets run concurrently whenever their blockers allow it.
- Each implementer shows a failing test before its implementation.
- A ticket starts when its final blocker lands on the integration branch.
- The run ends on one integration branch, with a request only when the workflow calls for one.
- Tickets are resolved through the configured workflow, and implementer worktrees are cleaned up.

## Where it fits

`implement-all` is the parallel alternative to per-ticket [implement](./implement.md) in the main flow: `to-specifications` → `to-tickets` → `implement-all` → `code-review-and-refactor`.
[improve-agent-environment](../upkeep/improve-agent-environment.md) follows a session worth learning from.
[what-is-next](../getting-started/what-is-next.md) routes between the two ways to build.
