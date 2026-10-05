Upstream skill: `wayfinder`, verified in the [archived domain model](../../../.upstream/CONTEXT.md). Renamed `graphify` in this fork to emphasize the decision graph rather than imply a diagram generator.

## What it does

Builds and works through a shared decision graph for an effort too large for one session. Its nodes are questions, and its blocking relationships determine which questions can be resolved next. It plans the route to a named destination rather than decomposing the destination into implementation tasks.

The map is an index. It holds the destination, unresolved fog, boundaries, and links to resolved decisions. Each child task owns its question, answer, rationale, and evidence. Agreed living behavior, design, and acceptance belong in the repository's canonical specification, not in a competing map or remote task body. A diagram may display this graph; it does not replace the records.

## When to reach for it

Run `/graphify`, or let an agent or another skill reach for it when a large uncertain effort needs mapping.

| Situation | Use |
| --- | --- |
| The idea spans several sessions and the route is unclear | Chart a map |
| A map already exists | Name the map and optionally the next decision task |
| The route is clear and implementation needs decomposition | Use [taskify](../workflow/taskify.md) |
| One conversation can settle the question | Use [refine](../reference/refine.md) |

The tracker configuration must exist. If it is absent, run [setup-ai-workspace](../setup/setup-ai-workspace.md) yourself first.

## The frontier and the fog

The frontier consists of unresolved, unblocked, unclaimed child tasks. Claims and blocking use native tracker relationships where available. A local map uses `documentation/capabilities/<capability>/map.md` and `tasks/NN-slug.md`, with progress and blocker metadata in the task bodies.

The fog is in-scope work whose question is not precise enough yet. A sharp question becomes a task even when blocked. Work beyond the destination goes under Out of scope, not in the fog.

Task types are research, prototype, refine, and prerequisite action. Research can run in parallel. Human-in-the-loop decisions require the human's live answers; other sessions resolve one decision task at a time.

## Common questions

**Are these implementation tasks?**

No. A decision task asks what must be settled before implementation. The prerequisite-action type performs work only to unblock a decision. An effort can explicitly approve execution in its Notes; otherwise the map ends when the route is clear. Selected constraints and requirements remain binding, and unresolved decisions do not authorize speculative implementation.

**Where does the map live?**

On the configured tracker. Local maps live in the folder of the capability they will become and can be referenced from `documentation/backlog.md`. Remote maps retain native parent-child and blocking relationships. With a remote tracker, that backlog document contains only the tracker name and link; priorities and deferrals are authoritative remotely. Unpublished work stays in local execution context pending authorization. Only a local tracker keeps candidate bodies in the local backlog. Optional local references to published remote tasks contain titles and links rather than copied bodies.

**Does charting authorize publishing a remote map?**

An explicit request to chart authorizes the relevant map, child tasks, and blocking operations on the configured tracker. Working through that map authorizes the relevant claim and resolution updates. A generic local documentation request does not authorize remote publication or unrelated tracker changes.

**Which tracker labels does it use?**

`graphify:map` for the map and `graphify:<type>` (`research`, `prototype`, `refine`, `task`) for its decision tasks. Maps created by the upstream `wayfinder` skill carry `wayfinder:` labels; graphify does not read those.

**When should I use prioritize or taskify instead?**

Graphify is for an effort where what to build is still undecided and settling it takes research, prototypes, or interviews across several sessions. When what to build is known and the question is which outcome comes first, use prioritize. When the behavior is agreed and needs splitting into delivery work, use [taskify](../workflow/taskify.md).

**Will I get a visual representation?**

The default output is the decision graph's records and map. At the end, Graphify asks once whether you want a visual representation. If you accept or already requested one, it uses [illustrate](../productivity/illustrate.md) to choose a small inline or HTML view without requiring a new file. The view explains recorded titles, dependencies, resolution state, and evidence, with not-yet-sharp questions shown separately. It does not invent edges, replace the authoritative graph, or grant remote publication permission.

**How does it update specifications?**

Requirements remain constraints, unresolved proposals belong in `draft.md`, and agreed behavior/design/acceptance update `specifications.md`. Decision rationale stays on its task and is linked, not copied.

**What if a skill it calls or hands over to is not installed?**
It names the missing skill with its install command, carries out that step from its stated intent, and tells you the step ran without it. Without `document` it waits instead, because its rules use that skill's terms: install it, or tell it to proceed anyway. When it tells you to run a skill you don't have, it gives the install command with it. The skills involved are listed at the top of its [`SKILL.md`](../../../skills/shaping/graphify/SKILL.md).

## It's working if

- You can name the destination and see which decision can be taken next.
- Narration and map entries use linked titles rather than unexplained identifiers.
- Each resolved question retains its answer, rationale, and evidence and reveals the next frontier without pre-slicing vague fog.
- One human decision is resolved per session, except parallel research.
- The living specification reflects agreements, and resumption context identifies active work.

## Where it fits

Graphify is a shaping workflow for multi-session uncertainty. It uses [document](../reference/document.md) for shared project documents and hands a clear route to [specify](../workflow/specify.md) or [taskify](../workflow/taskify.md). [Guide](../productivity/guide.md) routes the surrounding flow.
