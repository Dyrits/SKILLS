---
name: publish-message
description: "Publish an established conclusion or review summary to a connected service (code host, tracker, chat, documentation, email) in its conventions. Use when the user asks to post, publish, or send findings to one."
argument-hint: "Optional: where to post, and what to say"
---

Publish conclusions already established in this conversation to a destination other people read: a pull or merge request, an issue or ticket, a chat channel or thread, a documentation page, an email. Accept findings from any review source; use the established evidence and dispositions as the input.
Draft the complete publication in the destination's conventions, obtain approval of its exact text and destination, then publish and verify it.

**Calls:** `unslop`.

`.agents/issue-tracker.md`, when present, records the verified posting mechanism for the project's tracker and saves re-deriving it. Resolve the destination and posting mechanism directly (steps 1 and 2) when it is missing or does not cover the resolved destination.

## Process

### 1. Resolve the destination

Use the destination the user named: a pull or merge request number, an issue key, a channel or thread, a page, a recipient. Otherwise infer it only when exactly one candidate fits: a request tracking the current branch, an issue key or thread mentioned earlier in the conversation. Ask when neither resolves; this message becomes visible to other people, so the destination is confirmed, not guessed.

Once resolved, read the surrounding context the message lands in: the request's or ticket's title and description, the thread's recent messages, the page's current content. Step 3 needs it for language, tone, and placement. Note the audience and visibility (a public channel, an external recipient, a private thread), since they shape what the message may contain.

Done when the service, the exact destination, its surrounding context, and its audience are known.

### 2. Resolve how to post

If `.agents/issue-tracker.md` covers the destination, use the mechanism it records. A file that names a different tool than the destination's service (a GitHub tracker file for a Slack channel) does not cover it; resolve this destination as if the file were missing. Otherwise prefer a connected MCP tool or connector for the service (a GitHub, GitLab, Jira, Linear, Slack, Confluence, Notion, or mail server, for example), then the service's CLI (`gh`, `glab`, and similar), then its documented API with credentials already configured.

Ask the user how to post only when nothing resolves unambiguously: several tools could apply and it is unclear which reaches the destination, or none can. When no mechanism can reach it, step 5 hands the approved text to the user instead.

Done when one verified mechanism reaches the destination, or the user knows they will post it themselves.

### 3. Draft the complete publication

State the conclusion, the reason, and enough context for the reader to locate the affected behavior.
When condensing a review, account for every finding and preserve its disposition, verification limits, unresolved requirements, and decisions still needed.
Before describing a verified local change as completed in the destination branch, check that the destination contains it.
Otherwise describe it as a local change awaiting publication, or state that its destination status is unverified.

When the publication includes inline suggestions on a GitHub or GitLab request, read [inline-suggestions.md](inline-suggestions.md) for finding placement, diff validation, and submission handling.
Otherwise draft a single message.

Fit the message to the medium:

- **Format**: use the markup the destination renders (GitHub or GitLab Markdown, Jira or Confluence markup, Slack `mrkdwn`, plain text or HTML for email), and a structure its readers expect: a review summary on a request, a status update on a ticket, a short lead-with-the-conclusion message in chat with detail in a thread reply, a subject line for email.
- **Length**: match the medium. Chat and email lead with the conclusion and stay short; a review summary carries every finding.
- **Placement**: reply in the existing thread or conversation when one exists; start a new one only when the user asks or none exists.
- **Mentions and recipients**: include only the people the user names; a mention notifies them.
- **Audience**: leave out internal details (file paths, local branch names, private links) that an external or broader audience cannot use or should not see.

Write in the language already used at the destination, not necessarily the language of this conversation. When the destination carries no language signal, use this conversation's language, or ask when that is unclear.

- Write plain sentences in the user's voice, with one paragraph per point.
- Use commas, periods, or conjunctions to connect thoughts.
- Full words over contracted ones ("repository" not "repo", "configuration" not "config", "documentation" not "docs"), and the plain term over an acronym on first mention ("the null check" not "NPE", "the identifier" not "UUID") unless it is what the codebase itself calls it. The reader may not share the writer's technical background, and a shortened form is one more thing they might not parse.
- Keep only the context and reasoning the reader needs to understand or act on each point.

Call the Skill tool with "unslop" to remove AI language patterns from the message and any inline comments without changing their meaning or tone.
Done when every item is an exact, destination-specific draft in the destination's format and every included finding has a clear disposition.

### 4. Approve the complete publication

Show the service, the destination, any recipients or mentions, and the exact final text of every item, including each inline comment's file, diff side, line range, reason, and replacement.
Ask the user to confirm publication of the complete set under their responsibility, and wait for explicit approval before posting anything.
If the user already approved this exact final set and destination, use that approval.
After any revision, show the changed set and obtain approval again.
Done when the exact set and destination are approved.

### 5. Publish and verify

For a single message, publish the approved text through the mechanism from step 2, then read it back from the destination and check its text and placement. When the service cannot be read back, report that verification limit.
For a publication with inline suggestions, follow the submission handling in [inline-suggestions.md](inline-suggestions.md).
When no mechanism reaches the destination, give the user the approved text in its final format, ready to paste.
Report the published URLs or references, including any partial result.
Done when every approved item is live at its approved destination with text matching the approved draft (or is in the user's hands with that limit stated), and any stated suggestion count matches the items actually posted.
