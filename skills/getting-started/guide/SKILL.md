---
name: guide
description: "Choose the next skill, development workflow, or session boundary from the current situation."
disable-model-invocation: true
---

# Guide

`/guide` recommends the smallest useful next move and stops. Read the relevant skill before making a consequential claim about its behavior. Both development workflows use project-owned documents, so switching between them preserves agreements and progress.

## Choose the development workflow

| Situation | Route |
| --- | --- |
| You want explicit planning and execution phases | `/specify → /taskify → /implement → /review-and-refactor`. Skip task decomposition when the selected work is small enough to implement directly. |
| You want to discover behavior while building a living application | `/iterate` clarifies, implements, and verifies one useful batch at a time. |
| You want to clarify a decision without starting development | `/refine`, the general interview discipline. The caller records useful results in the appropriate documents. |

### Planned development

1. `/specify` reads the current context, resolves only outstanding decisions through `refine`, and writes or updates the selected capability's requirements and specifications. Settled decisions go straight to synthesis.
2. When conversation cannot settle a design question, suggest `/prototype`. The user requests or approves a scoped experiment. Its validated answer and evidence feed the specification; useful code can be integrated after production checks without mandatory rebuilding. `/research` handles consequential unknown external facts.
3. `/taskify` decomposes selected work into coherent tasks with acceptance criteria and blocking dependencies. Drafts remain local until explicit publication. The word task is tracker-neutral: a remote tracker may call it an issue or ticket.
4. `/implement` builds an authorized task, specification, or small approved batch. `/implement-all` instead implements a task graph on one integration branch, using concurrent work where dependencies allow.
5. `/test-first` establishes behavior through red/green at agreed seams. `/review-and-refactor` reviews Standards and Specifications against a fixed starting point, applies supported refactors, and verifies them. An explicit living agreement is valid review input; a separate specification is not mandatory for an iterative batch.
6. `/draft-merge-request` writes a request body with a summary visual, before/after evidence, and merge danger. It does not push or open the request. `/implement-all` can publish or open one only when explicit destination-and-scope authorization covers those actions; tracker configuration alone is not authorization.

### Just-in-time development

`/iterate` primarily maintains `documentation/backlog.md`, `documentation/work-in-progress.md`, and root `CHANGELOG.md`. It respects existing requirements and specifications but does not generate capability documents or tasks just to run a batch.

It evolves the living application, including alternative implementations when useful. A prototype rebuild is not a prerequisite. Approved interaction or appearance needs user acceptance where judgment matters; routine internal changes use agreed automated checks.

When unclear scope, competing outcomes, or dependencies prevent choosing an increment, it invokes `prioritize`. That branch retains candidates and deferrals, recommends one focus, and gets approval without requiring implementation tasks. Small clear changes bypass it. Completing one outcome does not approve the next.

Research, test-first work, diagnosis, and milestone reviews remain conditional branches.

## Shared project documents

The `document` skill owns the shared project documents: requirements, specifications, drafts, tasks, backlog, work-in-progress, and the changelog. When the user asks what each one holds, read its `PROJECT-DOCUMENTS.md`. Both workflows use the same documents, so switching between them keeps agreements and progress; `iterate` writes light changelog records and the planned workflow writes full ones.

`GLOSSARY.md`, architecture decision records, and `GUIDELINES.md` retain their separate roles: domain language, consequential decisions, and judgment-call review rules.

## On-ramps and open questions

| Situation | Next move |
| --- | --- |
| A published request needs verification and a maintainer decision | `/triage`, then implementation of its ready brief or further specification as needed. |
| What to build is still undecided, and settling it needs research, prototypes, or interviews across several sessions | `/graphify` builds a decision graph and resolves one decision per session. |
| What to build is known, but there are several candidate outcomes and the question is which comes first | `/prioritize` groups outcomes and recommends one focus within a session. |
| Agreed behavior needs splitting into delivery work | `/taskify` produces tasks with acceptance criteria and blockers. |
| One decision or plan needs stress-testing | `/refine` interviews until the frontier is empty. |
| A recurring work loop needs an implementable design | `/design-workflow`. |
| An architectural seam is causing friction | `/improve-codebase-architecture`, then explore the selected candidate. |
| The missing facts are in another person's head | `/ask-someone-else`, then bring the answers into refinement or specification. |

