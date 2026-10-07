Upstream skill: `triage`, verified at revision `d81f3a1`.

## What it does

Moves intake tasks through category and state roles, verifies the request against the codebase, and records an actionable next step. Remote tasks and local task bodies follow the same state machine. External pull requests can be included when the tracker configuration enables them.

The **ready brief** is the authoritative task-execution contract. It links to the repository's canonical living specification and applicable requirements rather than replacing them. A rejected enhancement leaves durable reasoning in `documentation/out-of-scope/`; a temporary deferral belongs in the project backlog.

## When to reach for it

Run `/triage`, or let an agent or another skill reach for it when requests need verifying and classifying.

| Situation | Request |
| --- | --- |
| You need the intake queue | Ask what needs attention |
| A task or external PR needs evaluation | Name it for triage |
| You have decided its next state | Request the state change |
| You need actionable work to assign | Ask what is ready |

Triage needs the tracker and role mappings that [setup-ai-workspace](../setup/setup-ai-workspace.md) writes. When they are absent, triage says which file is missing and stops.

## The intake machine

Every triaged item has one category, `bug` or `enhancement`, and one intake state:

| State | Meaning |
| --- | --- |
| `to-evaluate` | Evaluation is needed |
| `on-hold` | A named reply, dependency, or blocker is outstanding |
| `ready` | A brief defines actionable work |
| `not-planned` | Closed without action, with a reason |

These states describe actionability, not delivery progress. Local task bodies use `Category:` and `Status:`, with conversation under `## Comments`. Remote state lives on the remote record; a local title/link reference does not copy that state.

## Common questions

**Does ready mean an agent must do the work?**

No. The brief identifies work that needs a human and explains why. The same role also applies to a PR whose next step is clear.

**Is an already-implemented request a rejection?**

No. Close it with evidence of the existing implementation. The rejection knowledge base is for rejected enhancements, not built behavior or temporary pauses.

**Can triage change requirements or publish without asking?**

Requirements constrain the work. Triage can change an implementation approach within scope, but must surface a conflicting obligation. Remote comments, role changes, and closing follow the explicit triage request or confirmed outcome. General local document upkeep grants no remote publication permission.

**What if a task has two conflicting state labels?**
Triage shows both with their source and date, recommends the one the latest evidence supports (the newest comment, the linked pull request's status), and applies no role until the maintainer picks.

## It's working if

- Each intake item has one category and one state, with conflicting states raised before action.
- On-hold notes name a condition a later session can check.
- Ready work has concrete acceptance criteria, a specification link, and a validation plan.
- Deferred candidates and actual rejections are recorded separately.
- Resuming triage uses prior answers instead of asking the same questions again.

## Where it fits

Triage is periodic intake maintenance. It carries its own copies of the [interview](../shaping/interview.md) method, the glossary and decision record formats, and the rules for local specifications, backlog, active work, and the changelog. [Guide](../productivity/guide.md) routes the next step.
