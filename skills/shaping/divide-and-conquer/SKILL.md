---
name: divide-and-conquer
description: When competing capabilities, unresolved scope, or dependencies block choosing a useful increment, organize outcomes and recommend one focus. Also use for an explicit request to decompose an idea or reconsider a backlog. Project size alone does not require decomposition.
---

# Divide and conquer

Shape a large effort into outcomes that can be pursued one at a time. Retain the larger direction and deferred ideas while selecting one useful focus. A backlog entry preserves an idea; it is not permission or a promise to implement it.

This skill produces direction, a lightweight backlog, and an approved or explicitly pending focus. Implementation remains with the calling workflow. A standalone invocation ends with the proposed next step; tell the user they can invoke `/iterate` to build it.

Call the Skill tool with "documentation" for shared project-document rules. Primarily use `documentation/backlog.md`, `documentation/work-in-progress.md`, and the root `CHANGELOG.md`. Read and respect existing relevant requirements and specifications, linking to them when useful. Neither feature specifications nor task documents are prerequisites; do not generate them merely to choose a focus or run a batch.

## 1. Recover the direction

Read applicable instructions, relevant existing code, requirements, specifications, and decisions, and the primary project documents when present. Reconcile actual progress before reprioritizing existing work. Inspect available facts instead of asking the user to repeat them.

Establish the intended outcome, users, constraints, and exclusions. When available, call the Skill tool with "refine", rooting its design tree in **choosing the next focus**, not fully specifying the application. Ask the ready questions in concise numbered rounds with recommendations, then wait for answers. Use that bounded questioning discipline locally when the supporting skill is unavailable.

Completion: the intended outcome, users, constraints, and exclusions are explicit, and every remaining focus-blocking question is identified. Unanswered choices remain pending rather than being filled with assumptions; detailed future behavior may remain unresolved.

## 2. Group outcomes and dependencies

Group related ideas into recognizable user or project outcomes, not layers such as "all database work" followed by "all UI work". Keep uncertain areas coarse. A possible future capability needs a short description, not invented acceptance criteria or implementation tasks.

Identify prerequisites that could invalidate early work: shared data needs, access rules, feasibility of a critical integration, or other constraints affecting several outcomes. Distinguish confirmed dependencies from suspected ones. Investigate only those needed to choose the focus.

For consequential external unknowns, call the Skill tool with "research" when available, with a bounded question and existing constraints. Continue independent shaping while it runs; wait for evidence before deciding dependent priorities. Respect the harness's permissions and delegation policy.

If that skill is unavailable, investigate primary sources with available reading or web tools and retain citations. If the evidence cannot be obtained, keep the unknown as a blocker and return the bounded question as pending; neither an assumed answer nor silent waiting resolves it.

Completion: candidate outcomes, dependencies, and major unknowns are visible. Cycles or unresolved shared prerequisites are explicit rather than hidden in a proposed sequence.

## 3. Retain the backlog

Follow documentation's backlog-authority rule and preserve existing content and ownership. For local tracking, retain a lightweight `documentation/backlog.md`:

- **Direction**: intended outcome, constraints, and pointers to consequential decisions or relevant existing requirements.
- **Outcomes**: each has a descriptive heading, intended result, reason it matters, known prerequisites or open questions, and an explicit status.
- **Out of scope**: ideas the user has excluded, with reasons when known.

Distinguish candidate ideas, approved work, and deliberate deferrals. Record whether approved work is selected now or retained for later, linking to its authorization in working state or lasting history. Completing an outcome may be noted with a pointer to its result rather than retaining implementation details. Suggestions remain candidates until the user approves them; the backlog itself never grants authorization.

With remote tracking, `documentation/backlog.md` contains only the authoritative backlog name and link. Read that source for grouping and priorities; this shaping skill does not silently publish or reprioritize remote records. Keep a scoped proposal awaiting publication in local working state, not a second local backlog, and report pending publication honestly.

The authoritative backlog owns grouping, relative priority, dependencies, and deferrals. `documentation/work-in-progress.md` owns the selected work's active decisions, unfinished batches, verification, blockers, assignments, and resumption details; reference local headings or remote records instead of duplicating them. A known blocked outcome stays distinct from an idea too vague to decompose yet.

Maintain affected documents autonomously within agreed scope. Resolve consequential scope or obligation conflicts rather than weakening requirements to fit a preferred priority or the current implementation.

Completion: raised ideas are accounted for as candidates, approved work, deferred work, or explicit exclusions, with uncertain facts labeled. There are no mandatory tickets, task documents, schedules, estimates, or requirements invented from a captured idea.

## 4. Recommend one focus

Recommend the smallest coherent outcome that advances the intended product and provides useful evidence, not merely the easiest task. Explain its value, prerequisites, what is deferred, and what would change the recommendation. Include alternatives only when a real tradeoff needs the user's judgment.

Get approval of the focus and material deferrals before implementation. An explicit request can supply that approval; suggestions and silence cannot. If a prerequisite is still blocking, recommend resolving that bounded question first rather than guessing or approving an entire architecture.

After approval, this skill records the selected local heading or remote reference, approval and constraints, and remaining prerequisites in `documentation/work-in-progress.md`, preserving existing progress and unresolved questions. A replacement of active work must be explicit; retain its resumption information rather than overwriting it. Pending recommendations remain proposals and do not replace the approved active focus.

Record relevant authorized decisions in the root `CHANGELOG.md` using the entry format, fields, and vocabulary supplied by "documentation". Agreement records authorized decisions; Delivery records completed relevant checks and acceptance, not merely a recommendation or mechanical document edit. Do not create an entry for every mechanical edit.

Completion: one focus is approved, or the proposal and unanswered decision are explicitly pending. The rest of the backlog can remain open.

## 5. Return or reconsider

Return the selected outcome, backlog and working-state pointers, approval status, necessary prerequisites, and next unresolved decisions to the caller. In `iterate`, continue in the same workflow with batch refinement and implementation only after focus approval. This skill itself edits planning artifacts, not application code, dependencies, or external trackers.

Reconsider priorities when new evidence, conflicting goals, or changed constraints make the current selection unsuitable. Update only affected entries and recommend the next focus when asked or when the caller reaches that decision. Completing one outcome does not authorize the next; an out-of-scope idea requires an explicit scope change.

Completion: the caller or user can identify what to pursue now, what waits, and what still needs approval without rereading the whole conversation.
