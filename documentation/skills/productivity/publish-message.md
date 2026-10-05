Fork-created skill with no upstream equivalent, added in commit `363809a` as `publish-message`, with a sibling `publish-review` consolidated into it in `c9ed16e` (see the [provenance audit](../../research/2026-10-03-retained-skill-provenance.md)). It began as a pull request and merge request skill under version control and now publishes to any connected service, which is why it lives in the productivity bucket.

## What it does

`publish-message` publishes a conclusion already established in the conversation to a place other people read: a pull or merge request, an issue or ticket, a chat channel or thread, a documentation page, or an email. It drafts the full message in the destination's conventions, shows you the exact text and destination, waits for explicit approval, then posts and reads it back.

Nothing is posted without that approval, and any revision brings the changed set back for approval again.

## When to reach for it

Type `/publish-message`, optionally with where to post and what to say; an agent or another skill can also reach for it, but it always waits for approval of the exact text and destination. Use it after you have reached findings or a decision and want them shared. To answer someone else's feedback point by point, use [address-feedback](../workflow/address-feedback.md). To write a pull request description, use [draft-merge-request](../version-control/draft-merge-request.md).

## Prerequisites

A way to reach the destination: a connected tool for the service, its command line, or its configured API. If none resolves, you receive the approved text ready to paste. `.agents/issue-tracker.md` records the posting mechanism for a configured tracker and saves re-deriving it.

## Fitting the medium

The agent adapts each of these to the destination.

| Aspect | Behavior |
| --- | --- |
| Format | The markup it renders: Markdown, Jira or Confluence markup, Slack formatting, email text |
| Length | Short and conclusion-first in chat and email; every finding in a review summary |
| Placement | Replies in the existing thread; a new one only when asked or none exists |
| Mentions | Only the people you name, since a mention notifies them |
| Audience | Internal paths, local branch names, and private links stay out of external or broad messages |
| Language | The language already used at the destination |

## Inline suggestions

On a GitHub or GitLab request, a small unambiguous fix confined to one hunk can be posted as an executable inline suggestion. Everything else, including judgment calls and changes spanning hunks, stays in the summary. The agent validates each suggestion against the current diff, rechecks that the head revision has not moved before posting, and submits a neutral comment review, never an Approve or Request changes verdict. The rules are in [inline-suggestions.md](../../../skills/productivity/publish-message/inline-suggestions.md).

## Common questions

**Does approving the text also approve the review?**

No. Approval authorizes publication of text. The review event is neutral comment only.

**What if the posting fails partway?**

It reports what is confirmed posted and what remains, then stops. It checks the destination before any retry so nothing is posted twice.

**Can it say a fix is done?**

Only when the destination contains it. Otherwise the message describes a local change awaiting publication, or states that the destination status is unverified.

**What if a skill it calls is not installed?**
It names the missing skill with its install command, carries out that step from its stated intent, and tells you the step ran without it. The skills involved are listed at the top of its [`SKILL.md`](../../../skills/productivity/publish-message/SKILL.md).

## It's working if

- The message arrives in the right place, in the destination's format and language.
- Its text matches what you approved, and the read-back confirms placement.
- Every finding in a review summary has a clear disposition.
- A stated suggestion count matches the comments actually posted.

## Where it fits

This is a standalone publication step after [review-and-refactor](../workflow/review-and-refactor.md) or any other work that produced a conclusion. [address-feedback](../workflow/address-feedback.md) covers replies to feedback you received, and [draft-merge-request](../version-control/draft-merge-request.md) covers request descriptions. [guide](./guide.md) maps the whole system.
