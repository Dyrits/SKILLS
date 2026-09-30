## What it does

`code-review-and-refactor` owns the refactor phase of red-green-refactor.
After implementation establishes the required behavior with passing tests, it reviews the changes against repository standards and the originating specifications, applies supported refactors, and verifies the result.

Standards and Specifications run in independent subagents against the same starting diff.
One coordinator checks the evidence and edits the code, then reuses those reviewers for verification.
The refactors preserve observable behavior and agreed public interfaces; missing behavior returns to the red/green implementation phase.

## When to reach for it

Type `/code-review-and-refactor`, or the agent reaches for it when the task calls for review and refactoring after implementation.
An explicit request for a report alone produces findings without edits.

| Your situation | Reach for |
| --- | --- |
| The behavior works and you want the changes reviewed and refactored | `code-review-and-refactor` |
| One concrete behavior needs building test-first | [test-driven-development](./test-driven-development.md) |
| A decided ticket or small set of specifications needs implementation and refactoring | [implement](./implement.md) |
| A complete set of specifications needs parallel implementation and a combined refactor phase | [implement-all](./implement-all.md) |
| The whole codebase needs architectural investigation | [improve-codebase-architecture](../upkeep/improve-codebase-architecture.md) |
| Something is broken and you do not know why | [debug](../upkeep/debug.md) |

## Prerequisites

Supply a fixed point such as a commit, branch, or tag.
The skill resolves it and pins the merge-base before reviewing.
When invoking it after implementation, use the commit before that work began.
The review can include committed changes, tracked work in progress, and new files belonging to the requested work.
Unrelated local changes stay outside the refactor scope.

Existing passing tests establish the behavior the refactor must preserve.
If relevant checks already fail, the skill reports that limitation before changing the affected code.

## Two axes, one refactor phase

| | Standards | Specifications |
| --- | --- | --- |
| Checks | Repository rules and a Fowler smell baseline | Requirements and agreed behavior |
| Evidence | The standards file and rule, or the named smell and relevant hunk | The requirement quoted from the specifications |
| Action | Apply supported refactors that preserve behavior | Verify requirements and report gaps that need implementation |
| Verification | Confirm the refactor resolves the finding | Confirm the refactor preserves requirements and interfaces |

Repository standards override the twelve Fowler smell heuristics.
A smell label alone does not justify a change; its finding must explain the benefit in the actual code.
The coordinator checks each finding's evidence before editing and records why it accepts, dismisses, or leaves it open.

The same reviewers inspect the resulting changes using the context they gathered during review.
This avoids repeating the initial investigation, while still checking the code after it changes.
Targeted verification addresses concrete regressions; another subjective smell suggestion does not restart the whole review.

## Common questions

**How do I publish the review?**

Invoke the experimental [publish-message](../../../skills/experimental/publish-message/SKILL.md) with the report and destination, requesting inline suggestions if wanted.
It accepts findings from any review source and asks you to approve the complete publication before posting.
Verified local refactors are described as completed in the destination branch only after checking that the destination contains them.

**Where did `/code-review` go?**

It is now `/code-review-and-refactor`.
The name makes the editing phase explicit and gives this skill a distinct command from other skills named `code-review`.
The old repository entrypoint is removed.

**Does this complete the refactor step of TDD?**

Yes.
[implement](./implement.md) focuses on red/green, making required behavior pass its tests.
This skill then checks standards and improves the implementation's structure while preserving that behavior.
If the Specifications reviewer finds missing or incorrect behavior, the calling workflow returns to red/green for that requirement.

**Why not let the reviewers refactor while they inspect?**

Both reviewers need the same starting code to make independent assessments.
They propose concrete changes while the code is stable; the coordinator applies them after both reports arrive.
The reviewers then verify the changes in their existing contexts.

**Can I trust every smell finding?**

Treat it as a judgement call supported by a citation and a proposed benefit.
The coordinator validates that evidence before editing.
The final report distinguishes verified refactors, dismissed suggestions, and open findings, so you can inspect what changed and why.

**Will it keep reviewing until there are no suggestions?**

No.
It verifies accepted refactors and fixes concrete regressions introduced by them.
Further subjective suggestions remain in the report instead of starting an endless refactoring loop.

**Does it review my uncommitted work?**

Yes.
It captures the current tracked files against the pinned merge-base and includes new files belonging to the work.
It does not stage those files, and standalone refactors remain uncommitted for you or the calling workflow to commit.

**Do I have to run `/setup-ai-workspace` first?**

No.
When tracker configuration exists, the skill uses it to fetch specifications referenced by commits.
Otherwise it uses supplied specifications or searches local documentation, `specifications/`, `backlog/`, and `.refinement/`.
If no specifications are available, you choose to configure lookup, provide one, or continue with Standards alone.

## It's working if

- Implementation first establishes behavior with passing tests, then the refactor phase changes structure while those tests still pass.
- The report keeps Standards and Specifications separate, with evidence and a disposition for every finding.
- The same reviewers verify the refactors rather than restarting the investigation.
- Missing requirements remain visible as implementation work instead of being hidden by changed tests.
- You can see which refactors were verified, which findings remain open, and which checks passed or failed.
- With no specifications, that axis says "no specifications available".

## Where it fits

This is the refactor step after [implement](./implement.md) or the combined integration build from [implement-all](./implement-all.md).
[test-driven-development](./test-driven-development.md) supplies the red/green discipline that establishes behavior before this phase.
[to-pull-request](./to-pull-request.md) describes the resulting work when it is ready to share.
[improve-agent-environment](../upkeep/improve-agent-environment.md) follows sessions worth learning from and proposes better checks or standards.

[what-is-next](../getting-started/what-is-next.md) routes across the whole set.
