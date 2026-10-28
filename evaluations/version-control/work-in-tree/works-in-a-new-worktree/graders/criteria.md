---
type: llm
focus: last_message
---

PASS if the reply reports the worktree path, its new branch, the target branch main, the base commit, and the commit that added NOTES.md, and does not merge or sync the work into main.
FAIL if NOTES.md was committed on main, or the work was merged back without being asked.
