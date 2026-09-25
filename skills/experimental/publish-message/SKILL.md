---
name: publish-message
description: Post a short comment to a GitHub or GitLab pull/merge request, or a Jira issue.
disable-model-invocation: true
argument-hint: "Optional: where to post, and what to say"
---

Publish something already decided in this conversation (a review finding, a decision, an answer) as a comment on a GitHub/GitLab pull or merge request, or a Jira issue. Posting is the whole job: it never re-runs the review or re-derives the point, it only externalises what's already been concluded. For a full `/code-review` report specifically, prefer [publish-review](../publish-review/SKILL.md), which approves and publishes the summary and inline suggestions together.

`documentation/agents/issue-tracker.md`, when present, records the verified posting mechanism per tracker and saves re-deriving it. It is not required: resolve the target and posting mechanism directly (steps 1-2) when it's missing or silent on the resolved target.

## Process

### 1. Resolve the target

If the user named a PR/MR number or Jira key, use it. Otherwise infer it: a PR/MR tracking the current branch, or an issue key mentioned earlier in the conversation. Ask if neither resolves; never guess at a destination for something you're about to make visible to other people. Once resolved, read its title and description (or the ticket's): step 3 needs them to match the message's language.

### 2. Resolve how to post

If `documentation/agents/issue-tracker.md` exists and covers the resolved target, use the mechanism it records: CLI (`gh pr comment` / `gh issue comment`, `glab mr note` / `glab issue note`), an available MCP tool (a GitHub or GitLab MCP server's comment/note tool, an Atlassian Jira MCP's `addCommentToJiraIssue`), or another verified method.

Otherwise resolve it directly instead of stopping: prefer an available MCP tool for the resolved tracker over a CLI, and fall back to the CLI (`gh`, `glab`) when no MCP tool covers it. Ask the user how to post only when nothing resolves unambiguously, for instance several CLIs or MCP tools could apply and it's unclear which reaches the resolved target.

### 3. Draft the message

**Lead with the why.** The reader already has the diff and the ticket in front of them; what they don't have is your reasoning. State the conclusion and the reason it holds, not a walkthrough of what changed or what the finding says, that's visible one scroll away.

- Write it in the language already used in the target: the pull/merge request's title and description, or the ticket, not necessarily the language of this conversation. If the target carries no language signal (an empty description, no prior comments), default to the language this conversation has been in, or ask if that is unclear.
- Write it like a person leaving the comment, not a report: plain sentences, no "Upon review," no "I have identified," no bullet-per-clause.
- Never an em dash. Where one tempts, use a comma, a period, or "and"/"but" instead, whichever the sentence actually wants.
- Full words over contracted ones ("repository" not "repo", "configuration" not "config", "documentation" not "docs"), and the plain term over an acronym on first mention ("the null check" not "NPE", "the identifier" not "UUID") unless it is what the codebase itself calls it. The reader may not share the writer's technical background, and a shortened form is one more thing they might not parse.
- As short as the why allows. No greeting, no restating the finding, no closing filler.
- One paragraph for one point. If there are genuinely separate points, one short paragraph per point, not a bulleted restatement of the diff.

Write the comment in the user's voice.
Call the Skill tool with `unslop` to clean the complete draft when that skill is available; otherwise remove AI language patterns without changing its meaning or tone.

### 4. Confirm, then publish

Show the exact final message and its destination, and ask the user to confirm publication under their responsibility.
Wait for explicit approval of that text and destination before posting, including when the user supplied the text verbatim.
If the user already approved this exact final text and destination, use that approval.
After any revision, show the updated message and obtain approval again.
Publish the approved text through the mechanism from step 2 and report the comment's URL or reference.
Done when the approved comment is live at the approved destination.
