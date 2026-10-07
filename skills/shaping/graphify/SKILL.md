---
name: graphify
description: "Build and work through a shared decision graph for an effort too large for one session. Use when the user asks to graphify an effort or to resolve the next decision task on an existing graph."
metadata:
  forks: "mattpocock/skills/skills/engineering/wayfinder"
---

# Graphify

A loose idea has arrived, too big for one agent session, and wrapped in fog. Chart a shared decision graph toward a named **destination** and work its **decision tasks** one at a time. These are questions whose resolution is a decision, not implementation slices. The graph consists of task records and blocking relationships; a rendered diagram is an optional view, not the graph itself.

**Calls:** `delineate`, `document`, `illustrate`, `interview`, `prototype`, `research`. **Hands over to:** `/setup-ai-workspace`.

The destination might be a specification to hand off, a decision to settle before planning, or an in-place migration. It shapes every task. This workflow fits engineering and other domains with the same decision structure.

## Document and tracker contract

Call the Skill tool with "document"; its terms (authorized, obligation, lazy, pointer) and rules apply throughout, and requirements constrain the destination and every decision.

Read `.agents/issue-tracker.md` for map storage, parent-child relationships, blocking, claims, and frontier queries. If it is missing, tell the user to run `/setup-ai-workspace` and stop.

- A local map lives at `documentation/capabilities/<capability>/map.md`; its decision tasks are capability task files.
- A remote map and its children use native tracker records and relationships.
- The capability's specifications hold the agreed living behavior, design, and acceptance; its draft holds open proposals. The map indexes decisions and each task keeps its rationale.

An explicit request to chart a map authorizes creating the map, its decision tasks, and their blocking relationships on the configured tracker. A request to work through the map authorizes claiming, resolving, and closing its tasks and updating the map. Ask before any remote change outside the named effort.

## Plan, don't do

Each decision task resolves a question. The map is done when the route is clear and no decision remains before implementation. If you feel pulled to build the destination, hand off instead. An effort may explicitly include execution in its **Notes**; absent that, produce decisions, not deliverables.

The `task` type below is a prerequisite action needed to make a decision; the map stays a decision graph. Once the route is clear, `taskify` splits the agreed behavior into delivery tasks. When the decisions are already settled and the open question is only which outcome to build first, `prioritize` fits better.

## Refer by name

Refer to maps and tasks by their titles, with links wrapped in those names. Identifiers and URLs belong inside the link, not in place of a readable title. This applies to narration and Decisions-so-far entries.

## The map

The map is an **index**, not a store. It lists resolved decisions with a gist and a link to the task that owns the rationale. On a remote tracker it is a record labelled `graphify:map`, with child records. On the local tracker it is `map.md`.

Load the whole map at low resolution once per session. Open tasks are found by frontier query, not by copying their bodies into the map.

```markdown
## Destination

<what reaching the end of this map means, in one or two lines>

## Notes

<domain, skills to consult, standing preferences, any explicitly approved execution scope>

## Decisions so far

- [<resolved task title>](link): <one-line gist>

## Not yet specified

<in-scope questions not yet sharp enough to turn into decision tasks>

## Out of scope

<work beyond this destination, with reasoning and links where useful>
```

## Decision tasks

Each child holds a question sized for one 100K-token agent session:

```markdown
## Question

<the decision or investigation this task resolves>
```

Record the type using a native `graphify:<type>` label or the configured local `Type:` line. Types are `research`, `prototype`, `interview`, and `task`.

Claim the task before work, using the tracker assignee or local `Progress: claimed`. An open, unassigned remote task or unresolved, unclaimed local task is unclaimed.

Prefer native blocking relationships because they show the frontier in the tracker UI. Use the configured body convention only where native blocking is unavailable. A task is unblocked when all blockers are closed or locally resolved. The **frontier** is the open, unblocked, unclaimed children.

Record the answer, rationale, and supporting evidence on resolution rather than replacing the question. Link assets instead of pasting their contents. A specification update captures the agreed living outcome; the task retains the decision rationale.

## Task types

Each task is **HITL**, human in the loop, or **AFK**, agent-driven. A HITL task resolves only through live exchange with a human who speaks for themselves.

