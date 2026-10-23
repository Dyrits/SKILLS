---
name: implement
description: "Implement authorized work test-first and report its verification evidence. Use when the user asks to build agreed specifications, a task, or an approved work batch, or when a coordinator hands an implementer one task."
metadata:
  forks: "mattpocock/skills/skills/engineering/implement"
---

# Implement

The project documents and their rules are in [project-documents.md](references/project-documents.md); its terms (authorized, obligation, lazy, pointer) apply throughout.

Identify the authorized behavior and its originating agreement: a task, specifications with their requirements, or a user-approved batch in working state. When the user passes a task reference, fetch it through the task tracker configuration `AGENTS.md` points to and state its title before starting; when the reference is ambiguous, ask. Read the applicable requirements. Record the starting commit and work scope for review.

Preserve accepted behavior, and prefer targeted edits over regenerating unchanged code or documents. Put mechanical conventions in formatter, compiler, and lint configuration; keep the conventions file for judgment those tools cannot enforce. Comments capture reasons and constraints the code cannot show.

When the work fixes a reported bug, diagnose it following [diagnose.md](references/diagnose.md) before editing code, so the fix follows a reproduced cause. Diagnose a resistant failure the same way instead of stacking speculative fixes.

Read the capability's blueprint when `AGENTS.md` names one: its modules, seams, and acceptance table are the agreed design, and its seams are the pre-agreed seams. Build test-first where possible, at those seams, following [test-first.md](references/test-first.md). Run typechecking and individual test files regularly, and the full test suite once at the end. Verify acceptance against the originating agreement, including appearance and interaction evidence when human judgment is needed, and state which checks passed, failed, or could not run. When verification needs browser interaction, drive a real browser with what the harness offers (a browser tool, or a scripted run with a browser automation library the project already uses), and report the check as could not run if no way is available.

In a versioned project, commit the work to the current branch. When a coordinator handed you the work, it owns the project records: return the evidence, blockers, and resumption pointers to it. Otherwise keep working state current with unfinished work, evidence, blockers, and resumption pointers, and record completed agreements and deliveries in the changelog; unfinished acceptance stays in working state.

Review belongs to whoever runs the batch. Finish by reporting the starting commit, scope, originating agreement, and verification evidence, so a review of the batch can start from them.
