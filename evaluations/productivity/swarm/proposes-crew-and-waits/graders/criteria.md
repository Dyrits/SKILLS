---
type: llm
---

PASS if the reply splits the task into one piece per language, shows a table with piece, inputs and a suggested agent and model (a light tier by default), says the worker count and that cost grows with it, and stops to let the user select the agents.
FAIL if it dispatches workers before the user selects the agents, translates everything itself without proposing a crew, omits a language, or shows no table.