## Session boundaries

Keep authoritative work state current before changing context.

| Boundary | Use it when |
| --- | --- |
| Continue | The current context remains relevant to the next step. |
| Clear | The next task is self-contained and its authoritative sources preserve what it needs. |
| `/hand-off`, then `/take-over` | Moving between sessions, workspaces, or agents needs session-specific context and source pointers. |
| Compact | You need the same session with less conversational detail; preserve unresolved agreements, running assignments, and recovery pointers first. |

`hand-off` writes a new versioned file in `.agents/handoffs/`; `take-over` reads the latest one and follows earlier pointers only when needed. The agent can also run `hand-off` on its own, which is how the `setup-auto-handoff` gate gets a handoff before compaction. Live working state does not replace the session handoff, and the handoff should not duplicate all project documents.

## Standalone and supporting skills

| Skill | Responsibility |
| --- | --- |
| `/debug` | Build a tight reproduction loop, diagnose, fix, and regression-test. |
| `/resolve-merge-conflicts` | Resolve an in-progress conflict by intent and finish the operation. |
| `/improve-skills` | Review a session's skill use with the user and report skill problems as an issue on the skills repository. |
| `/re-explain` | Re-explain a message with missing context and canonical vocabulary. |
| `/illustrate` | Explain with the smallest useful diagram, sketch, or HTML artifact. |
| `/teach` | Maintain a mission-grounded teaching workspace across sessions. |
| `/optimize-process` | Improve a recurring process using actual friction and evidence. |
| `/model-domain` | Actively sharpen domain language and record qualifying decisions or guidelines. |
| `/design-modules` | Design deep modules, useful seams, and testable interfaces. |
| `/document` | Maintain technical documents and shared project artifacts. |
| `/write-for-agents` | Write skills, steering instructions, and agent references. |
| `/walk-through` | Generate an interactive script for steps only a human can perform. |
| `/unslop` | Remove filler and recurring AI writing patterns from prose. |
| `/setup-ai-tooling` | Configure verified tool integrations, measurements, and recovery methods. |
| `/monitor-ai-tooling` | Report actual usage, quality, gaps, and evidence-supported benefits. |
| `/setup-delegation-policy` | Install machine-wide delegation and model-tier policy. |
| `/setup-git-hooks` | Configure versioned commit checks. |
| `/setup-git-guardrails` | Block dangerous Git operations at supported enforcement layers. |
| `/setup-auto-handoff` | Gate supported compaction on a fresh handoff. |
| `/address-feedback` | Assess review feedback from any source, implement approved changes, and deliver approved replies. |
| `/publish-message` | Publish established findings to any connected service after approval of exact text and destination. |
| `/work-in-tree` | Create or reuse an isolated task checkout. |
| `/sync-tree` | Transfer committed work to its verified corresponding local branch. |
| `/rebase` | Rebase branches with recovery state, intent checks, and separately approved publication. |
| `/classify` | Classify safe-to-send text with a third-party API; retain uncertain results. |
| `/memorize` | File lessons where the next agent will look, and reuse saved scripts before writing new ones. |

## Setup

Tell the user to run `/setup-ai-workspace` before a tracker-dependent flow when the tracker configuration is missing. It configures task authority, writing conventions, triage roles, and domain layout. Its optional stage offers `setup-ai-tooling`, `setup-git-hooks`, `setup-git-guardrails`, `setup-auto-handoff`, and `/setup-delegation-policy`. `iterate` does not require tracker setup merely to maintain its local working documents.
