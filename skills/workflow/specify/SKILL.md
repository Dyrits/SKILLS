---
name: specify
description: Resolve the open decisions in a selected scope and synthesize its living repository specification.
disable-model-invocation: true
---

# Specify

Turn the selected scope into agreed behavior, design, and acceptance. Interview only where decisions remain unresolved; synthesize directly when current context is settled.

## Gather and reconcile

Call the Skill tool with "documentation" and apply its shared project document model. Inspect the conversation, applicable instructions, global and feature requirements, existing specifications, backlog, working state, glossary, architecture decisions, and relevant code. Fetch the full body and comments of referenced remote records when they are relevant inputs.

Identify the selected scope and account for every applicable requirement. Reuse existing agreements. Surface conflicting legacy inputs and consequential scope or obligation conflicts to the user; continue independent unblocked work. A missing blocking decision remains explicit rather than becoming an assumption.

## Resolve the frontier

Call the Skill tool with "refine" only for unresolved decisions necessary to complete the selected scope. Call the Skill tool with "domain-modeling" when actively sharpening terms or recording qualifying architectural decisions; reading existing vocabulary alone does not require it.

Agree observable acceptance and validation, using existing high-level test seams where practical. Separate checks an agent can perform from any necessary human acceptance.

When code or visual exploration would settle a question, propose a separately scoped prototype and obtain user approval before building it. Call the Skill tool with "prototype" only within that requested or approved scope. Capture what its evidence establishes and what still needs production validation. Useful validated code may be productionized and integrated; exploratory success alone does not establish production readiness.

## Synthesize and maintain

Record newly established constraints in the appropriate project or feature requirements document, preserving their source and any required authorization. Feature constraints add to global obligations rather than silently overriding them. Link those requirements from the specification instead of copying them.

Write or update the canonical repository specification for the selected scope. Include the problem and intended outcome, agreed behavior and relevant edge cases, design and interfaces, acceptance and validation, requirement references, dependencies, and explicit exclusions. Complete this scope without demanding an exhaustive specification for future product work.

Use precise domain language and link authoritative constraints instead of copying them. Include a decision-rich prototype shape or snippet when it is clearer than prose, with its validation limits. Unresolved proposals belong in the draft, not among agreed behavior.

Record authorized agreements using the shared changelog semantics. Maintain useful backlog and unfinished working state without creating empty documents. Specifications remain canonical in the repository even if a remote record links to or summarizes them. Remote publication or updates require explicit approval of destination and scope.

Report the canonical paths, covered requirements, agreements, unresolved blockers, and validation still needed. The scope is specified when its necessary decisions are authorized and its behavior and acceptance are coherent; if blockers remain, report partial progress honestly.

The human may next choose taskify for a useful decomposition, implement for direct delivery, or iterate for a small living-code batch. Tasks are optional, not a prerequisite imposed by this skill.
