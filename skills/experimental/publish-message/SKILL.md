---
name: publish-message
description: Publish a conclusion or review summary to GitHub, GitLab, or Jira, with optional inline suggestions on a pull or merge request.
disable-model-invocation: true
argument-hint: "Optional: where to post, and what to say"
---

Publish conclusions already established in this conversation as a comment, a review summary, or a requested set of inline comments on a GitHub/GitLab pull or merge request, or a Jira issue.
Accept findings from any review source; use the established evidence and dispositions as the input.
Draft the complete publication, obtain approval of its exact text and destination, then publish and verify it.

`documentation/agents/issue-tracker.md`, when present, records the verified posting mechanism per tracker and saves re-deriving it. It is not required: resolve the target and posting mechanism directly (steps 1-2) when it's missing or silent on the resolved target.

## Process

### 1. Resolve the target

If the user named a PR/MR number or Jira key, use it. Otherwise infer it: a PR/MR tracking the current branch, or an issue key mentioned earlier in the conversation. Ask if neither resolves; never guess at a destination for something you're about to make visible to other people. Once resolved, read its title and description (or the ticket's): step 3 needs them to match the message's language.

### 2. Resolve how to post

If `documentation/agents/issue-tracker.md` exists and covers the resolved target, use the mechanism it records: CLI (`gh pr comment` / `gh issue comment`, `glab mr note` / `glab issue note`), an available MCP tool (a GitHub or GitLab MCP server's comment/note tool, an Atlassian Jira MCP's `addCommentToJiraIssue`), or another verified method.

Otherwise resolve it directly instead of stopping: prefer an available MCP tool for the resolved tracker over a CLI, and fall back to the CLI (`gh`, `glab`) when no MCP tool covers it. Ask the user how to post only when nothing resolves unambiguously, for instance several CLIs or MCP tools could apply and it's unclear which reaches the resolved target.

### 3. Draft the complete publication

State the conclusion, the reason, and enough context for the reader to locate the affected behavior.
When condensing a review, account for every finding and preserve its disposition, verification limits, unresolved requirements, and decisions still needed.
Before describing a verified local change as completed in the destination branch, check that the destination contains it.
Otherwise describe it as a local change awaiting publication, or state that its destination status is unverified.

When the requested publication includes inline suggestions, read [inline-suggestions.md](inline-suggestions.md) for finding placement, diff validation, and submission handling.
Otherwise draft a single comment or summary.

- Write it in the language already used in the target: the pull/merge request's title and description, or the ticket, not necessarily the language of this conversation. If the target carries no language signal (an empty description, no prior comments), default to the language this conversation has been in, or ask if that is unclear.
- Write plain sentences in the user's voice, with one paragraph per point.
- Use commas, periods, or conjunctions to connect thoughts.
- Full words over contracted ones ("repository" not "repo", "configuration" not "config", "documentation" not "docs"), and the plain term over an acronym on first mention ("the null check" not "NPE", "the identifier" not "UUID") unless it is what the codebase itself calls it. The reader may not share the writer's technical background, and a shortened form is one more thing they might not parse.
- Keep only the context and reasoning the reader needs to understand or act on each point.

Call the Skill tool with `unslop` to clean the summary and any inline comments when that skill is available; otherwise remove AI language patterns without changing their meaning or tone.
Done when every item is an exact, destination-specific draft and every included finding has a clear disposition.

### 4. Approve the complete publication

Show the destination and exact final text of every item, including each inline comment's file, diff side, line range, reason, and replacement.
Ask the user to confirm publication of the complete set under their responsibility, and wait for explicit approval before posting anything.
If the user already approved this exact final set and destination, use that approval.
After any revision, show the changed set and obtain approval again.
Done when the exact set and destination are approved.

### 5. Publish and verify

For a single comment or summary, publish the approved text through the mechanism from step 2, then verify its text and destination.
For a publication with inline suggestions, follow the submission handling in [inline-suggestions.md](inline-suggestions.md).
Report the published comment or review URLs or references, including any partial result.
Done when every approved item is live at its approved destination, its text matches the approved draft, and any stated suggestion count matches the items actually posted.
