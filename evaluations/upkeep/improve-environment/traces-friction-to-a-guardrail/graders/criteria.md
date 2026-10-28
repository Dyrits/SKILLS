---
type: llm
focus: last_message
---

PASS if the reply finds that the lint script exists in package.json but nothing runs it before a commit or in CI, and proposes wiring that existing script into a pre-commit hook or CI job rather than writing a new check or a steering-file reminder.
FAIL if it only suggests adding a line to AGENTS.md asking agents to lint, or proposes code changes unrelated to the environment.
