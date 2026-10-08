---
name: architect
description: Decide or assess a system's technical shape (technology stack, parts and their boundaries, data ownership and flows, integrations, deployment) and how it meets the system-wide requirements, weighing alternatives and their tradeoffs. Use when choosing a stack or high-level architecture, when the user asks whether an existing system's architecture fits, or when a requirement or new capability puts the system's structure in question.
---

# Architect

Decide how the system as a whole is built: the stack, the parts it runs as, what each part owns, how the parts and external systems talk, and where they run, so that every system-wide requirement is met. Work at the level of the whole system. One capability's internal design, code conventions, and tool installation are out of scope.

Take one branch:

- **Design**: little or nothing is built yet. Decide the shape.
- **Assess**: a system exists. Describe it as it is, test it against the requirements, and recommend changes only where a requirement or a stated problem calls for one. "Keep it as it is" is a valid conclusion.

## Gather

Find the project's documents through its `AGENTS.md`, which names each one and where it lives; a kind it does not name does not exist yet. When you notice a likely document `AGENTS.md` does not name, mention it in your report instead of using it. Read the functional picture first: the system outline, the system-wide and capability requirements, and the glossary. Then read the technical state: the architecture document, the decision records, and, in Assess, the code, dependency manifests, configuration, and deployment files.

When the functional picture is missing, ask only what the architecture cannot be decided without: what the system is for, who uses it and how many, and what it must guarantee (availability, performance, data location, security, compliance, budget). Also ask what the team knows and must keep running, since skills and operations budget constrain the stack. Record each obligation the user states in the requirements, following [REQUIREMENTS-FORMAT.md](REQUIREMENTS-FORMAT.md), and report that the domain outline is missing.

In Assess, write the current shape down before judging it, from the code rather than from older documents, and flag every place the two disagree.

## Decide

List the open decisions as a tree: the stack and the parts come first; data ownership, flows, integrations, and deployment depend on them. For each decision, present two or three real alternatives, compare them against the requirements, the team's constraints, and the cost of reversing later, and recommend one. Prefer the simplest shape that meets the requirements: one deployable part and one store until a requirement or a context boundary justifies more.

Settle the tree with the user through the [interview method](INTERVIEW.md). Requirements outrank preferences: when an alternative the user prefers breaks a requirement, say which, and ask whether to relax the requirement or choose differently.

## Write it down

Write the architecture document following [ARCHITECTURE-FORMAT.md](ARCHITECTURE-FORMAT.md), updating the one `AGENTS.md` names in place. When it names none, first look for an existing home of that kind in the repository (judging by content, not a folder name alone, and asking when the match is unclear), and use the default only when nothing matches; never overwrite, but adopt a file already at the target and add to it in its own style. The default is `documentation/architecture.md`. Record each decision that is hard to reverse, surprising without context, and the result of a real tradeoff as a decision record following [DECISION-RECORD-FORMAT.md](DECISION-RECORD-FORMAT.md). A decision that replaces an earlier record marks that record as superseded.

When you create a document (the architecture, the first decision record, the requirements), add one line naming it and when to read it to the nearest `AGENTS.md`, and a link to it where the root `README.md` lists the project's documentation (adding a short Documentation section if there is none). Check for an existing line first.

With no user to answer (a subagent run), write nothing as agreed: return the current-shape description, the decision tree, and your recommendations.

Completion: every system-wide requirement has a row saying how it is met or naming its gap; every context or capability in the domain outline is served by a named part; every piece of data has one owning part; every decision in the tree is settled and written, or listed as open with its recommendation.
