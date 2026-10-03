---
name: implement-all
description: "Implement an authorized task graph or agreed work batch on an integration branch."
disable-model-invocation: true
---

Call the Skill tool with "documentation" for the shared project-document model before reading or updating work records.

Identify the authorized intended behavior and originating agreement for the batch. It may be shared specifications with tasks, or an explicit user-approved batch in living working state. Read applicable global and feature requirements. Living iteration does not require creating feature specifications or tasks just to run this workflow. Preserve historical inputs rather than automatically migrating them.

For remote tracker work, read `documentation/agents/issue-tracker.md` for the configured workflow. If remote work needs it and it is missing, tell the user to run `/setup-ai-workspace`. Continue local-only work without requiring tracker setup.

The goal is the entire authorized batch implemented on a single **integration branch**, with each task's implementation and validation accounted for. Tracker transitions and publication require their own explicit authorization. Local task bodies are authoritative before authorized publication; afterward remote tracker tasks are authoritative and local files carry title/link pointers. Local-only work does not require tracker setup.

The tasks form a **task graph** with blocking relationships, not a list of implementation steps. Its **frontier** contains tasks whose prerequisites have been satisfied.

Communicate primarily through **context pointers** to the originating agreement, tasks, research notes, and previous commits. Do not duplicate information already available through those pointers.

**Implementer subagents** should be run in the background where possible for maximum concurrency.

## Steps

1. Read the originating agreement and tasks to understand the task graph. For a living batch, derive the authorized work boundaries and dependencies from working state without manufacturing standalone specifications. Pin the starting commit and scope for final review. Resolve consequential scope or obligation conflicts with the user rather than weakening requirements.

2. Optionally use an **exploration subagent** for relevant codebase or external-documentation research. Save its Markdown notes outside the repository where future implementer subagents can read them.

3. Create the integration branch. If a pull or merge request is appropriate, prepare its body through the Skill tool with "to-pull-request". Before publishing the branch or opening a draft request, obtain explicit authorization for the destination and scope, including any task-closing links. Existing explicit instructions may supply that authorization; tracker configuration alone does not. Open an authorized draft after the first merge in step 5, when there are commits ahead of the target. Link the canonical repository specification as context, never as something to close. Without authorization, keep the branch and request draft local and report pending publication.

4. Use **implementer subagents** to implement each task in its own worktree and branch. Each implementer subagent:
   - receives the originating agreement, applicable requirements, scoped acceptance, and work-record pointers, including an approved living batch when there is no standalone specification;
   - confirms its worktree is based on the integration branch before starting, and rebases its own task branch onto it if needed;
   - calls the Skill tool with "test-driven-development" to build the task;
   - merges the integration branch tip into its own branch before reporting done.

5. Once an **implementer subagent** completes, merge its work to the integration branch with a **merger subagent**.

6. When the **frontier** changes, start implementer subagents for newly unblocked tasks.

7. Once the authorized batch is implemented, call the Skill tool with "code-review-and-refactor" on the integration branch, supplying the pinned starting commit, scope, originating agreement, and evidence. Fix remaining implementation issues and commit the refactors in a single implementer subagent.

8. Record validated local completion. Mark a remote draft ready or resolve remote tasks only when explicit authorization covers those transitions and their destinations. Ask for uncovered transitions, or leave them pending in local working state. Report implementation evidence separately from request readiness, task closure, and other publication state.

9. Clean up disposable implementer worktrees only after confirming their work is integrated and they contain no uncommitted or unmerged changes.

Throughout implementation, update `documentation/work-in-progress.md` autonomously with active assignments, unfinished work, evidence, acceptance, blockers, and resumption pointers. Keep local documents current under the shared model. Verify the integrated batch against its originating agreement, including appearance and interaction acceptance when judgment is needed. Record completed authorized agreements and deliveries automatically in root `CHANGELOG.md` using the shared format; report blocked or missing verification honestly.
