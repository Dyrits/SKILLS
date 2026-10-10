# Glossary format

A glossary holds the project's domain language and nothing else: no implementation details, specifications, or decisions. Update it the moment a term is resolved instead of batching terms up.

## Structure

```md
# {Context Name}

{One or two sentence description of what this context is and why it exists.}

## Language

**Order**:
{A one or two sentence description of the term}
_Avoid_: Purchase, transaction

**Invoice**:
A request for payment sent to a customer after delivery.
_Avoid_: Bill, payment request

**Customer**:
A person or organization that places orders.
_Avoid_: Client, buyer, account

**Task**:
A unit of delivery work with acceptance criteria.
_Avoid_: Ticket
_Why_: The tracker already uses it.
```

## Rules

- **Be opinionated.** When multiple words exist for the same concept, pick the best one and list the others under `_Avoid_`.
- **Keep definitions tight.** One or two sentences max. Define what it IS, not what it does.
- **Record why a term won in one `_Why_` line**, only when the user states why the term was chosen over a rival and the choice is easy to reverse. A hard-to-reverse choice goes to an architecture decision record instead.
- **Only include terms specific to this project's context.** General programming concepts (timeouts, error types, utility patterns) don't belong even if the project uses them extensively. Before adding a term, ask: is this a concept unique to this context, or a general programming concept? Only the former belongs.
- **Group terms under subheadings** when natural clusters emerge. If all terms belong to a single cohesive area, a flat list is fine.

## Several contexts

Find the glossary, or each context's glossary, through `AGENTS.md`. When it names none, look for an existing home of that kind in the repository first (judging by content, not a folder name alone, and asking when the match is unclear), and use the default only when nothing matches. Never overwrite: adopt a file already at the target and add to it in its own style, and give new files and entries in an adopted home the neighbouring documents' naming, numbering, and template. Then add one line for it to the nearest `AGENTS.md` and tell the user. The default for one context is `documentation/glossary.md`; with several, each context keeps its glossary in a `documentation/` folder beside its code, and one `AGENTS.md` line covers them all. When a term's context is unclear, ask.
