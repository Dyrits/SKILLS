---
name: iterate
description: Develop a solo project through a continuous loop of questioning, documented decisions, runnable changes, and verification, without mandatory tickets or a prototype rebuild.
disable-model-invocation: true
argument-hint: "An idea to build, or an existing project to continue"
---

# Iterate

Coordinate the interview and implementation in one session. An **increment** is a coherent change validated against agreed behavior. Group related decisions into a **batch**, implement that batch, and use the result to decide what comes next. The application evolves in place; replacing it is a consequential decision, not a graduation from prototype to product.

When the user corrects the agent, the approach goes off course, or the user expresses uncertainty about the process, read [ARTIFACTS.md](ARTIFACTS.md) and capture the feedback promptly, including before the first batch.

Check which supporting skills are available before calling them. This skill can run independently using its batch, verification, and artifact rules. Where an optional discipline is unavailable, perform the relevant work locally and report any capability that cannot be verified; an unavailable skill is not permission to skip verification.

## 1. Establish the starting point

Read applicable repository instructions, existing startup and verification configuration, and `documentation/work-in-progress.md` if present. Inspect the relevant code and decisions before asking questions the workspace can answer. Preserve existing work and respect the harness's permissions and delegation policy.

When working state references an approved backlog focus, follow that entry and recover its constraints and prerequisites rather than restarting priority selection. A proposal or an unapproved backlog entry does not authorize implementation.

For a new project, establish who will use it, where it should run, whether it retains important data, and the first useful interaction. Ask only what is needed to choose an approach and define the first runnable batch. For an existing project, prefer its current approach and recover the pending batch rather than restart the interview.

If competing capabilities, unresolved scope, or cross-cutting dependencies make choosing a useful batch premature, call the Skill tool with "divide-and-conquer" when available. Supply the known direction, constraints, and existing backlog or working-state pointers. Explain why decomposition helps; let it retain deferred ideas and recommend one outcome. The agent chooses the shaping tool, but the user approves the focus and material deferrals before implementation. Continue this workflow after approval. A clear small change skips this branch.

If that skill is unavailable, report the missing support and perform bounded local scope assessment: identify candidate outcomes, blocking dependencies, and deferred ideas, then propose one focus for approval. Installation may be suggested for later use; it does not replace the current-run fallback. An existing backlog's presence alone does not require decomposition. Revisit the branch only when priorities or dependencies prevent choosing the next useful batch, and never treat completion of one outcome as authorization to implement the next.

Completion: intended use, immediate constraints, and the next decisions are explicit. Unrelated future behavior may remain open.

## 2. Agree the technical approach

For a new project, present a concise shortlist of suitable approaches. Give each option's advantage and cost, then recommend one. Select for explicit structure, early meaningful error detection, visible failure handling, testing support, documentation access, setup effort, and maintenance cost. Popularity is supporting evidence, not the selection rule. Exclude approaches whose weak checking or hidden failures undermine the agreed verification needs.

When a consequential choice depends on external facts, such as framework capabilities, diagnostics, or setup requirements, call the Skill tool with "research" when available. Supply the specific unresolved question and existing constraints; retain cited findings under the project's documentation convention. Continue independent work while research runs, but wait for its evidence before deciding dependent choices. Research a concrete knowledge gap rather than surveying every possible stack.

Get approval of the initial approach and its consequences before setup. Make the first batch a small, useful interaction that demonstrates both the approach and executable checks. Provide one-command startup using the project's natural tooling; add a small script only when needed.

For an existing project, revisit this step only when its current approach cannot meet a concrete need. Compare improving the existing application with replacing it before recommending a migration.

Completion: an approved approach for new setup, or a suitable existing approach, with the first batch defined. A successful trial remains part of the application unless disposal was explicitly agreed.

## 3. Settle one batch

When available, call the Skill tool with "grilling" for its decision-tree, frontier, and recommended-answer discipline. Root the tree in the **current batch**: traverse only decisions needed to implement and verify that batch. Record later-application branches as pending rather than traversing them now. An open future frontier never blocks a confirmed batch.

Ask the ready questions in numbered rounds with concise recommendations, then wait for answers. Apply the confirmation gate to this batch, not the entire future application: establish shared understanding before changing its behavior. This batch-scoped discipline also applies when "grilling" is unavailable. Continue the larger interview as increments reveal new questions.

Group questions affecting the same behavior or related code. Separate exploration, agent recommendations, and user-approved decisions. An answer that raises alternatives is not permission to implement one of them. Keep deferred in-scope questions separate from ideas the user has ruled out; only an explicit scope change makes an out-of-scope idea eligible for a batch.

Summarize the batch's intended behavior, scope, relevant verification, and any choices requiring approval. A direct, unambiguous request can confirm scope; otherwise ask for confirmation. Define checks at the observable interface, including persistence or failure behavior when relevant. Include user review where appearance or interaction needs judgment.

