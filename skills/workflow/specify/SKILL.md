---
name: specify
description: "Resolve the open decisions about one capability's observable behavior and synthesize its living repository specification: behavior, edge cases, acceptance, and capability requirements. Use when the user asks to specify a capability or feature, or when requirements have outstanding decisions before implementation."
metadata:
  forks: "mattpocock/skills/skills/engineering/grill-with-docs mattpocock/skills/skills/engineering/to-spec"
---

# Specify

Turn the selected capability into agreed behavior and acceptance. Interview only where decisions remain unresolved; synthesize directly when current context is settled.

Stay on the observable side: what users and other systems can see and rely on, including an external contract such as a public API or an event others consume. How the code delivers it (modules, internal interfaces, the data model, technology) is out of scope; capture a technical idea the user raises as a note for the capability's blueprint, not as agreed behavior.

The documents and their rules are in [PROJECT-DOCUMENTS.md](PROJECT-DOCUMENTS.md); its terms (authorized, obligation, lazy, pointer) apply throughout, with full changelog records.

## Gather and reconcile

Inspect the conversation, applicable instructions, the domain outline (`documentation/outline.md`), system-wide and capability requirements, existing specifications, backlog, working state, glossary, and relevant code. Fetch the full body and comments of referenced remote records when they are relevant inputs.

Identify the selected capability and account for every applicable requirement. Reuse existing agreements. A missing blocking decision stays explicit and open until the user settles it.

## Resolve the frontier

Settle only the unresolved decisions needed to complete the selected scope, through the [interview method](INTERVIEW.md).

When a term is fuzzy, disputed, or clashes with the glossary or the code, raise it before carrying on: name the conflict, test it with a concrete scenario, recommend a canonical term, and once the user agrees, write it to the glossary following [GLOSSARY-FORMAT.md](GLOSSARY-FORMAT.md). Reading the existing vocabulary needs none of this.

Agree observable acceptance and validation. Separate checks an agent can perform from any necessary human acceptance.

When building something would settle a question better than discussion (an interaction to try, a feasibility doubt), say so and propose a separately scoped prototype; keep the question open until its evidence is in. Useful validated prototype code may later be productionized; exploratory success alone does not establish production readiness.

## Synthesize and maintain

Record newly established obligations in the capability's requirements, or the system-wide requirements when they bind more than this capability, following [REQUIREMENTS-FORMAT.md](REQUIREMENTS-FORMAT.md), and point to them from the specification.

Write or update `documentation/capabilities/<capability>/specifications.md`. Include the problem and intended outcome, agreed behavior and relevant edge cases, external contracts, acceptance and validation, requirement references, dependencies on other capabilities, and explicit exclusions. Complete this scope without demanding an exhaustive specification for future product work.

Use the glossary's terms. Unresolved proposals belong in the draft, not among agreed behavior.

Record authorized agreements in the changelog, and keep the backlog and working state current. When the specifications are new and the domain outline lists capabilities, add this capability's line there or link its specifications from it.

When you create the project's first capability specifications, add one line saying where capability specifications live and when to read them to the nearest `AGENTS.md`, and a link to `documentation/capabilities/` where the root `README.md` lists the project's documentation (adding a short Documentation section if there is none). Do the same for any other document you create, such as the changelog or backlog. Check for an existing line first.

With no user to answer (a subagent run), write nothing as agreed: return the draft and the open decisions, each with its recommendation.

Report the canonical paths, covered requirements, agreements, unresolved blockers, and validation still needed. The scope is specified when its necessary decisions are authorized and its behavior and acceptance are coherent; if blockers remain, report partial progress honestly.
