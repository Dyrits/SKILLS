---
name: delineate
description: Outline a system functionally (its purpose, actors, domain contexts, capability map, system-wide requirements, and glossary), settling fuzzy or conflicting terms along the way. Use when starting or reshaping a system's functional picture, when the user wants a domain outline, system requirements, or a glossary built or cleaned up, or when a term is ambiguous, disputed, or clashes with the glossary or the code.
metadata:
  forks: "mattpocock/skills/skills/engineering/domain-modeling"
---

# Delineate

Describe the system from the functional side: what it is for, who it serves, the domain contexts it divides into, the capabilities it offers, the requirements imposed on it from outside the code, and the words everyone uses for all of that. Technology, structure, and design are out of scope; name one only when a requirement imposes it, and record it as that requirement.

Take one branch:

- **Outline**: build or revise the system's functional picture. Run every section below.
- **Term**: one word is fuzzy or disputed mid-task. Run only "Challenge terms" and "Write it down" for that word, then return to the task.

## Gather

Read what exists before asking anything: `README.md`, `AGENTS.md`, and the documents `AGENTS.md` names (the domain outline, the requirements, the glossary, existing capability specifications), and the code's entry points and domain types. A kind of document `AGENTS.md` does not name does not exist yet; when you notice a likely one it does not name, mention it in your report instead of using it. Draft every section of the outline from that evidence, marking each claim as stated by a document or inferred from the code.

## Outline

Settle the draft with the user through the [interview method](references/INTERVIEW.md), recommending an answer from the evidence for each question:

- **Purpose**: the problem, who has it, what success looks like.
- **Actors**: the people and external systems that use the system or that it relies on.
- **Contexts**: one for most systems; propose a split only where the same word means different things in different parts.
- **Capabilities**: each lasting area of agreed behavior, one line each.
- **Requirements**: the system-wide obligations, each with its source. Ask about the kinds users forget: availability, performance, data location and retention, security, compliance, budget, and anything a client or contract imposes.

Formats: [OUTLINE-FORMAT.md](references/OUTLINE-FORMAT.md) for the outline and [REQUIREMENTS-FORMAT.md](references/REQUIREMENTS-FORMAT.md) for requirements.

## Challenge terms

Raise each of these the moment it shows up, before carrying on:

- **Against the glossary**: the user's meaning conflicts with an entry. "Your glossary defines 'cancellation' as X, but you seem to mean Y. Which is it?"
- **Against vague language**: one word covers several things. "You're saying 'account': do you mean the Customer or the User? Those are different things."
- **Against the code**: the code disagrees with the stated meaning. "Your code cancels entire Orders, but you just said partial cancellation is possible. Which is right?"
- **Against a concrete scenario**: invent an edge case that forces a boundary. "An order of three items where one has already shipped: is that a cancellation?"

When several terms are open at once, settle them in rounds through the [interview method](references/INTERVIEW.md), recommending a canonical term for each and the synonyms to avoid. Glossary format: [GLOSSARY-FORMAT.md](references/GLOSSARY-FORMAT.md).

## Write it down

Write each item as soon as it is settled, without batching: the outline, the requirements, and terms to the glossary, each in the document `AGENTS.md` names, updated in place. When it names none, first look for an existing home of that kind in the repository (judging by content, not a folder name alone, and asking when the match is unclear), and use the default only when nothing matches; never overwrite, but adopt a file already at the target and add to it in its own style, and give new files and entries in an adopted home the neighbouring documents' naming, numbering, and template. The outline's default is `documentation/outline.md`; the requirements' and glossary's are in their formats. Create a document only when it has content, and a folder with its first document.

To clean up an existing glossary, propose a home for every entry that is not a term: a requirement to the requirements, agreed behavior to its capability's specifications, a technical decision reported to the user. Sharpen the terms that stay. Move nothing without the user's approval.

When you create a document (the domain outline, the requirements, a glossary), add one line naming it and when to read it to the nearest `AGENTS.md`, and a link to it where the root `README.md` lists the project's documentation (adding a short Documentation section if there is none). Check for an existing line first.

With no user to answer (a subagent run), write nothing as agreed: return the draft and the open questions, each with its recommendation.

Completion:

- **Outline**: every section is settled and written, or listed as open with its recommendation; every requirement names its source; every project-specific term the outline uses is in the glossary.
- **Term**: the settled term is in the glossary, and nothing but terms was written there.
