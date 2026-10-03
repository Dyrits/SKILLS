---
name: iterate
description: Build a living application one verified batch at a time, settling decisions just in time and recording them as you go.
disable-model-invocation: true
argument-hint: "An idea to build, or an existing project to continue"
---

# Iterate

Coordinate refinement and implementation in one living development workflow. An **increment** is a coherent change validated against agreed behavior. Group related decisions into a **batch**, implement it, and let the result decide what comes next. Settle decisions **just in time**: the ones the current batch needs, and no further. The application evolves in place from its first runnable batch; replacing it is a consequential decision for the user.

Call the Skill tool with "document"; its terms (authorized, obligation, lazy, pointer) and rules apply throughout. This workflow runs on `documentation/backlog.md`, `documentation/work-in-progress.md`, and the root `CHANGELOG.md` with light records, and links existing requirements and specifications where they apply.

The supporting skills named here ship with this repository. If one is missing, do its work inline and say which one was missing.

When the user corrects the agent, the approach goes off course, or the user expresses uncertainty about the process, read [ARTIFACTS.md](ARTIFACTS.md) and capture the feedback promptly, including before the first batch.

## 1. Establish the starting point

Read applicable repository instructions, startup and verification configuration, relevant requirements and specifications, and the project documents. Inspect code and decisions before asking questions the workspace can answer.

When working state names an approved focus, resume it with its constraints and prerequisites.

For a new project, establish who will use it, where it runs, whether it keeps important data, and the first useful interaction. Ask only what choosing an approach and the first batch requires. For an existing project, keep its current approach and recover the pending batch.

When competing capabilities, unclear scope, or cross-cutting dependencies make choosing a useful batch premature, call the Skill tool with "prioritize" with the known direction, constraints, and document pointers, and tell the user why. Implement once the user approves its recommended focus and material deferrals. A clear small change goes straight on. Return to this branch when priorities or dependencies block the next batch; each new outcome needs its own approval.

Completion: intended use, immediate constraints, and the next decisions are explicit. Unrelated future behavior may remain open.

## 2. Agree the technical approach

For a new project, present a short list of suitable approaches, each with its advantage and cost, and recommend one. Select for explicit structure, early meaningful error detection, visible failure handling, testing support, documentation access, setup effort, and maintenance cost; popularity is supporting evidence only. Drop approaches whose weak checking or hidden failures would undermine the agreed verification.

When a consequential choice depends on external facts (framework capabilities, diagnostics, setup requirements), call the Skill tool with "research" with the specific question and constraints. Continue independent work meanwhile; decide dependent choices once its cited findings arrive.

Get approval of the approach and its consequences before setup. Make the first batch a small useful interaction that demonstrates the approach and its executable checks, started by one command in the project's natural tooling.

For an existing project, revisit the approach only when it cannot meet a concrete need, and compare improving it with replacing it before recommending a migration.

Completion: an approved approach, or a suitable existing one, with the first batch defined. The first trial becomes the application unless the user agrees to discard it.

## 3. Settle one batch

Call the Skill tool with "refine", rooting its design tree in the **current batch**: traverse only the decisions needed to implement and verify it, and record later branches as pending. A confirmed batch proceeds while future questions stay pending. Continue the larger interview as increments reveal new questions.

Group questions that affect the same behavior or code. Keep exploration, agent recommendations, and user decisions distinct; implement an alternative once the user chooses it. Keep deferred in-scope questions apart from ideas the user ruled out; a ruled-out idea returns only through an explicit scope change.

Summarize the batch's behavior, scope, verification, and choices needing approval. A direct, unambiguous request confirms scope; otherwise ask. Define checks at the observable interface, including persistence or failure behavior when relevant, and plan user review where appearance or interaction needs judgment.

In a versioned project, record the goal's starting revision when its first batch is agreed. When a batch starts an agreed milestone or substantial structural or data-risk work, read [MILESTONE-REVIEW.md](MILESTONE-REVIEW.md) before implementation.

Call the Skill tool with "model-domain" when sharpening domain terms, recording a consequential decision, or establishing judgment-call guidelines, and with "design-modules" when a module's interface or testability needs design.

Completion: the batch can be implemented and checked without guessing at an open decision. Record the agreed batch and pending questions using [ARTIFACTS.md](ARTIFACTS.md).

## 4. Implement and verify

Implement the settled batch, preserving accepted behavior. Prefer targeted edits over regenerating unchanged code or documents. Put mechanical conventions in formatter, compiler, and lint configuration; keep `GUIDELINES.md` for judgment those tools cannot enforce. Comments capture reasons and constraints the code cannot show.

When a batch is built test-first or adds integration tests, call the Skill tool with "test-first" before writing them, using the test interfaces agreed in step 3. Keep the evidence: a meaningful red check, then green.

Call the Skill tool with "debug" for a resistant failure instead of stacking speculative fixes, and with "webapp-testing" when browser interaction is needed.

Delegate a bounded task when it benefits from a fresh context; a small edit is usually cheaper locally. Give a worker the agreed behavior, document pointers, edit scope, and verification criteria. Keep overlapping edits sequential. Continue independent questions while work runs; hold dependent ones until the result arrives. When feedback changes a running assignment, update or stop it, then check the returned work against the revised agreement.

Run relevant checks and exercise the result the way it will be used. A passing build is evidence of correctness; intended behavior and appearance need their own checks or user review. For new or changed setup, document and run the startup command and early-error checks.

Completion: the batch is implemented, its verification evidence is recorded, and failed or missing checks are stated. Blocked setup is reported as incomplete. Update progress through [ARTIFACTS.md](ARTIFACTS.md).

## 5. Validate and continue

Report what changed, the verification result, and how to run or inspect it. The agreed checks validate routine internal changes. For appearance, interaction, or open preferences, ask the user to accept the runnable result, grouping related changes into one review. Keep "implemented and checked" distinct from "accepted by the user".

At an agreed milestone, before delivery, or after substantial structural or data-risk changes, read [MILESTONE-REVIEW.md](MILESTONE-REVIEW.md) and review the related increments together.

A review gap in already approved behavior becomes the next batch. Other findings become deferred in-scope work or out-of-scope ideas; a new product choice or change of approach needs approval first. Once validation and any required review are complete, mark the increment complete, prune finished working notes, and return to the next ready decisions. End when the user's current goal is met or they pause, reporting the remaining work.

Completion: acceptance is recorded where needed, working state supports resumption, and the next step or stopping point is clear.

## Approval and cost boundaries

The user owns intended behavior and consequential tradeoffs; routine implementation choices within the agreed approach are delegated. Ask before paid services, publishing, destructive actions, or replacing the approach.

When setup, migration, repeated failures, or unexpected work materially increases scope or cost, pause: report what works, the blocker, and the alternatives, recommend continuing, simplifying, or changing approach, and wait for the decision. Quote measured costs when available, and only measured ones.

Call model-invoked supporting skills through the Skill tool; ask the human to run user-invoked ones. Record feedback about reusable skills or tools for a separate session and keep this run on the application.
