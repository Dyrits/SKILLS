---
type: llm
---

PASS if the reply lists the open architecture decisions (stack, parts, data ownership, deployment), gives two or three real alternatives for at least the first ones with tradeoffs against the EU data location and two-developer constraints, recommends the simplest shape that meets them (for example one deployable part and one store), and asks the user to settle the decisions.
FAIL if the reply presents a single design as agreed without alternatives, recommends many separate services for a two-developer team without justification, ignores the EU data requirement, or designs one capability's internals instead of the whole system.
