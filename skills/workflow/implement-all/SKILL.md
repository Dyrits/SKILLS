---
name: implement-all
description: "Implement an authorized task graph or agreed work batch on an integration branch."
disable-model-invocation: true
---

Call the Skill tool with "document"; its terms (authorized, obligation, lazy, pointer) and rules apply throughout.

Identify the authorized behavior and originating agreement for the batch: specifications with tasks, or a user-approved batch in `documentation/work-in-progress.md`. Read the applicable requirements. For remote tracker work, read `documentation/agents/issue-tracker.md` for the configured workflow; if it is missing, tell the user to run `/setup-ai-workspace`. Local-only work runs without tracker setup.

The goal is the entire authorized batch implemented on a single **integration branch**, with each task's implementation and validation accounted for.

The tasks form a **task graph** with blocking relationships, not a list of implementation steps. Its **frontier** contains tasks whose prerequisites have been satisfied.

Communicate primarily through **context pointers** to the originating agreement, tasks, research notes, and previous commits. Do not duplicate information already available through those pointers.

**Implementer subagents** should be run in the background where possible for maximum concurrency.

## Steps

1. Read the originating agreement and tasks to understand the task graph. For a batch in working state, derive its work boundaries and dependencies from there. Pin the starting commit and scope for final review.

2. Optionally use an **exploration subagent** for relevant codebase or external-documentation research. Save its Markdown notes outside the repository where future implementer subagents can read them.

3. Create the integration branch. If a pull or merge request is appropriate, prepare its body through the Skill tool with "draft-merge-request". Publish the branch and open a draft request once authorized, including any task-closing links; existing explicit instructions can supply that authorization. Open the draft after the first merge in step 5, when commits are ahead of the target. Link the specification as context; closing links apply to tasks. Until authorized, keep the branch and draft local and report publication as pending.

4. Use **implementer subagents** to implement each task in its own worktree and branch. Each implementer subagent:
   - receives pointers to the originating agreement, applicable requirements, scoped acceptance, and work records;
   - confirms its worktree is based on the integration branch before starting, and rebases its own task branch onto it if needed;
   - calls the Skill tool with "test-first" to build the task;
   - merges the integration branch tip into its own branch before reporting done.

5. Once an **implementer subagent** completes, merge its work to the integration branch with a **merger subagent**.

6. When the **frontier** changes, start implementer subagents for newly unblocked tasks.

7. Once the authorized batch is implemented, call the Skill tool with "review-and-refactor" on the integration branch, supplying the pinned starting commit, scope, originating agreement, and evidence. Fix remaining implementation issues and commit the refactors in a single implementer subagent.

8. Record validated local completion. Mark a remote draft ready or resolve remote tasks once those transitions are authorized; ask about the others or leave them pending in working state. Report implementation evidence separately from request readiness, task closure, and other publication state.

9. Clean up disposable implementer worktrees only after confirming their work is integrated and they contain no uncommitted or unmerged changes.

Throughout, keep `documentation/work-in-progress.md` current with active assignments, unfinished work, evidence, acceptance, and blockers. Verify the integrated batch against its originating agreement, including appearance and interaction acceptance when judgment is needed. Record completed agreements and deliveries in the root `CHANGELOG.md`, and state any blocked or missing verification.
