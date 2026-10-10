# Inline suggestions

Read this reference when the requested publication includes inline suggestions.
The main process in [SKILL.md](../SKILL.md) owns destination resolution, prose, and approval of the complete publication.

## Place the findings

Account for every finding in exactly one place:

- **Inline suggestion:** an open finding on GitHub or GitLab whose fix is small, unambiguous, and confined to one hunk in the current destination diff.
- **Summary:** completed work, unresolved requirements, decisions, uncertain changes, changes spanning hunks or files, and every finding when the destination is not a GitHub or GitLab request.

Use a suggestion only when a literal replacement fully addresses the finding and the proposed change is still absent from the destination diff.
Keep judgement calls in the summary with their evidence and disposition.
An executable suggestion invites immediate acceptance, so its replacement needs stronger evidence than a description of a possible change.
Done when every finding has one placement and every inline candidate meets these conditions.

## Validate and draft

Read the current destination diff and record its head revision before drafting suggestions.
For each inline finding, identify its file, diff side, and line range, write one sentence explaining the reason, and add the replacement using the platform's supported suggestion syntax.
Check that the addressed lines exist in the current diff, the replacement applies to that range, and it resolves the established finding.
Keep a finding in the summary if its replacement or valid diff location cannot be established.

Draft the summary from the remaining findings, preserving their dispositions and distinguishing local work from changes present in the destination.
When a summary accompanies suggestions, include their drafted count only if it helps the reader locate them.
An explicitly requested set of inline comments can stand alone when there are no summary findings.
Other destinations and publications with no eligible suggestions use a single summary message and return to the main process.
Done when every suggestion is a validated, destination-specific draft and any summary count agrees with the drafted set.

## Submit the approved set

Before posting, check that the destination head still matches the revision used to validate the suggestions.
If it changed, revalidate the locations and replacements against the new diff, then return to approval if any approved text or location changes.

Where the tracker supports one review submission, publish the approved summary as the review body and the suggestions as inline comments in that review.
Use a neutral comment review event; approval here authorizes publication of text, not an Approve or Request changes verdict.
Prefer an available MCP tool's pending-review workflow; otherwise use a verified CLI or platform UI.
Verify the pending body's text, every inline comment, and their locations before submission.

Where one submission cannot hold the complete set, post the approved inline suggestions first, batching them when supported.
Verify their destinations and count before posting the approved summary as a separate comment, if there is one.
If any item fails or its outcome is uncertain, report the confirmed posted items and the remaining items, then stop.
Check the destination before retrying so confirmed items are posted only once.
If a partial result requires changing the summary or its promised count, return to approval with the revised draft.

Verify the published text, inline locations, and count against the approved set, then return the resulting URLs or references to the main process.
