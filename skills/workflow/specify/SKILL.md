---
name: specify
description: "Resolve the open decisions about one capability's observable behavior and synthesize its living repository specification: behavior, edge cases, acceptance, and capability requirements. Use when the user asks to specify a capability or feature, or when requirements have outstanding decisions before implementation."
metadata:
  forks: "mattpocock/skills/skills/engineering/grill-with-docs mattpocock/skills/skills/engineering/to-spec"
---

# Specify

Turn the selected capability into agreed behavior and acceptance. Interview only where decisions remain unresolved; synthesize directly when current context is settled.

Stay on the observable side: what users and other systems can see and rely on, including an external contract such as a public API or an event others consume. How the code delivers it (modules, internal interfaces, the data model, technology) is out of scope; capture a technical idea the user raises as a note for the capability's blueprint, not as agreed behavior.

The documents and their rules are in [project-documents.md](references/project-documents.md); its terms (authorized, obligation, lazy, pointer) apply throughout, with full changelog records.

## Gather and reconcile

Find the project's documents through `AGENTS.md`, as [project-documents.md](references/project-documents.md) describes. Inspect the conversation, applicable instructions, the domain outline, system-wide and capability requirements, existing specifications, backlog, working state, glossary, and relevant code. Fetch the full body and comments of referenced remote records when they are relevant inputs.

Identify the selected capability and account for every applicable requirement. Reuse existing agreements. A missing blocking decision stays explicit and open until the user settles it.

## Resolve the frontier

Settle only the unresolved decisions needed to complete the selected scope, through the [interview method](references/interview.md).

When a term is fuzzy, disputed, or clashes with the glossary or the code, raise it before carrying on: name the conflict, test it with a concrete scenario, recommend a canonical term, and once the user agrees, write it to the glossary following [glossary-format.md](references/glossary-format.md). Reading the existing vocabulary needs none of this.

Agree observable acceptance and validation. Separate checks an agent can perform from any necessary human acceptance.

When building something would settle a question better than discussion (an interaction to try, a feasibility doubt), say so and propose a separately scoped prototype; keep the question open until its evidence is in. Useful validated prototype code may later be productionized; exploratory success alone does not establish production readiness.

## Synthesize and maintain

Record newly established obligations in the capability's requirements, or the system-wide requirements when they bind more than this capability, following [requirements-format.md](references/requirements-format.md), and point to them from the specification.

Write or update the capability's specifications. Include the problem and intended outcome, agreed behavior and relevant edge cases, external contracts, acceptance and validation, requirement references, dependencies on other capabilities, and explicit exclusions. Complete this scope without demanding an exhaustive specification for future product work.

Use the glossary's terms. Unresolved proposals belong in the draft, not among agreed behavior.

Record authorized agreements in the changelog, and keep the backlog and working state current. When the specifications are new and the domain outline lists capabilities, add this capability's line there or link its specifications from it.

When you create a document (the project's first capability specifications, the changelog, the backlog), add its `AGENTS.md` line and `README.md` link as [project-documents.md](references/project-documents.md) describes; one line covers all capability specifications.

With no user to answer (a subagent run), write nothing as agreed: return the draft and the open decisions, each with its recommendation.

Report the canonical paths, covered requirements, agreements, unresolved blockers, and validation still needed. The scope is specified when its necessary decisions are authorized and its behavior and acceptance are coherent; if blockers remain, report partial progress honestly.
