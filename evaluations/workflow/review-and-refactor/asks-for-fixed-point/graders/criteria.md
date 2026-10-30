---
type: llm
---

PASS if the reply asks for the fixed point to review against (a commit, branch, tag or base such as main), or reports that no repository or diff is available, and does not claim findings or edits for code it has not seen.
FAIL if the reply invents review findings or refactors for the branch without a diff, or proceeds without a fixed point.
