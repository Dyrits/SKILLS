---
name: prioritize
description: Decompose a large or tangled idea into outcomes, recommend one focus to build next, and keep the rest in the backlog. Use when competing capabilities, unclear scope, or dependencies block choosing the next increment, or when asked to break down an idea or revisit a backlog.
---

# Prioritize

Shape a large effort into outcomes pursued one at a time: keep the larger direction and deferred ideas, and select one useful focus. The output is direction, a lightweight backlog, and an approved or explicitly pending focus; implementation stays with the caller. A standalone run ends with the proposed next step: tell the user they can run `/iterate` to build it.

The open question here is which outcome comes first. When the effort instead hinges on design decisions that need research or prototypes over several sessions before anything can be prioritized, tell the user `/graphify` fits better.

Call the Skill tool with "document"; its terms (authorized, obligation, lazy, pointer) and rules apply throughout. This skill works on the backlog, working state, and the changelog, and links existing requirements and specifications.

**Calls:** `document`, `interview`, `research`.

## 1. Recover the direction

Read applicable instructions, relevant code, requirements, specifications, decisions, and the project documents. Reconcile actual progress before reprioritizing existing work. Inspect available facts instead of asking the user to repeat them.

Establish the intended outcome, users, constraints, and exclusions. Call the Skill tool with "interview", rooting its design tree in **choosing the next focus**.

Completion: outcome, users, constraints, and exclusions are explicit, and every focus-blocking question is identified. Unanswered choices stay pending; detailed future behavior may stay open.

## 2. Group outcomes and dependencies

Group related ideas into recognizable user or project outcomes: vertical results such as "members can book a slot", in place of layers such as "all database work". Keep uncertain areas coarse; a possible future capability gets a short description.

Identify prerequisites that could invalidate early work: shared data needs, access rules, feasibility of a critical integration, or constraints affecting several outcomes. Mark each dependency as confirmed or suspected, and investigate the ones that affect choosing the focus.

For a consequential external unknown, call the Skill tool with "research" with a bounded question. Continue independent shaping meanwhile, and decide dependent priorities once the evidence arrives. An unknown that stays unresolved remains a named blocker with its pending question.

Completion: candidate outcomes, dependencies, and major unknowns are visible, with cycles and unresolved shared prerequisites stated.

## 3. Retain the backlog

With a local tracker, keep the backlog lightweight:

- **Direction**: intended outcome, constraints, and pointers to consequential decisions or relevant requirements.
- **Outcomes**: each with a descriptive heading, intended result, reason it matters, known prerequisites or open questions, and a status.
- **Out of scope**: ideas the user has excluded, with reasons when known.

Mark each outcome as a candidate, approved now, approved for later, or deferred, with a pointer to its approval. A completed outcome keeps a pointer to its result. With a remote tracker, read its backlog for grouping and priorities, and keep a scoped proposal in working state until its publication is authorized.

The backlog owns grouping, priority, dependencies, and deferrals; working state owns the selected work's progress. Keep a known blocked outcome distinct from an idea still too vague to decompose.

Completion: every raised idea is a candidate, approved, deferred, or excluded, with uncertain facts labeled. Captured ideas stay at description level; tasks, estimates, and requirements belong to later workflows.

## 4. Recommend one focus

Recommend the smallest coherent outcome that advances the product and yields useful evidence. Explain its value, prerequisites, what is deferred, and what would change the recommendation. Offer alternatives when a real tradeoff needs the user's judgment. If a prerequisite still blocks, recommend resolving that bounded question first.

The user approves the focus and material deferrals, through an answer or an explicit request. Then record the selected backlog heading or remote pointer, the approval, constraints, and remaining prerequisites in working state, keeping existing progress and open questions. Replacing active work needs the user's explicit confirmation and keeps the replaced work's resumption information. Record the approval as an Agreement when it changes scope or priorities.

Completion: one focus is approved, or the proposal and its open decision are explicitly pending.

## 5. Return or reconsider

Return the selected outcome, document pointers, approval status, prerequisites, and next open decisions to the caller. In `iterate`, batch refinement continues after the focus is approved. This skill edits planning documents only; application code, dependencies, and external trackers belong to other workflows.

Reconsider priorities when new evidence, conflicting goals, or changed constraints make the selection unsuitable, updating only the affected entries. Each next outcome needs its own approval.

Completion: the caller or user can tell what to pursue now, what waits, and what still needs approval without rereading the conversation.
