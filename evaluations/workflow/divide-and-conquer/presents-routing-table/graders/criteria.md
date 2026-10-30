---
type: llm
---

PASS if the reply presents a routing table with one row per task showing blockers (task 3 blocked by task 2), a model tier with a reason, and a lighter tier for the mechanical rename than for the retry redesign, and asks the user to approve it before dispatching or building anything.
FAIL if the reply starts implementing or dispatching before approval, routes every task to the same tier without reasons, ignores the blocking edge from task 2 to task 3, or invents measured costs.
