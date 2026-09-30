## What it does

`to-pull-request` writes the body of a pull request, or a merge request on GitLab, in a fixed three-part shape: a **summary** visual, **evidence** as a before/after pair, and the **merge danger**. It is a format reference, not a workflow: it does not open the request, push the branch, or review anything.

What it writes is aimed at the reviewer's missing information, never at restating what changed. The reviewer already has the diff open, so a body that narrates the diff back tells them nothing they cannot scroll to. Why the change exists comes from its **primary source**, the ticket or specification that asked for it, and the diff only decides which shape shows it.

## When to reach for it

Type `/to-pull-request`, or the agent reaches for it automatically when a task fits: writing a request description, rewriting one that reviewers bounced, or closing out a branch that is about to go up for review.

| Where you are | What to run |
| --- | --- |
| A branch is finished and needs a description a human can read fast | `/to-pull-request` |
| The change is not reviewed yet | [code-review](./code-review.md) first, then this |
| The ticket is not built yet | [implement](./implement.md), which closes out with the review |
| The request is already open and reviewers have commented | [address-feedback](../../../skills/experimental/address-feedback/SKILL.md), which is experimental |
| The conclusion is already written and just needs posting | [publish-message](../../../skills/experimental/publish-message/SKILL.md), which is experimental |

## The summary is a shape, not a paragraph

The summary's job is one visual sized to the single point the change makes, and the skill carries the menu of shapes to pick from: pseudocode for logic, a call tree for runtime control flow, a component tree for user interface structure, a shallow file tree for responsibility or a broad refactor, a Mermaid diagram for interaction, a sketched `diff` where the surrounding shape already exists, and the whole block where most of it is new.

The instruction that does the work is **pick the smallest view that makes the key point clear**. A component tree pruned to the two components that moved beats the same tree drawn in full, because everything else on it is a line the reviewer has to rule out. Using one shape is usual, several happens, and all of them never does.

## Merge danger, in two words

The last section asks two questions and wants short answers.

| Term | The question | Why it is on the body |
| --- | --- | --- |
| **Door** | One-way or two-way? | You walk back through a two-way door. A change carrying a destructive action or a hard-to-reverse decision is one-way, and a reviewer reads a one-way door differently. |
| **Blast radius** | How far does a bad merge reach? | One word, then a line only where the word hides something: layout shift, breakage for consumers, mobile responsiveness, a migration that runs on deploy. |

Both are the author's call, stated up front, rather than something the reviewer has to infer from the file list.

## Common questions

**Does it open the pull request?**
No. It writes the body and stops. Pushing the branch, opening the request, and setting its reviewers stay yours, or stay with [implement-all](./implement-all.md), which opens a request for a whole specification when the tracker workflow or user calls for one.

**Why is it model-invoked when the rest of the `to-*` family is user-invoked?**
Because other skills need to reach it. [implement-all](./implement-all.md) can open a request as part of its run, and a body format that only a human can trigger would be unreachable at exactly the moment it is needed. Typing `/to-pull-request` still works: model-invocation adds the agent's reach, it never removes yours.

**It described the diff instead of explaining the change.**
That is the failure the skill is written against, and it usually means the primary source was not in the window. Give it the ticket or the specification, not just the branch, and the summary has something to be about.

**Where did `pr` go?**
It was named `pr` in the repository this fork started from, where it sat in an `in-progress` bucket. Porting it here renamed it to full words and to this repository's `to-<artifact>` convention, alongside [to-specifications](./to-specifications.md) and [to-tickets](./to-tickets.md).

**Is there a matching skill for commit messages?**
No. The original proposal upstream paired a `/to-commit` with this one, so the commit template would feed the request body. Only the request half exists, and [implement](./implement.md) still commits with a single line of its own guidance.

**Can I trust the agent's door call?**

Treat it as a claim to review.
Reverting a commit cannot undo an email already sent or data already written in a new format.
Give the agent the ticket or specification and your repository's rules for irreversible changes.

**Does the repository's request template take precedence?**

The skill carries its own format and has no discovery step for an existing template.
State how Summary, Evidence, and Merge danger should fit into your required template in the repository's agent guidance.

**Does it update the body as the request changes?**

It writes the body at one point in time.
Ask for a rewrite after substantial changes during review.

**What goes in Evidence when there is no user interface?**

Use the failing and passing test, or changed console output.
The screenshot recommendation applies when the change is visual; a statement that tests pass is not a before/after pair.

**Why does Mermaid appear as source text?**

The body is Markdown, and rendering depends on where you view it.
Use a call tree, file tree, or shaped diff when your review surface does not render diagrams.

## It's working if

- The body opens with a picture, not a paragraph, and the picture is small enough to read in one glance.
- A reviewer can say what the change is for without opening the diff.
- The evidence section shows both states, not just the passing one.
- Reviewers stop asking "is this safe to merge?" in the comments, because the door and the blast radius already answered it.
- You recognise the shape it picked as the one you would have drawn.

## Where it fits

A **chain step**, the last one before the work leaves your machine: `implement` → `code-review` → `to-pull-request`. Its neighbours are [code-review](./code-review.md), because the findings it produces are what the evidence and merge danger sections have to be honest about, and [address-feedback](../../../skills/experimental/address-feedback/SKILL.md), which picks the thread back up once reviewers reply. After a session worth learning from, [improve-agent-environment](../upkeep/improve-agent-environment.md) proposes changes to the checks and standards future reviews use. For the whole map, see [what-is-next](../getting-started/what-is-next.md).
