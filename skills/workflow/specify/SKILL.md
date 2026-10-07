---
name: specify
description: "Resolve the open decisions in a selected scope and synthesize its living repository specification. Use when the user asks to specify a capability, or when requirements have outstanding decisions before implementation."
metadata:
  forks: "mattpocock/skills/skills/engineering/grill-with-docs mattpocock/skills/skills/engineering/to-spec"
---

# Specify

Turn the selected scope into agreed behavior, design, and acceptance. Interview only where decisions remain unresolved; synthesize directly when current context is settled.

**Calls:** `delineate`, `document`, `interview`, `prototype`. **Hands over to:** `/implement`, `/iterate`, `/taskify`.

## Gather and reconcile

Call the Skill tool with "document"; its terms (authorized, obligation, lazy, pointer) and rules apply throughout, with full changelog records. Inspect the conversation, applicable instructions, global and feature requirements, existing specifications, backlog, working state, glossary, architecture decisions, and relevant code. Fetch the full body and comments of referenced remote records when they are relevant inputs.

Identify the selected scope and account for every applicable requirement. Reuse existing agreements. A missing blocking decision stays explicit and open until the user settles it.

## Resolve the frontier

Call the Skill tool with "interview" only for unresolved decisions necessary to complete the selected scope. Call the Skill tool with "delineate" when a term is fuzzy or disputed; reading existing vocabulary alone does not require it. Record a hard-to-reverse decision by calling the Skill tool with "document" for a decision record.

Agree observable acceptance and validation, using existing high-level test seams where practical. Separate checks an agent can perform from any necessary human acceptance.

When code or visual exploration would settle a question, propose a separately scoped prototype and obtain user approval before building it. Call the Skill tool with "prototype" only within that requested or approved scope. Capture what its evidence establishes and what still needs production validation. Useful validated code may be productionized and integrated; exploratory success alone does not establish production readiness.

## Synthesize and maintain

Record newly established constraints in the project or capability requirements document, with their source, and point to them from the specification.

Write or update the canonical repository specification for the selected scope. Include the problem and intended outcome, agreed behavior and relevant edge cases, design and interfaces, acceptance and validation, requirement references, dependencies, and explicit exclusions. Complete this scope without demanding an exhaustive specification for future product work.

Use precise domain language. Include a decision-rich prototype shape or snippet when it is clearer than prose, with its validation limits. Unresolved proposals belong in the draft, not among agreed behavior.

Record authorized agreements in the changelog, and keep the backlog and working state current.

Report the canonical paths, covered requirements, agreements, unresolved blockers, and validation still needed. The scope is specified when its necessary decisions are authorized and its behavior and acceptance are coherent; if blockers remain, report partial progress honestly.

Close by offering the user the next move: to run `/taskify` for a useful decomposition, to run `/implement` for direct delivery, or to run `/iterate` for a small living-code batch.
