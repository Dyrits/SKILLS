---
name: publish-review
description: Publish a finished code review report to the tracker, with cross-cutting findings as a summary and fixable findings as inline suggestions.
disable-model-invocation: true
argument-hint: "Optional: where to post"
---

Publish a `/code-review` report that already ran in this conversation. The finished two-axis report is the input. Assign each finding to an inline suggestion or the summary, approve the complete publication, then post it.

Use the target resolution and drafting rules in [publish-message](../publish-message/SKILL.md) when it is installed. This skill handles publication itself so that the summary and inline suggestions receive one approval before either becomes visible.

## Process

### 1. Split the findings

For every finding across both axes:

- **Inline suggestion**, GitHub/GitLab only: the fix *is* the finding, small, unambiguous, and scoped to one hunk (a rename, a dropped null check, a swapped condition). Something a reviewer would one-click-accept.
- **Summary**: everything else: judgement calls (the Fowler smells, "possible X"), anything spanning more than one hunk or file, anything on Jira (no diff to suggest against), and any GitHub/GitLab finding you aren't confident enough in to propose as a literal replacement.

When in doubt, summary. A wrong suggested change is worse than a described one: the reader can act on a wrong description by disagreeing with it, but a wrong suggestion invites a wrong one-click accept. Done when every finding from the report sits in exactly one of the two buckets.

### 2. Draft the complete publication

Resolve the target and posting mechanism, preferring an available tracker MCP tool over a CLI. Read the target's title and description to match its language. Draft an `[AI]`-prefixed summary with one short paragraph per summary finding, each leading with the reason rather than restating the finding. When there are inline suggestions, end with `+ N inline suggestions on the diff`, where N is the number drafted and ready to post.

For each inline finding, draft one comment at its file and line: `[AI] ` plus one sentence of why, then a fenced `suggestion` block holding the corrected line(s) on GitHub or the platform's suggestion syntax on GitLab. Check that each replacement applies to the current diff. Jira and reviews with no inline findings need only the summary.

Done when the summary and every inline suggestion are exact, destination-specific drafts and their count agrees.

### 3. Approve the complete publication

Show the exact summary and every inline suggestion with its file, line, reason, and replacement. Ask for one go-ahead covering the complete set before posting anything. Revise the drafts and show the changed set again when requested.

Done when the user has approved the exact summary and every suggestion to publish.

### 4. Publish and verify

Where the tracker supports a review body and inline suggestions in one submission, publish the approved summary as the review body and the suggestions as its inline comments. Prefer an available MCP tool's pending-review workflow; otherwise use a verified CLI or platform UI. Submit only after the full review matches the approved drafts.

Where one submission cannot hold both, post the approved inline suggestions first, batching them when the tracker allows it. Verify their destinations and count before posting the summary as a separate comment. If any suggestion fails, report the partial result and stop. Revise the summary and seek approval again if its promised count or wording must change. On Jira or when there are no inline suggestions, post only the approved summary.

Report the published comment and review URLs or references. Done when every approved item is live at the intended destination and any count in the published summary matches the inline suggestions actually posted.
