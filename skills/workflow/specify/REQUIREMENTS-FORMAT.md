# Requirements format

A **requirement** is an obligation imposed on the product from outside the code: by users, legal, operations, a client, a budget, or the company. It binds the product whatever the implementation, functional or not: "every export is logged with the account identifier", "99.9% monthly uptime", "personal data stays in the European Union", "hosting under 200 euros a month".

What is not a requirement:

- **Agreed behavior** of one capability (what users see, edge cases, acceptance) belongs in that capability's specifications.
- **A technical choice** (a stack, a structure, a module design) answers requirements; it is not one, unless someone outside the code imposes it ("the client mandates Azure").
- **A code convention** is the team's own choice about how code is written. A coverage floor the team picked is a convention or a tool setting; one a contract imposes is a requirement.

A requirement outranks any technical choice or convention: when they conflict, satisfy the requirement, and ask the user before relaxing either. Only the user relaxes a requirement.

## Where

Find the requirements through `AGENTS.md`, and write there. When it names none, look for an existing home of that kind in the repository first (judging by content, not a folder name alone, and asking when the match is unclear), and use the default only when nothing matches. Never overwrite: adopt a file already at the target and add to it in its own style, and give new files and entries in an adopted home the neighbouring documents' naming, numbering, and template. Then add one line for it to the nearest `AGENTS.md` and tell the user. The defaults are `documentation/requirements.md` for system-wide requirements, and `documentation/capabilities/<capability>/requirements.md` for requirements that bind one capability only, which add to the system-wide ones.

## Structure

```md
# Requirements

## {Area: Compliance, Availability, Performance, Budget, Behavior...}

- **{Short name}**: {the obligation, in glossary terms}.
  Source: {who imposes it}. Reason: {why it binds}.
  Check: {for a measurable one: the number, and the command, monitor, or acceptance step that checks it}.
```

## Rules

- **One obligation per entry**, stated as what must hold, not how to achieve it.
- **Always name the source.** An entry nobody outside the code imposed is not a requirement; send it back to the user to place.
- **A measurable requirement states its number and its check.** "Fast" is not a requirement; "search answers in under 300 ms at the 95th percentile, checked by the load test in CI" is.
- **Group under areas** once there are more than a handful of entries.
- **Never delete or weaken an entry on your own.** Mark one the user relaxed or retired as such, with the date and their reason.
