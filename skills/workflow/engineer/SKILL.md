---
name: engineer
description: Design one capability's technical solution before implementation (modules and their interfaces, data model, seams, and where each acceptance test attaches) inside the system's architecture, and write it down without writing production code. Use when the user asks how a specified capability should be built, to design a feature's modules, interfaces, or data model, or to make a capability's code more testable before building it.
---

# Engineer

Design how one capability is built: its modules and their interfaces, the data it owns, the seams where behavior varies, and the interface each acceptance test drives. Work inside the system's architecture and against the capability's specifications. Write no production code; the result is the capability's blueprint.

## Gather

Select one capability. Find the project's documents through its `AGENTS.md`, which names each one and where it lives; a kind it does not name does not exist yet. When you notice a likely document `AGENTS.md` does not name, mention it in your report instead of using it. Read, when present:

- the capability's specifications and capability requirements;
- the system-wide requirements, the architecture document, and the decision records;
- the glossary and the code conventions;
- the code the capability touches, and the modules around it.

When the specifications are missing, ask the user for the behavior and acceptance the design must serve, record those answers under a heading "Assumed behavior" in the blueprint, and report that the capability has no agreed specifications. When the architecture is missing, design from the parts the code already has and report the gap.

## Design

Use the vocabulary and principles in [MODULES.md](references/MODULES.md) throughout. List the open decisions as a tree: module boundaries and interfaces first; the data model, seams and adapters, and test seams depend on them. Recommend an answer for each from the code and the requirements, and settle them with the user through the [interview method](references/INTERVIEW.md).

- To deepen existing shallow modules, follow [DEEPENING.md](references/DEEPENING.md).
- When the user wants to compare interfaces, or a central interface has no clear best shape, follow [DESIGN-IT-TWICE.md](references/DESIGN-IT-TWICE.md).

**Escalate instead of diverging.** When the design needs something the architecture does not allow (a new part, a different store, a change in which part owns some data), stop on that decision. Write a decision record with status `proposed` following [DECISION-RECORD-FORMAT.md](references/DECISION-RECORD-FORMAT.md), explain the conflict to the user, and continue only on the parts that do not depend on it. Once the user accepts the record, update the architecture document to match.

## Write it down

Write the capability's blueprint following [BLUEPRINT-FORMAT.md](references/BLUEPRINT-FORMAT.md), updating an existing one in place. When `AGENTS.md` says nothing about blueprints, first look for an existing home of that kind in the repository (judging by content, not a folder name alone, and asking when the match is unclear), and use the default only when nothing matches; never overwrite, but adopt a file already at the target and add to it in its own style, and give new files and entries in an adopted home the neighbouring documents' naming, numbering, and template. The default is in the format. Record a capability-level decision that is hard to reverse, surprising without context, and the result of a real tradeoff as a decision record, linked from the blueprint. Create the folder with its first document.

When you create a blueprint, add one line pointing to it from the capability's specifications when they exist. When you create the project's first blueprint, add one line saying where capability blueprints live and when to read them to the nearest `AGENTS.md`, and a link to where they live where the root `README.md` lists the project's documentation (adding a short Documentation section if there is none). Do the same for the first decision record. Check for an existing line first.

With no user to answer (a subagent run), write nothing as agreed: return the decision tree, your recommendations, and any conflict with the architecture.

Completion: every acceptance criterion and every applicable requirement is traced to the module that delivers it and the interface its test drives; every module lists its interface; every conflict with the architecture is a proposed decision record; every open question is listed with its recommendation; no production code was written.
