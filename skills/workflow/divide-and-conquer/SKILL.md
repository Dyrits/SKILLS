---
name: divide-and-conquer
description: "Implement an authorized task graph in parallel: route each task to the least expensive capable agent, build on one integration branch, then review once. Use when the user asks to implement a whole task graph or a batch of independent tasks."
metadata:
  forks: "mattpocock/skills/skills/engineering/implement-spec"
---

# Divide and conquer

The project documents and their rules are in [project-documents.md](references/project-documents.md); its terms (authorized, obligation, lazy, pointer) apply throughout.

Identify the authorized behavior and originating agreement for the batch: specifications with tasks, or a user-approved batch in working state. Read the applicable requirements. For remote tracker work, read the task tracker configuration that `AGENTS.md` points to for the configured workflow; if `AGENTS.md` points to none, ask the user how the remote tasks are read and updated, and keep remote updates pending until they answer. Local-only work runs without tracker setup.

The goal is the entire authorized batch implemented on a single **integration branch**, each task built by the least expensive agent that can do it reliably, with each task's implementation and validation accounted for. The run has three phases: **divide** routes every task, **conquer** builds them in parallel, **combine** merges and reviews once.

The tasks form a **task graph** with blocking relationships, not a list of implementation steps. Its **frontier** contains tasks whose prerequisites have been satisfied.

Communicate primarily through **context pointers** to the originating agreement, tasks, research notes, and previous commits. Do not duplicate information already available through those pointers.

Run subagents in the background where possible for maximum concurrency.

## Divide

1. Read the originating agreement and tasks to understand the task graph. For a batch in working state, derive its work boundaries and dependencies from there. Pin the starting commit and scope for final review.

2. Optionally use an **exploration subagent** for relevant codebase or external-documentation research. Save its Markdown notes outside the repository where future implementer subagents can read them.

3. Route every task, the merges, and the final fixes by [routing.md](references/routing.md).

4. Present the **routing table** and get the user's approval before dispatching anything. One row per task: title, blockers, tier, resolved model or agent, effort, and the reason for the tier. Below it, state how many subagents will run and that each reloads its own context, so cost grows with the number of tasks and their tiers; quote measured costs only. The user may change tiers, keep tasks here, or cut scope. Completion: the user approved the table as shown or as adjusted.

## Conquer

5. Create the integration branch. If a pull or merge request is appropriate, prepare its body following [merge-request.md](references/merge-request.md). Publish the branch and open a draft request once authorized, including any task-closing links; existing explicit instructions can supply that authorization. Open the draft after the first merge, when commits are ahead of the target. Link the specification as context; closing links apply to tasks. Until authorized, keep the branch and draft local and report publication as pending.

6. For each frontier task, start an **implementer subagent** at its routed tier, in its own worktree and branch. Each implementer subagent:
   - receives pointers to the originating agreement, applicable requirements, scoped acceptance, and work records;
   - confirms its worktree is based on the integration branch before starting, and rebases its own task branch onto it if needed;
   - implements its one task following [implement.md](references/implement.md), whose path is in its briefing, told that this run owns the project records and the review;
   - merges the integration branch tip into its own branch before reporting done.

7. Once an implementer subagent completes with passing verification, merge its work to the integration branch with a **merger subagent**. A failed task follows the escalation rule in [routing.md](references/routing.md).

   A task kept in this session follows the same path without the subagents: build it on its own task branch cut from the integration branch, merge the integration branch tip into that branch, and merge into the integration branch only after its verification passes. The merge is Light, or Balanced with conflicts, as [routing.md](references/routing.md) sets it; do it here when the table kept it here, or route it to a merger subagent.

8. When the **frontier** changes, start implementer subagents for newly unblocked tasks at their routed tiers.

## Combine

9. Once the authorized batch is implemented, review and refactor the integration branch following [review.md](references/review.md), with the pinned starting commit as the fixed point, and the scope, originating agreement, and evidence. Fix remaining implementation issues and commit the refactors in a single implementer subagent.

10. Record validated local completion. Mark a remote draft ready or resolve remote tasks once those transitions are authorized; ask about the others or leave them pending in working state. Report implementation evidence separately from request readiness, task closure, and other publication state, and name the tier and model that handled each task, including escalations.

11. Clean up disposable implementer worktrees only after confirming their work is integrated and they contain no uncommitted or unmerged changes.

When a coordinator started this run, it owns the project records: return the routing, evidence, and blockers to it. Otherwise, throughout, keep working state current with the approved routing, active assignments, unfinished work, evidence, acceptance, and blockers. Verify the integrated batch against its originating agreement, including appearance and interaction acceptance when judgment is needed. Record completed agreements and deliveries in the changelog, and state any blocked or missing verification.
