---
type: llm
focus: last_message
---

PASS if the reply names the source branch, the target branch main, and the verified commit main now points to, and says it was a fast-forward.
FAIL if it created a merge commit, pushed to a remote, or removed the worktree without being asked.
