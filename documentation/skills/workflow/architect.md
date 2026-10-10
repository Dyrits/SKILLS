Fork-specific skill with no upstream equivalent, accepted in [architecture decision record 0005](../../architecture-decision-record/0005-make-skills-autonomous.md) and placed in the system-and-capability model by [architecture decision record 0006](../../architecture-decision-record/0006-describe-systems-and-capabilities-functionally-and-technically.md).

## What it does

`architect` decides how the system as a whole is built: the technology stack, the parts it runs as, which part owns which data, how the parts and outside systems talk, and where everything runs. Its defining constraint is the requirements: every system-wide requirement ends up with a line saying how the architecture meets it, or a visible gap.

It works in two branches. **Design** decides the shape of a system that is not built yet. **Assess** describes an existing system as the code shows it, tests it against the requirements, and recommends changes only where a requirement or a stated problem calls for one. Concluding that the architecture should stay as it is counts as a result.

## When to reach for it

Type `/architect`, or an agent can reach for it when a task fits:

| The situation | The move |
| --- | --- |
| Choosing a stack or high-level structure for a new system | `architect`, design branch |
| "Is our architecture still right for this?" | `architect`, assess branch |
| A new requirement (a partner's latency budget, data residency) puts the structure in question | `architect`, assess branch |
| What the system is for, or its requirements, are unclear | [delineate](./delineate.md) |
| One capability's modules and interfaces | [engineer](./engineer.md) |
| How code is written and checked | [codify](../setup/codify.md) |
| Deepening shallow modules in an existing codebase | [improve-codebase-architecture](../upkeep/improve-codebase-architecture.md) |

## What it writes

| Document (default location) | Holds |
| --- | --- |
| `documentation/architecture.md` | The shape as it stands: stack, parts, flows, integrations, deployment, and a table mapping each requirement to how it is met |
| Architecture decision records | Each choice that is hard to reverse, surprising without context, and a real tradeoff |
| `documentation/requirements.md` | Only obligations you state while it asks, when no requirements exist yet |

Paths are defaults: the skill first uses the document `AGENTS.md` names. When there is none, it adopts an existing home of that kind in your project, creates one at the default only when nothing matches, never overwrites an existing file, matches the naming and style of the documents it finds, and adds its line to `AGENTS.md`.

## Common questions

**Can it run without a domain outline or requirements?**
Yes. It asks the minimum the architecture cannot be decided without (what the system is for, who uses it and how much, what it must guarantee, what the team can run), records the obligations you state as requirements, and reports that the domain outline is missing.

**Will it push me toward microservices?**
It starts from the simplest shape that meets the requirements, one deployable part and one store, and adds parts only where a requirement or a domain context boundary justifies them. Each alternative it offers is compared against your requirements and the cost of reversing later.

**What if I prefer an option that breaks a requirement?**
It names the requirement and asks you to choose: relax the requirement, or pick differently. Requirements outrank preferences, and only you relax one.

**How is this different from `improve-codebase-architecture`?**
That skill looks for shallow modules inside the code and proposes deepening them. `architect` works a level up: the system's parts, stack, and data ownership.

## It's working if

- Every system-wide requirement has a row in the architecture document, met or with its gap named.
- Every capability in the domain outline is served by a named part, and every piece of data has one owner.
- Alternatives arrive with a recommendation and a reason, not as a menu.
- In assess, it writes down what the code actually does before judging it, and flags where older documents disagree.
- `AGENTS.md` and the root `README.md` each gain one line for every kind of document it creates for the first time, and no duplicate when one exists.

## Where it fits

`architect` is the technical half of the system level, usually after [delineate](./delineate.md) and before [codify](../setup/codify.md), since conventions depend on the stack. [engineer](./engineer.md) designs each capability inside the shape it sets.
