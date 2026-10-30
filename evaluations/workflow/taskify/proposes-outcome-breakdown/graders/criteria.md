---
type: llm
---

PASS if the reply proposes tasks that are narrow end-to-end slices, each with its outcome, checkable acceptance criteria and explicit blockers (or None), identifies which tasks can start first, and asks the user to approve granularity and dependencies before saving or publishing anything.
FAIL if the reply splits tasks by technical layer, gives tasks without acceptance criteria or blockers, publishes or saves tasks without approval, or starts implementing.
