---
name: address-feedback
description: Assess comments on a pull request, merge request, issue, or ticket; propose a disposition and change plan; implement the approved changes; then draft and post a reply to every substantive comment.
disable-model-invocation: true
argument-hint: "PR, MR, issue, or ticket reference"
---

# Address Feedback

Turn a review or ticket thread into an accounted-for set of decisions, approved code changes, and replies grounded in the validated result.

`documentation/agents/issue-tracker.md`, when present, records how to read and update the configured tracker. It is not required: resolve the target and access method directly when the file is missing or silent.

## Process

### 1. Resolve the target and working context

Use the target named by the user. Otherwise infer one only when the current branch or conversation identifies exactly one pull request, merge request, issue, or ticket. Ask when the destination remains ambiguous.

Read the repository instructions, the target's title and description, every comment and review thread, and the current code and diff relevant to them. Include resolved and outdated threads when they still explain intent or constrain the current change. Identify whether the checked-out branch is the branch that should receive the changes before proposing an implementation.

Done when the target, repository, branch, complete comment set, and relevant code context are known.

### 2. Account for the feedback

Treat each substantive comment as one unit of feedback. Group repeated comments only when they ask for the same outcome, and retain every comment identifier in the group so each one can receive a reply later. Record automated status messages, approvals without requests, and social acknowledgements as non-substantive instead of turning them into invented work.

Assign one disposition to every substantive comment:

- **Accept**: the request is correct as written.
- **Adjust**: the concern is valid, but a different change better satisfies it.
- **Already addressed**: the current code already satisfies it; cite the evidence.
- **Decline**: the request conflicts with the specification, repository constraints, or a better-supported design; explain the tradeoff.
- **Blocked**: a missing decision or fact prevents a responsible disposition.

Check comments against each other, the target description, repository conventions, tests, and current behavior. Surface contradictions and scope expansion instead of silently choosing a side. Investigate factual questions with read-only work before calling them blocked.

Present one compact table with the comment reference, request, assessment, disposition, and proposed change or reply. Follow it with the implementation and validation plan, including which files are likely to change. Give a clear recommendation when judgment is involved.

Done when every substantive comment appears exactly once, every non-substantive comment is accounted for separately, and the user can review the complete consequences of accepting the plan.

### 3. Get approval for the change plan

Ask the user to approve or revise the dispositions and implementation plan. This gate authorizes local implementation only. Apply requested revisions and present the changed plan again when they materially alter the work.

Make no code edits until the user approves the plan. Once approved, continue through implementation and validation without asking for routine implementation choices already covered by it.

Done when the user has approved a concrete disposition and action for every substantive comment.

### 4. Implement and validate

Implement only the approved changes, preserving unrelated work in the working tree. Follow the repository's development workflow and run validation proportional to the change. If implementation reveals that an approved disposition is wrong or requires materially broader work, stop that item, explain the evidence, and return it to the plan gate.

Review the resulting diff against every approved disposition. A passing test suite does not account for a comment by itself; connect each comment to the changed code, existing evidence, or stated decision.

Done when the approved changes are implemented, relevant validation passes, and every substantive comment has a verified outcome.

### 5. Draft every reply

Draft one reply for every substantive comment, including declined, blocked, duplicate, and already-addressed comments. Reply in the target's language and in the original thread where the tracker supports it. For an unthreaded issue or ticket, identify the comment or quote only the minimum text needed to make the reply unambiguous.

Lead with the decision and its reason. For implemented changes, name the observable result and the validation that supports it. For adjusted or declined requests, explain the tradeoff directly. Do not claim a change is complete unless step 4 verified it.

Keep replies short and specific. Avoid greetings, report language, and walkthroughs of the whole diff. Use the `[AI] ` prefix only when the user requests it or the repository convention requires it.

Present the exact replies beside their destination comments, plus any proposed thread resolutions or status changes. Do not treat posting a reply as permission to resolve a thread, approve a review, close a ticket, or change tracker status.

Done when every substantive comment has an exact, destination-specific draft and any additional tracker mutations are listed separately.

### 6. Confirm and publish

Ask the user to approve the complete reply set and any separately listed tracker mutations. Revise drafts when requested. Skip this confirmation only when the user already supplied the exact reply text to post verbatim after seeing the implementation outcome.

Publish the approved replies through the access method resolved in step 1. Apply only the separately approved thread resolutions or status changes. Prefer a batched review submission when the tracker supports it without losing thread placement.

Report the posted comment URLs or references, any comments intentionally left without a reply, and the final validation result.

Done when every approved reply is live at the intended destination, every substantive source comment is accounted for, and no unapproved tracker mutation occurred.
