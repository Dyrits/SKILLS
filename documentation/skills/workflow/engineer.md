Fork-specific skill, added by [architecture decision record 0006](../../architecture-decision-record/0006-describe-systems-and-capabilities-functionally-and-technically.md). Its module vocabulary and its deepening and design-it-twice references derive from upstream `codebase-design`, which this fork once shipped as `design-modules`.

## What it does

`engineer` designs how one capability is built before it is implemented: its modules and their interfaces, the data it owns, the seams where behavior varies, and the interface each acceptance test drives. It works inside the system's architecture and against the capability's specifications, and writes no production code.

Its defining constraint is traceability: every acceptance criterion and every applicable requirement ends up traced to the module that delivers it and the interface its test drives. A criterion no module covers is a visible gap, not a surprise during implementation.

## When to reach for it

Type `/engineer`, or an agent can reach for it when a task fits. The description excludes plain "build this" requests: it designs, it does not implement.

| The situation | The move |
| --- | --- |
| A capability is specified and you want its technical design agreed before building | `engineer` |
| You want a feature's modules, interfaces, or data model worked out | `engineer` |
| The capability's behavior is not agreed yet | [specify](./specify.md) |
| The system's stack or parts are in question | [architect](./architect.md) |
| The design is obvious from the existing code | Skip it and implement |
| Existing code is full of shallow modules, independent of any one capability | [improve-codebase-architecture](../upkeep/improve-codebase-architecture.md) |

## What it writes

| Document (default location) | Holds |
| --- | --- |
| `documentation/capabilities/<capability>/blueprint.md` | The approach, modules and interfaces, data, seams, and tables tracing acceptance criteria and requirements to modules |
| Architecture decision records | A capability-level choice that clears the bar, or a proposed change to the architecture |

Paths are defaults: the skill first uses the document `AGENTS.md` names. When there is none, it adopts an existing home of that kind in your project, creates one at the default only when nothing matches, never overwrites an existing file, matches the naming and style of the documents it finds, and adds its line to `AGENTS.md`.

## Deep modules

The blueprint uses one vocabulary throughout: a **module** has an **interface** (everything a caller must know) and an **implementation**; it is **deep** when a lot of behavior sits behind a small interface; a **seam** is where behavior can vary, filled by **adapters**. A seam earns its place only when at least two adapters exist, usually production and test. When a central interface has no clear best shape, it can design it several radically different ways in parallel and compare them.

## Common questions

**Why is this separate from `specify`?**
Specifications say what users and other systems can observe; the blueprint says how the code delivers it. Keeping them apart lets the behavior be agreed by people who do not care about the code, and lets the blueprint change without reopening the agreement. An external contract other systems rely on, such as a public API, is observable, so it stays in the specification.

**What if the design needs something the architecture does not allow?**
It stops on that decision, writes a decision record with status `proposed`, explains the conflict, and carries on only with what does not depend on it. Once you accept the record, it updates the architecture document to match.

**Can it run without specifications?**
Yes. It asks for the behavior and acceptance the design must serve, records them under "Assumed behavior" in the blueprint, and reports that the capability has no agreed specifications.

**Do I need it for every capability?**
No. Skip it when the design is obvious from the existing code. It pays off when several modules, a new data model, or a new integration are involved.

## It's working if

- Every acceptance criterion in the specifications appears in the blueprint's acceptance table with a module and a test seam.
- Interfaces list their error modes and invariants, not only their method names.
- A conflict with the architecture shows up as a proposed decision record, not as a quiet divergence.
- No production code was written.
- `AGENTS.md` and the root `README.md` each gain one line for every kind of document it creates for the first time, and no duplicate when one exists.

## Where it fits

`engineer` is the technical half of the capability level, after [specify](./specify.md) and before [taskify](./taskify.md) or [implement](./implement.md). [architect](./architect.md) sets the shape it works inside.
