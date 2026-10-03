Upstream source: `pr`, verified in the `d81f3a1` tree, now `draft-merge-request` in this fork.

## What it does

`draft-merge-request` writes the body of a pull request, or a merge request on GitLab, in a fixed three-part shape: a **summary** visual, **evidence** as a before/after pair, and the **merge danger**. It is a format reference, not a workflow: it does not open the request, push the branch, or review anything.

It explains the reviewer's missing information rather than narrating the diff. The reason for a change comes from its authoritative agreement: a task, living specification, applicable requirements, or approved working-state scope. The diff determines which visual shows the change; it does not establish that every obligation was met.

## When to reach for it

Type `/draft-merge-request`, or the agent reaches for it automatically when a task fits: writing a request description, rewriting one that reviewers bounced, or closing out a branch that is about to go up for review.

| Where you are | What to run |
| --- | --- |
| A branch is finished and needs a description a human can read fast | `/draft-merge-request` |
| The change is not reviewed yet | [review-and-refactor](../workflow/review-and-refactor.md) first, then this |
| The ticket is not built yet | [implement](../workflow/implement.md), which closes out with the review |
| The request is already open and reviewers have commented | [address-feedback](../workflow/address-feedback.md) |
| The conclusion is already written and just needs posting | [publish-message](../productivity/publish-message.md), after approval of text and destination |

## The summary is a shape, not a paragraph

The summary's job is one visual sized to the single point the change makes.
The skill calls [illustrate](../productivity/illustrate.md) to choose the shape and render it inline in the request body.
If `illustrate` is not installed, it uses the formats named in the template to produce the summary itself.

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
No. It writes the body and stops. Pushing the branch, opening the request, and setting its reviewers stay yours, or stay with [implement-all](../workflow/implement-all.md), which opens a request for a whole specification when the tracker workflow or user calls for one.

**Why is it model-invoked when other planned workflow steps are user-invoked?**
Because other skills need to reach it. [implement-all](../workflow/implement-all.md) can open a request as part of its run, and a body format that only a human can trigger would be unreachable at exactly the moment it is needed. Typing `/draft-merge-request` still works: model-invocation adds the agent's reach, it never removes yours.

**It described the diff instead of explaining the change.**
That is the failure the skill is written against, and it usually means the primary source was not in the window. Give it the ticket or the specification, not just the branch, and the summary has something to be about.

**Where did `pr` go?**
It was named `pr` upstream. This fork first adopted the full-word name `to-pull-request`, now `draft-merge-request`. The current planned workflow uses [specify](../workflow/specify.md) and [taskify](../workflow/taskify.md), not old-name aliases.

**Is there a matching skill for commit messages?**
No. The original proposal upstream paired a `/to-commit` with this one, so the commit template would feed the request body. Only the request half exists, and [implement](../workflow/implement.md) still commits with a single line of its own guidance.

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

`draft-merge-request` is a chain step after [review-and-refactor](../workflow/review-and-refactor.md), and a standalone format reference when rewriting a description. Its evidence must reflect agreed checks, actual results, and any pending human acceptance rather than declaring delivery prematurely. [address-feedback](../workflow/address-feedback.md) continues when reviewers reply. [improve-agent-environment](../upkeep/improve-agent-environment.md) reviews useful session lessons, and [guide](../getting-started/guide.md) maps both development workflows.
