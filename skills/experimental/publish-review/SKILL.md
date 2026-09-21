---
name: publish-review
description: Publish a finished code review report to the tracker, with cross-cutting findings as a summary and fixable findings as inline suggestions.
disable-model-invocation: true
argument-hint: "Optional: where to post"
---

Publish a `/code-review` report that already ran in this conversation. It never re-reviews the diff: the finished two-axis report is the input, and the whole job is deciding, per finding, whether it becomes an inline suggested change or a line in the summary, then posting both.

It needs [publish-message](../publish-message/SKILL.md) installed alongside it: this skill calls it for the summary comment and depends on it for tracker resolution and its drafting rules (step 3 of that skill). Installing `publish-review` alone gets you a skill that cannot post its summary. Those same drafting rules, including the target's language, apply here too, to the one-sentence why on every inline suggestion.

## Process

### 1. Split the findings

For every finding across both axes:

- **Inline suggestion**, GitHub/GitLab only: the fix *is* the finding, small, unambiguous, and scoped to one hunk (a rename, a dropped null check, a swapped condition). Something a reviewer would one-click-accept.
- **Summary**: everything else: judgement calls (the Fowler smells, "possible X"), anything spanning more than one hunk or file, anything on Jira (no diff to suggest against), and any GitHub/GitLab finding you aren't confident enough in to propose as a literal replacement.

When in doubt, summary. A wrong suggested change is worse than a described one: the reader can act on a wrong description by disagreeing with it, but a wrong suggestion invites a wrong one-click accept. Done when every finding from the report sits in exactly one of the two buckets.

### 2. Post the summary

Call the Skill tool with `publish-message`, handing it the target, everything sorted into "Summary" in step 1, and an explicit instruction to post with the `[AI]` prefix: one short paragraph per finding leading with the why, not a restatement of the finding text, plus a closing line naming how many inline suggestions ride alongside it (`+ N inline suggestions on the diff`), so the two land reading as one review. A review's provenance is never optional, so this skips `publish-message`'s own prefix question; its confirmation before posting still applies. Let `publish-message` own drafting, confirmation, and posting for this part entirely; don't re-implement any of it here.

### 3. Draft the inline suggestions

Skip this step and step 4 entirely on Jira, or when nothing sorted into "Inline suggestion".

For each inline finding, one comment at its file and line: `[AI] ` plus one sentence of why, then a fenced ` ```suggestion ` block holding the corrected line(s) (GitHub's syntax) or the platform's suggestion syntax (GitLab). Post through the tracker's pull/merge request **review** flow, not a plain issue comment: an available MCP tool's pending-review workflow (create the review, add each line comment, submit) is preferred; fall back to the CLI (`gh pr review`, `glab mr` note-with-position) or the platform UI where no MCP tool covers it. Done when every inline finding has a drafted comment carrying the `[AI] ` prefix, a one-sentence why, and a correct fenced suggestion block.

### 4. Confirm, then publish the suggestions

Show every drafted inline suggestion (file, line, the one-sentence why, the replacement) before posting any of them. This is a second, separate confirmation from `publish-message`'s own in step 2: a suggestion proposes a code change, which needs its own look even after the summary is already approved. Publish everything confirmed as one review submission where the tracker supports batching, rather than one notification per comment. Done when every confirmed suggestion is live and nothing posted before the user saw it.
