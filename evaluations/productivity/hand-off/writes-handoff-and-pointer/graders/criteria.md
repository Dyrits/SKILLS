---
type: llm
focus: trace
---

PASS if the handoff file has the sections Goal, State, Decisions, Next, Open questions and Sources in that order, a verbatim "To resume" paragraph, a Supersedes line (none for a new thread), marks the passing test run as assumed or unverified rather than verified (it was not rerun in this workspace), keeps the next step as porting `/orders`, and AGENTS.md holds exactly one line pointing to the new file and saying handoffs are shared.
FAIL if any section is missing or out of order, the test claim is marked verified without being rerun, the file is written outside a handoffs folder, AGENTS.md has no pointer or two for the thread, or the reply names a skill for the next session to call.
