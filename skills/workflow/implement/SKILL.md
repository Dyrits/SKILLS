---
name: implement
description: "Implement authorized work test-first and report its verification evidence. Use when the user asks to build agreed specifications, a task, or an approved work batch, or when a coordinating skill hands an implementer one task."
metadata:
  forks: "mattpocock/skills/skills/engineering/implement"
---

Call the Skill tool with "document"; its terms (authorized, obligation, lazy, pointer) and rules apply throughout.

**Calls:** `debug`, `document`, `test-first`. **Hands over to:** `/review-and-refactor`.

Identify the authorized behavior and its originating agreement: a task, specifications with their requirements, or a user-approved batch in working state. Read the applicable requirements. Record the starting commit and work scope for review.

Preserve accepted behavior, and prefer targeted edits over regenerating unchanged code or documents. Put mechanical conventions in formatter, compiler, and lint configuration; keep the conventions file for judgment those tools cannot enforce. Comments capture reasons and constraints the code cannot show.

When the work fixes a reported bug, call the Skill tool with "debug" before editing code, so the fix follows a reproduced cause. Call it too for a resistant failure instead of stacking speculative fixes.

Call the Skill tool with "test-first" where possible, at pre-agreed seams. Run typechecking and individual test files regularly, and the full test suite once at the end. Verify acceptance against the originating agreement, including appearance and interaction evidence when human judgment is needed, and state which checks passed, failed, or could not run. Call the Skill tool with "webapp-testing" when verification needs browser interaction. It ships outside this repository; when it is not installed, tell the user, verify the interaction another way (a scripted browser run, for example), and report the check as could not run if no way is available.

In a versioned project, commit the work to the current branch. When a coordinating skill handed you the work, it owns the project records: return the evidence, blockers, and resumption pointers to it. Otherwise keep working state current with unfinished work, evidence, blockers, and resumption pointers, and record completed agreements and deliveries in the changelog; unfinished acceptance stays in working state.

Review belongs to whoever runs the batch. Finish by reporting the starting commit, scope, originating agreement, and verification evidence; a standalone run tells the user to run `/review-and-refactor` with them as the next step.