For a versioned project, record the current goal's starting revision when its first batch is agreed, so a later delivery review has a usable baseline. When a batch starts an agreed milestone or substantial structural or data-risk work, read [MILESTONE-REVIEW.md](MILESTONE-REVIEW.md) to record its review baseline and behavior evidence before implementation.

Call the Skill tool with "domain-modeling" when sharpening domain terms, recording a consequential architecture decision, or establishing judgment-call guidelines. Call the Skill tool with "codebase-design" when a module's interface or testability needs design. Load each only when its branch is reached.

Completion: the batch can be implemented and checked without guessing at an unresolved decision. Record approved but unfinished behavior and pending questions using [ARTIFACTS.md](ARTIFACTS.md).

## 4. Implement and verify

Implement only the settled batch, preserving previously accepted behavior. Prefer targeted edits and relevant context over regenerating unchanged code or documents. Keep meaningful names and clear module interfaces. Put mechanical conventions in formatter, compiler, and lint configuration; use `GUIDELINES.md` only for useful judgment those tools cannot enforce. Comments and folder explanations capture reasons or constraints that names and code do not convey.

When a batch uses test-first development or introduces integration tests, call the Skill tool with "test-driven-development" when available, before writing those tests. Agree its observable test interfaces in the batch confirmation, then retain evidence of a meaningful failing check followed by a passing implementation. Approval of those interfaces carries into the batch; local passing tests alone do not establish that the discipline was followed.

Call the Skill tool with "debug" for a resistant failure rather than accumulating speculative fixes. Use "webapp-testing" through the Skill tool when browser interaction is needed and the skill is available.

Delegate only when a bounded task benefits from independent execution or a fresh context. Give a worker the agreed behavior, relevant artifact pointers, edit scope, and verification criteria. A subagent is optional; a small edit may cost less to do locally. Keep overlapping edits sequential. Continue independent questions while work runs, but wait for the result before asking dependent questions or building dependent changes.

If new feedback changes a running assignment, reconcile it before accepting the worker's result. Update or stop the assignment using the harness's supported mechanism, then check the returned work against the revised agreement.

Run relevant checks and exercise the result in the way it will be used. Report what was actually checked and what remains unverified. Static-check or build success is evidence about code correctness, not acceptance of intended behavior or appearance. For new or changed setup, document and successfully run the single startup command and chosen early-error checks.

Completion: the batch is implemented, verification evidence is available, and failures or missing checks are explicit. New or changed setup has a documented, demonstrated startup command and successful early-error checks; blocked setup is reported as incomplete. Use [ARTIFACTS.md](ARTIFACTS.md) to update progress and capture feedback.

## 5. Validate and continue

Present a short account of what changed, the verification result, and how to run or inspect it. Routine internal changes are validated autonomously through agreed checks. For appearance, interaction, or unresolved preferences, ask the user to accept the runnable result, grouping related changes into one review. Keep implemented-and-checked distinct from user-accepted when that judgment is needed.

At an agreed milestone, before delivery, or after substantial structural or data-risk changes, read [MILESTONE-REVIEW.md](MILESTONE-REVIEW.md) and run a bounded standards-and-behavior review before pruning its behavior evidence. Review related increments together rather than dispatching the full review process for every small edit.

If review finds a gap in already approved behavior and scope, turn it into the next bounded batch and retain previously accepted behavior. Classify other findings as deferred in-scope work or out-of-scope ideas, and obtain approval before implementing a new product choice or change of approach. Out-of-scope ideas require an explicit scope change. Once validation and any required milestone review are complete, mark the increment complete, prune finished working notes, and return to the next ready decisions. End the run when the user's current goal is met or they choose to pause; report remaining work without inventing a requirement to finish the entire application.

Completion: acceptance is recorded where needed, current state supports resumption, and the next step or stopping point is clear.

## Approval and cost boundaries

The user owns intended behavior and consequential tradeoffs. Delegate routine implementation choices within the agreed approach. Ask before paid services, publishing, destructive actions, or replacing that approach. Additional harness permissions still apply.

When setup, migration, repeated failed attempts, or unexpected work materially increases scope or cost, pause. Report what works, the blocker, and the alternatives; recommend continuing, simplifying, or changing approach, then wait for the decision. Do not silently continue across sessions. Use measured costs if available; avoid claiming a token saving or inventing a token threshold.

Keep the human-facing workflow unified. Reuse relevant available model-invoked skills through the Skill tool; user-invoked skills require the human to invoke them. Tickets, `.refinement`, and external publication are optional choices, not prerequisites. Feedback about reusable skills or tools is recorded for a separate session, keeping this run focused on the application.
