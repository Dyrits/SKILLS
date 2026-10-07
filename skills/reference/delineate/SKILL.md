---
name: delineate
description: Settle what the project's words mean by challenging fuzzy or conflicting terms against the glossary, the code, and concrete scenarios, then have the agreed terms written to the glossary. Use when a term is ambiguous, disputed, or clashes with the glossary or the code, or when the user wants to build or clean up the glossary.
metadata:
  forks: "mattpocock/skills/skills/engineering/domain-modeling"
---

# Delineate

Make sure the user, the agent, and the code mean the same thing by the same word. Left alone, an agent picks a meaning silently and moves on, and one word ends up meaning three things across the project. Reading the glossary for vocabulary is not this skill; any skill can do that. This skill is for changing what a word means.

**Calls:** `document`, `interview`.

## Challenge the term

Raise each of these the moment it shows up, before carrying on with the task:

- **Against the glossary**: the user's meaning conflicts with an entry. "Your glossary defines 'cancellation' as X, but you seem to mean Y. Which is it?"
- **Against vague language**: one word covers several things. "You're saying 'account': do you mean the Customer or the User? Those are different things."
- **Against the code**: the code disagrees with the stated meaning. "Your code cancels entire Orders, but you just said partial cancellation is possible. Which is right?"
- **Against a concrete scenario**: invent an edge case that forces a boundary. "An order of three items where one has already shipped: is that a cancellation?"

When several terms are open at once, call the Skill tool with "interview" to settle them in rounds, recommending a canonical term for each and the synonyms to avoid.

## Write it down

When a term is settled, write it to the glossary right there, without batching: call the Skill tool with "document" for the glossary. The glossary holds terms only; behavior, constraints, and decisions the conversation produced go to their own documents through the same call.

To clean up an existing glossary, move every entry that is not a term (implementation detail, agreed behavior, a constraint, a decision) to its home through "document", and sharpen the terms that stay. Move nothing without the user's approval.

Completion: every term settled in the session is in the glossary, and nothing but terms was written there.
