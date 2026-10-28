---
type: llm
focus: last_message
---

PASS if the reply lists the setup areas (task tracking or workspace, code checks, Git guardrails, AI tooling) with each one's current state in this repository and a recommendation, then asks which to set up.
FAIL if it installed or configured anything before asking, or if it asks generic questions without having inspected the repository.
