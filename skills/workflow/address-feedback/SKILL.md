---
name: address-feedback
description: "Assess review feedback from any source (pull or merge request, issue, ticket, document comments, pasted notes), propose dispositions, then implement and reply. Use when the user shares feedback to address or asks to handle review comments."
argument-hint: "Feedback source: PR, MR, issue, or ticket reference, a file path, or pasted text"
---

# Address Feedback

Turn a set of review feedback into an accounted-for set of decisions, approved changes, and replies grounded in the validated result.

Feedback arrives in one of two kinds of **source**:

- A **tracked source** has addressable comments and a reply destination: a pull or merge request, an issue, a ticket, comments on a shared document.
- An **untracked source** is plain text with no reply channel the agent can write to: notes pasted into the conversation, a file, an email or chat message, a meeting transcript, a reviewer's verbal summary.

The **subject** is whatever the feedback concerns: code, a document, a design, a specification, a configuration. Steps 2 to 4 are the same for both kinds of source; steps 1, 5, and 6 branch on it.

`documentation/agents/issue-tracker.md`, when present, records how to read and update the configured tracker. Resolve the source and access method directly when the file is missing or silent.

## Process

### 1. Resolve the source, the subject, and working context

Use the source named or supplied by the user. Otherwise infer one only when the current branch or conversation identifies exactly one; ask when it remains ambiguous.

For a tracked source, read its title and description and every comment and review thread, including resolved and outdated threads when they still explain intent or constrain the change. Record each comment's identifier for replies.

For an untracked source, read the whole text and split it into individual points. Give each point a stable reference (`F1`, `F2`, ...) with the minimum quoted text needed to recognize it, and note who gave the feedback when known.

Then locate the subject and read its current state: the relevant code and diff, the document, or the artifact the feedback refers to. Read the repository instructions when the subject lives in a repository, and confirm the checked-out branch is the one that should receive changes. When the subject cannot be located, ask instead of guessing which version was reviewed.

Done when the source kind, the complete set of comments or points, the subject's current state, and (for repository work) the receiving branch are known.

### 2. Account for the feedback

Treat each substantive comment or point as one unit of feedback. Group repeated ones only when they ask for the same outcome, keeping every reference in the group so each can be answered. Record automated status messages, approvals without requests, and social acknowledgements as non-substantive.

Assign one disposition to every substantive unit:

- **Accept**: the request is correct as written.
- **Adjust**: the concern is valid, but a different change better satisfies it.
- **Already addressed**: the current subject already satisfies it; cite the evidence.
- **Decline**: the request conflicts with the specification, project constraints, or a better-supported design; explain the tradeoff.
- **Blocked**: a missing decision or fact prevents a responsible disposition.

Check units against each other, the source's stated intent, project conventions, tests, and current behavior. Surface contradictions and scope expansion for the user to decide. Investigate factual questions with read-only work before calling them blocked.

Present one compact table with the reference, request, assessment, disposition, and proposed change or reply. Follow it with the implementation and validation plan, including which files are likely to change. Give a clear recommendation when judgment is involved.

Done when every substantive unit appears exactly once, every non-substantive one is accounted for separately, and the user can review the complete consequences of accepting the plan.

### 3. Get approval for the change plan

Ask the user to approve or revise the dispositions and plan. This gate authorizes local changes only. Present the plan again when revisions materially alter the work.

Edit the subject only after the user approves the plan. Once approved, continue through implementation and validation without asking about routine choices the plan already covers.

Done when the user has approved a concrete disposition and action for every substantive unit.

### 4. Implement and validate

Implement only the approved changes, preserving unrelated work. Follow the project's development workflow and validate in proportion to the change. If implementation shows an approved disposition is wrong or needs materially broader work, stop that item, explain the evidence, and return it to the plan gate.

Review the result against every approved disposition. A passing test suite does not account for a unit by itself; connect each one to the changed subject, existing evidence, or a stated decision.

Done when the approved changes are implemented, relevant validation passes, and every substantive unit has a verified outcome.

### 5. Draft the replies

Lead each reply with the decision and its reason. For implemented changes, name the observable result and the validation that supports it. For adjusted or declined requests, state the tradeoff directly. Claim a change is complete only when step 4 verified it. Keep replies short and specific, in the language of the feedback. Use the `[AI] ` prefix only when the user requests it or the project convention requires it.

- **Tracked source**: draft one reply per substantive comment, including declined, blocked, duplicate, and already-addressed ones, placed in its original thread where the tracker supports threading. For an unthreaded issue or ticket, quote only enough text to make the reply unambiguous. List proposed thread resolutions or status changes separately: posting a reply does not authorize resolving a thread, approving a review, closing a ticket, or changing status.
- **Untracked source**: draft one consolidated response addressed to the reviewer, answering every substantive point by its reference or a short quote, in the medium the feedback came through. Skip the response when the user says the changes are the only answer wanted.

Done when every substantive unit has an exact draft answer (or the user waived replies for an untracked source) and any tracker mutations are listed separately.

### 6. Confirm and deliver

Ask the user to approve the replies and any separately listed tracker mutations, and revise on request. Skip this confirmation only when the user already supplied exact reply text to post verbatim after seeing the implementation outcome.

- **Tracked source**: publish the approved replies through the access method resolved in step 1, preferring a batched review submission when it keeps thread placement. Apply only the separately approved resolutions or status changes. Report the posted comment URLs or references.
- **Untracked source**: hand the approved response to the user, ready to send; the agent has no channel to deliver it.

Report any units intentionally left without a reply and the final validation result.

Done when every approved reply is live at its destination or in the user's hands, every substantive unit is accounted for, and no unapproved tracker mutation occurred.
