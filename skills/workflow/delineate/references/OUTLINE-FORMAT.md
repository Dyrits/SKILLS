# Domain outline format

The domain outline (by default at `documentation/outline.md`; `AGENTS.md` names where it actually lives) says what the system is for in functional terms: its purpose, its actors, its domain contexts, and its capabilities. It names no technology, structure, or design. Requirements live in the requirements document and terms in the glossary; the outline links to them instead of repeating them.

## Structure

```md
# {System name}

{Purpose, one paragraph: the problem, who has it, and what success looks like for them.}

## Actors

- **{Actor}**: {who or what it is, and what it comes to the system for}

## Contexts

- [{Context}]({path to that context's glossary}): {what the context covers}

### Relationships

- **{Context} → {Context}**: {what passes between them, in domain terms}

## Capabilities

- **{capability-name}**: {one line: the lasting behavior it covers}

See also the [requirements]({path from AGENTS.md}) and the [glossary]({path from AGENTS.md}).
```

## Rules

- **Contexts only when there are several.** A context is an area where each word keeps one meaning; split only when the same word means different things in different parts of the system ("order" in sales and in the warehouse). With one context, leave the section out and keep one glossary. With several, each context keeps its glossary in a `documentation/` folder beside its code, linked from this section.
- **A capability is anything with lasting agreed behavior**: a user-facing feature, an integration, an infrastructure area, or a concern such as security. Name it with a kebab-case noun phrase built from glossary terms (`order-checkout`, `invoice-export`), never after a ticket, date, technology, or version. When the capability has specifications that `AGENTS.md` leads to, link them from its line.
- **A name is fixed once anything references it.** Renaming a capability means moving its folder and updating every link, with the user's approval.
- **The capability list is a map, not a plan.** It says what the system does or is agreed to do. Candidates, priorities, and deferrals belong in the backlog.
- **Use glossary terms throughout.** A word the outline needs that the glossary lacks is a term to settle.
