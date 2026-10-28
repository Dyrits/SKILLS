---
type: llm
focus: trace
---

PASS if the run produced candidates that name shallow modules in this code (for example the pass-through files in src/) and propose deepening them, using terms such as module, interface, depth, or seam, then asks which candidate to explore.
FAIL if it refactors code without being asked, or writes no report.
