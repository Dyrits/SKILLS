Fork-created skill with no upstream equivalent, added in commit `35b08c5` (see the [provenance audit](../../research/2026-10-03-retained-skill-provenance.md)). It began as a pull request and merge request skill under version control and now accepts feedback from any source, which is why it lives in the workflow bucket.

## What it does

`address-feedback` turns a set of review comments into accounted-for decisions, approved changes, and replies grounded in the validated result. You approve the plan before anything is edited, and you approve the replies before anything is posted.

It accepts two kinds of source:

| Kind | Examples | Reply |
| --- | --- | --- |
| Tracked | Pull or merge request, issue, ticket, comments on a shared document | One draft per comment, placed in its thread |
| Untracked | Pasted notes, a file, an email or chat message, a meeting transcript | One consolidated response, handed to you to send |

The subject can be code, a document, a design, a specification, or a configuration.

## When to reach for it

Type `/address-feedback`, with a reference, a file path, or pasted text; an agent or another skill can also reach for it. Use it when someone has reviewed your work and you need to respond to every point. To publish a conclusion you already reached, use [publish-message](../productivity/publish-message.md). To review code yourself, use [review-and-refactor](./review-and-refactor.md).

## Dispositions

Every substantive comment gets exactly one disposition, shown in a single table with the proposed change or reply.

| Disposition | Meaning |
| --- | --- |
| Accept | Correct as written |
| Adjust | Valid concern, better change |
| Already addressed | Current state satisfies it, with evidence |
| Decline | Conflicts with the specification, constraints, or a better design, with the tradeoff |
| Blocked | A missing decision or fact prevents a responsible answer |

Automated messages and plain approvals are recorded separately as non-substantive.

## Common questions

**Does approving the plan let it post replies or resolve threads?**

No. The plan approval authorizes local changes only. Replies need their own approval, and resolving a thread, approving a review, closing a ticket, or changing status is listed and approved separately.

**What if the feedback came from an email or a meeting?**

Paste it or point to the file. Each point gets a stable reference (`F1`, `F2`), and you receive one drafted response to send yourself, since the agent has no channel to the reviewer.

**What if implementation shows an approved disposition was wrong?**

That item stops and returns to the plan gate with the evidence. The rest continues.

**Is a green test suite enough to say a comment is handled?**

No. Each unit is connected to the changed subject, existing evidence, or a stated decision.

## It's working if

- Every substantive comment appears exactly once in the table with a disposition.
- Nothing was edited before you approved the plan.
- Each reply leads with the decision and names the verified result.
- No thread was resolved and no status changed without your separate approval.

## Where it fits

This is a workflow step that follows a review of your work and loops back through implementation: [implement](./implement.md) and [test-first](./test-first.md) style validation apply to the changes. Replies are drafted in the spirit of [publish-message](../productivity/publish-message.md), which handles posting conclusions to any service. [guide](../productivity/guide.md) maps the whole system.
