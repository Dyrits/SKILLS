Fork-created skill with no upstream equivalent, added in commit `b05ce86` under the name `divide-and-conquer` and renamed `prioritize` in this fork (the name now belongs to the former `implement-all`) (see the [provenance audit](../../research/2026-10-03-retained-skill-provenance.md)).

## What it does

`prioritize` decomposes a large or tangled idea into outcomes, recommends one focus to build next, and keeps the rest in the backlog. Its output is direction, a lightweight backlog, and an approved or explicitly pending focus. It edits planning documents only; application code, dependencies, and external trackers belong to other workflows.

It groups ideas into vertical outcomes such as "members can book a slot", not layers such as "all database work". Uncertain areas stay coarse, dependencies are marked confirmed or suspected, and a consequential external unknown gets a bounded research question, run with the skill's own copy of the [research](./research.md) steps. Captured ideas stay at description level: tasks, estimates, and requirements come later.

## When to reach for it

Type `/prioritize`, or an agent can reach for it when competing capabilities, unclear scope, or dependencies block choosing the next increment. A clear small change skips it.

Four skills border each other on decomposition.

| Situation | Use |
| --- | --- |
| The design is undecided and settling it needs research, prototypes, or interviews over several sessions | [graphify](./graphify.md) |
| What to build is known, but several candidate outcomes compete and the question is which comes first | `prioritize` |
| Agreed behavior needs splitting into delivery tasks with acceptance criteria | [taskify](../workflow/taskify.md) |
| One decision or plan needs stress-testing | [interview](../shaping/interview.md) |

It ends with the approved focus recorded in the backlog and working state; it does not start or suggest the build.

## The backlog

The backlog owns grouping, priority, dependencies, and deferrals; working state owns progress on the selected work. Both are found through `AGENTS.md`. The skill carries its own copy of the rules for these documents.

| Section | Holds |
| --- | --- |
| Direction | Intended outcome, constraints, pointers to decisions and requirements |
| Outcomes | Heading, intended result, why it matters, prerequisites, status |
| Out of scope | Ideas you excluded, with reasons when known |

Each outcome is a candidate, approved now, approved for later, or deferred. With a remote tracker, its backlog informs grouping, and a scoped proposal stays in working state until publishing is authorized.

## Common questions

**Does approving a focus approve the next outcome too?**

No. Each outcome needs its own approval. Replacing active work needs your explicit confirmation and keeps the replaced work's resumption information.

**Is a backlog candidate a requirement?**

No. A candidate is neither a requirement nor authorization to implement.

**What if a prerequisite blocks everything?**

It recommends resolving that bounded question first, and names it as a blocker with its pending question.

## It's working if

- You can tell what to pursue now, what waits, and what needs approval without rereading the conversation.
- Every raised idea is a candidate, approved, deferred, or excluded.
- Exactly one focus is approved, or the proposal and its open decision are stated as pending.
- No tasks, estimates, or code appear.

## Where it fits

This is a shaping step before building. Use [graphify](./graphify.md) when the question is design, [taskify](../workflow/taskify.md) once behavior is agreed, and [interview](../shaping/interview.md) for single decisions; it carries its own interview and research steps. [guide](../productivity/guide.md) maps the whole system.