- **Research, AFK.** Surface an external fact a decision depends on. A subagent calls the Skill tool with "research" and links the findings.
- **Prototype, HITL.** Raise discussion fidelity with a cheap artifact to react to. Call the Skill tool with "prototype"; link the artifact as an asset.
- **Interview, HITL.** Resolve a decision through conversation. Call the Skill tool with "interview". When a term is disputed, call the Skill tool with "delineate".
- **Task, HITL or AFK.** Perform a prerequisite action that unblocks a decision, such as obtaining service access or moving data so its shape can be examined. The agent works alone where possible; otherwise it gives the human a precise checklist. The answer records what was done and resulting facts. Record credential locations, never secret values.

## Fog of war

The map is deliberately incomplete. Resolving a task reveals the next questions; add only what can now be specified.

- Create a decision task when you can state the question precisely, even if it is blocked.
- Use **Not yet specified** when the question is still too vague. One patch of fog can become several tasks or none.

Fog is in scope, toward the destination. It excludes decisions already made, live tasks, and out-of-scope work. Clear a graduated patch when its new tasks exist so it has one owner.

## Out of scope

Work beyond the destination belongs in **Out of scope**, not fog. It returns only through a redrawn destination or fresh effort.

If an existing task turns out to be outside this effort, close it and add a gist, reason, and link under **Out of scope**. Keep it out of **Decisions so far**, which records the route taken.

Record a candidate deferred to another effort in the backlog, following the "document" backlog rules. Out of scope here marks this effort's boundary; triage's `documentation/out-of-scope/` knowledge base records project-wide rejections of enhancement requests.

## Invocation

Resolve no more than one decision task per session, except parallel research tasks.

### Chart the map

The user supplies a loose idea.

1. **Name the destination.** Call the Skill tool with "interview" to settle the destination and its scope.
2. **Map the frontier.** Refine breadth-first across the space instead of going deep on one question. If there is no fog and the journey fits one session, stop and ask how the user wants to proceed.
3. **Create the map.** Fill Destination and Notes, leave Decisions-so-far empty, and sketch fog under Not yet specified. Use the configured local or remote operation.
4. **Create sharp decision tasks.** Create children first, then wire blocking in a second pass once identities exist. Keep everything still vague in the fog.
5. **Start research subagents.** For each research task, start a subagent that calls the Skill tool with "research". Capture findings on a throwaway `research/<name>` branch with a context pointer from the task.
6. **Finish.** Charting fills one session; resolving decisions starts in the next. Update the backlog pointer and working state where useful. Offer the optional visual delivery below, then stop.

### Work through the map

The user supplies a map URL, identifier, or local path. Naming a decision task is optional.

1. Load the map, relevant requirements, and canonical specification without loading every task body.
2. Use the named task, or choose the first frontier task in map order. Claim it before work.
3. Resolve it. Fetch related task bodies only as needed. Call the Skill tool for skills named in Notes. If unsure, call the Skill tool with "interview".
4. Record the answer, rationale, and evidence as a resolution comment or the configured local answer. Close or resolve the task, then append a titled context pointer to Decisions-so-far. Update agreed living specifications and remove settled proposals from the draft without copying whole task bodies.
5. Create newly sharp tasks and wire their blockers. Clear graduated fog. Close tasks beyond the destination and record them under Out of scope. Update invalidated tasks; ask before deleting historical remote records.
6. Update working state and the changelog. Offer the optional visual delivery below, then stop after this decision, leaving the next frontier visible.

Expect other sessions to update the map concurrently. Re-read relevant claim and blocker state before acting.

### Optional visual delivery

At the end of either path, ask once whether the user wants a visual representation of the decision graph. If they already requested one, proceed without asking again. If they accept or already requested it, call the Skill tool with "illustrate".

Supply actual task titles, recorded dependencies, resolution state, and evidence pointers from the authoritative graph. Show unresolved, not-yet-sharp questions separately from task nodes. Draw only recorded edges. The visual is a derived explanation; the tracker stays the source of truth. Let illustrate choose the smallest useful inline or HTML view.
