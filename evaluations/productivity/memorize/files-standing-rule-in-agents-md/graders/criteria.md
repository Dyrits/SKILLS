---
type: llm
focus: trace
---

PASS if the rule (use pnpm, never npm or yarn, with the lockfile and CI cache reason) is written in an AGENTS.md inside the workspace, exactly once, before or alongside answering the install question, and the reply says in one line what was saved and where.
FAIL if the rule is filed only in the harness's own memory or a home directory, is saved nowhere, is written twice, or the reply never says where it went.
