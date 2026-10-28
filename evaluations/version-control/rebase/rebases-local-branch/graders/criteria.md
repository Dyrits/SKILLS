---
type: llm
focus: last_message
---

PASS if the final reply reports the branch with its start and new tip, states it was rebased onto main, gives an undo command using the backup ref, and pushes nothing (local only).
FAIL if it pushed, if it rebased a different branch, or if it left a rebase in progress.
