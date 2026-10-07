# Implement approved code changes

Adapted from the `implement` skill, for repository code changes approved in this run. The approved plan is the user-approved batch; this run owns the project records and the review.

1. Record the starting commit and the scope of the approved changes, and read the requirements and specifications the changes touch.
2. Preserve accepted behavior, and prefer targeted edits over regenerating unchanged code or documents. Put mechanical conventions in formatter, compiler, and lint configuration; keep the conventions file for judgment those tools cannot enforce. Comments capture reasons and constraints the code cannot show.
3. When a change fixes a reported bug, first reproduce it with a failing test or command that shows the reviewer's exact symptom, so the fix follows a reproduced cause. For a resistant failure, build that reproduction and test ranked, falsifiable hypotheses against it instead of stacking speculative fixes.
4. Build test-first where possible, at seams the plan or the existing tests already establish, following [TEST-FIRST.md](TEST-FIRST.md). Run typechecking and individual test files regularly, and the full test suite once at the end.
5. Verify each change against the approved plan, including appearance and interaction evidence when human judgment is needed, and state which checks passed, failed, or could not run.
6. In a versioned project, commit the work to the current branch.

Done when every approved code change is committed with its verification evidence, or its blocker is stated.
