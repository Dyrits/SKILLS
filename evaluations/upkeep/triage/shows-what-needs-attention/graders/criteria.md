---
type: llm
focus: last_message
---

PASS if the reply groups the tasks into untriaged (task 1, the export bug), to-evaluate (task 2, dark mode), and on-hold whose condition may have lifted (task 3, waiting on the API release that task 4 says shipped), with a one-line summary each, leaves out task 5 (ready), and asks which to look at.
FAIL if it changes any task's status or category without being asked, or omits one of tasks 1 to 3.
