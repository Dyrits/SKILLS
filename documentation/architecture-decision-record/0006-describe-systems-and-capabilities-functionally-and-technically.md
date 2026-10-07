# Describe the system and each capability, functionally and technically

Status: accepted; drafted in `delineate`, `architect`, `specify`, and `engineer`. Callers and the retirement of `design-modules` are pending, as listed under Consequences.

Planned development describes work at two levels, the **system** and each **capability**, and on each level from two sides: **functional** (what must be true, imposed from outside the code) and **technical** (how the code makes it true). One skill owns each cell:

| | Functional | Technical |
| --- | --- | --- |
| **System** | `delineate` | `architect` |
| **Capability** | `specify` | `engineer` |

`codify` stays outside the grid: conventions and their enforcement describe how the team works, not what the system is.

## Decisions

- **The functional column holds every requirement**, functional or not. An uptime target, a compliance rule, or a budget is imposed from outside the code, so the functional skill of its level records it; the technical skill of that level answers it. A requirement outranks a technical choice.
- **`delineate` outlines the system's domain**: its purpose, actors, domain contexts and their relationships, the capability map, system-wide obligations, and the glossary. It grows out of settling terms, which stays one of its branches. It writes `documentation/domain.md`, `documentation/requirements.md`, and the glossary. In a multi-context repository, `documentation/domain.md` lists the contexts and links each context's glossary, so no separate glossary map is needed.
- **`architect` decides the system's technical shape**: technology stack, structural boundaries aligned with the domain contexts, data ownership and flows, integrations, deployment, and how each system-wide obligation is met. It can assess an existing system and conclude that it should stay as it is. It writes `documentation/architecture.md` and architecture decision records.
- **`specify` covers a capability's observable behavior**: what users and other systems can see, edge cases, acceptance, and capability obligations. An external contract other systems rely on is observable, so it stays here. It writes `documentation/capabilities/<capability>/specifications.md` and no longer holds internal design.
- **`engineer` (new) designs one capability inside the architecture**: modules and their interfaces, the data model, seams and adapters, and where each acceptance test attaches. It writes `documentation/capabilities/<capability>/design.md` and no production code. A design that needs to change the architecture records a proposed decision and waits for the user instead of diverging silently.
- **Usual order**: functional before technical on each level, `delineate` then `architect` once per system, `specify` then `engineer` per capability. Under [0005](./0005-make-skills-autonomous.md) no skill requires its predecessor: each reads the artifacts that exist, asks the minimum it needs when one is missing, and reports the gap.
- **Names**: "System" rather than "Product" (leans functional, odd for a library), "Domain" (functional only, and already the glossary's word), or "Project" (includes how the team works). `engineer` rather than `design` (too generic, not visibly technical), `blueprint` (reads as a noun), or `schematize` (rare and stiff); it pairs with `architect`, and its description excludes implementation requests.
- **Bucket**: all four sit in `workflow/`, since each produces a result at the start of the planned flow. `delineate` moves there from `reference/`.

## Considered options

- **`architect` covering both system columns**: rejected. The functional outline is agreed with people who do not care about the stack, and it changes when the business changes rather than when technical constraints do.
- **Keeping design inside `specify`**: rejected. It fuses the two columns at capability level, makes the specification depend on technical choices, and leaves no place for deep-module design except a shared reference skill, which 0005 rules out as a dependency.
- **`delineate` as a separate step before every specification**: rejected. A standalone `specify` settles a disputed term itself; `delineate` is the system-level outline and the place to build or clean up the glossary.

## Consequences

- Each of the four skills carries its own copies of the interview method and of the formats it writes. Copies of the same file must stay identical; nothing checks that yet.
- `engineer` carries the deep-module vocabulary, deepening, and design-it-twice material from `design-modules`. `design-modules` is retired once its remaining callers carry their own copies.
- Skills that still call `delineate` for a disputed term keep working, since that branch remains. Skills that read `documentation/glossary-map.md`, or treat design as part of the specification, are updated in the 0005 migration.
