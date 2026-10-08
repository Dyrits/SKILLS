---
name: guide
description: "Choose the next skill, development workflow, or session boundary from the current situation. Use when the user asks which skill or workflow to use next, or when a flow stalls and the next move is unclear."
metadata:
  forks: "mattpocock/skills/skills/engineering/ask-matt"
---

# Guide

`/guide` recommends the smallest useful next move and stops. Read the relevant skill before making a consequential claim about its behavior. Both development workflows use project-owned documents, so switching between them preserves agreements and progress.

## Choose the development workflow

| Situation | Route |
| --- | --- |
| You want explicit planning and execution phases | Once per system, `/delineate → /architect`; then per capability, `/specify → /engineer → /taskify → /implement → /review-and-refactor`. Skip a step whose result already exists, and task decomposition when the selected work is small enough to implement directly. |
| You want to discover behavior while building a living application | `/iterate` clarifies, implements, and verifies one useful batch at a time. |
| You want to clarify a decision without starting development | `/interview`, the general interview discipline. The caller records useful results in the appropriate documents. |

### Planned development

Work is described on two levels, each from two sides. Functional comes before technical on each level; no step requires the one before it, but each reads what exists.

| | Functional: what must be true | Technical: how the code makes it true |
| --- | --- | --- |
| **System**, once and when it changes | `/delineate`: purpose, actors, contexts, capabilities, system-wide requirements, glossary | `/architect`: stack, parts, data ownership, integrations, deployment, how each requirement is met |
| **Capability**, each one | `/specify`: observable behavior, edge cases, acceptance, capability requirements | `/engineer`: modules, interfaces, data, seams, where each test attaches |

Every requirement, functional or not, sits in the functional column; the technical skill of the same level answers it. `/codify` sits outside the grid: it sets how code is written and enforced, best once the stack is chosen.

1. `/specify` reads the current context, resolves only outstanding decisions, and writes or updates the selected capability's requirements and specifications. Settled decisions go straight to synthesis. `/engineer` then designs the capability inside the architecture; skip it when the capability is small enough that its design is obvious from the code.
2. When conversation cannot settle a design question, suggest `/prototype`. The user requests or approves a scoped experiment. Its validated answer and evidence feed the specification; useful code can be integrated after production checks without mandatory rebuilding. `/research` handles consequential unknown external facts.
3. `/taskify` decomposes selected work into coherent tasks with acceptance criteria and blocking dependencies. Drafts remain local until explicit publication. The word task is tracker-neutral: a remote tracker may call it an issue or ticket.
4. `/implement` builds an authorized task, specification, or small approved batch. `/divide-and-conquer` instead implements a task graph on one integration branch: it routes each task to the least expensive capable agent, asks the user to approve that routing table, runs the tasks concurrently where dependencies allow, and reviews once.
5. `/test-first` establishes behavior through red/green at agreed seams. `/review-and-refactor` reviews Standards and Specifications against a fixed starting point, applies supported refactors, and verifies them. An explicit living agreement is valid review input; a separate specification is not mandatory for an iterative batch.
6. `/draft-merge-request` writes a request body with a summary visual, before/after evidence, and merge danger. It does not push or open the request. `/divide-and-conquer` can publish or open one only when explicit destination-and-scope authorization covers those actions; tracker configuration alone is not authorization.

### Just-in-time development

`/iterate` primarily maintains the backlog, working state, and changelog. It respects existing requirements and specifications but does not generate capability documents or tasks just to run a batch.

It builds each batch with its own copy of the `implement` discipline, or of `divide-and-conquer` when a batch splits into independent tasks. It evolves the living application, including alternative implementations when useful. A prototype rebuild is not a prerequisite. Approved interaction or appearance needs user acceptance where judgment matters; routine internal changes use agreed automated checks.

When unclear scope, competing outcomes, or dependencies prevent choosing an increment, it runs its own copy of the `prioritize` branch. That branch retains candidates and deferrals, recommends one focus, and gets approval without requiring implementation tasks. Small clear changes bypass it. Completing one outcome does not approve the next.

Research, test-first work, diagnosis, and milestone reviews remain conditional branches.

## Shared project documents

The shared project documents are these kinds: requirements (obligations), capability specifications (agreed behavior and acceptance), drafts (unresolved proposals), tasks, the backlog (candidates and deferrals), work-in-progress (active work and resumption), the changelog (agreements and deliveries), the glossary (domain terms), conventions (code rules no tool enforces), and decision records (hard-to-reverse decisions). The skill that creates one adds a line for it to `AGENTS.md`, and every other skill finds it there, so no skill depends on another's paths. Every skill that reads or writes them carries the same rules for them. Both workflows use the same documents, so switching between them keeps agreements and progress; `iterate` writes light changelog records and the planned workflow writes full ones.

The glossary, decision records, and conventions retain their separate roles: domain language, consequential decisions, and project-agnostic code conventions. `/delineate` settles the terms, `/codify` the conventions, and `/architect` and `/engineer` the decisions they record. The domain outline, the architecture document, and each capability's blueprint belong to the skills that write them.

## On-ramps and open questions

| Situation | Next move |
| --- | --- |
| A published request needs verification and a maintainer decision | `/triage`, then implementation of its ready brief or further specification as needed. |
| What to build is still undecided, and settling it needs research, prototypes, or interviews across several sessions | `/graphify` builds a decision graph and resolves one decision per session. |
| What to build is known, but there are several candidate outcomes and the question is which comes first | `/prioritize` groups outcomes and recommends one focus within a session. |
| Agreed behavior needs splitting into delivery work | `/taskify` produces tasks with acceptance criteria and blockers. |
| One decision or plan needs stress-testing | `/interview` interviews until the frontier is empty. |
| A recurring work loop needs an implementable design | `/design-workflow`. |
| An architectural seam is causing friction | `/improve-codebase-architecture`, then explore the selected candidate. |

## Session boundaries

Keep authoritative work state current before changing context. The decision belongs only at a phase boundary, never mid-phase; read [PHASE-BOUNDARIES.md](PHASE-BOUNDARIES.md) for the definition and the reasoning behind the order.

Work the table top to bottom. The first row that fits wins.

| Boundary | Use it when |
| --- | --- |
| Continue | The next step needs this context as a primary source, or enough room remains for it to fit. |
| Clear | Everything in this session is disposable for the next task, and its authoritative sources preserve what it needs. |
| `/hand-off` | Something travels: a new harness, directory, repository, or colleague, or a side task forked mid-phase. It needs session-specific context and source pointers. |
| Subagent | The next task is tightly scoped enough to run without steering (an automated review is the standard case) and this session stays untouched. |
| Compact | None of the above fit: relevant context, same harness and directory, and you stay in the loop. Pass an instruction naming what the next phase needs; preserve unresolved agreements, running assignments, and recovery pointers first. |

`hand-off` writes a new versioned, self-contained file in `.agents/handoffs/` and points to it from `AGENTS.md`; the file says how to resume from it, following earlier handoffs only when needed. Live working state does not replace the session handoff, and the handoff should not duplicate all project documents.

## Standalone and supporting skills

| Skill | Responsibility |
| --- | --- |
| `/debug` | Build a tight reproduction loop, diagnose, fix, and regression-test. After the fix, `/improve-environment` asks what would have prevented the bug; when no correct seam existed for the test, follow with `/improve-codebase-architecture`. |
| `/resolve-merge-conflicts` | Resolve an in-progress conflict by intent and finish the operation. |
| `/improve-skills` | Review a session's skill use with the user and report skill problems as an issue on the skills repository. |
| `/improve-environment` | Trace a session's friction to the project's environment and apply the agreed checks, guardrails, pointers, and steering changes. |
| `/re-explain` | Re-explain a message with missing context and canonical vocabulary. |
| `/illustrate` | Explain with the smallest useful diagram, sketch, or HTML artifact. |
| `/teach` | Maintain a mission-grounded teaching workspace across sessions. |
| `/optimize-process` | Improve a recurring process using actual friction and evidence. |
| `/codify` | Define or audit the project's code conventions. |
| `/write-for-agents` | Write skills, steering instructions, and agent references. |
| `/walk-through` | Generate an interactive script for steps only a human can perform. |
| `/unslop` | Remove filler and recurring AI writing patterns from prose. |
| `/setup-ai-tooling` | Configure verified tool integrations, measurements, and recovery methods. |
| `/monitor-ai-tooling` | Report actual usage, quality, gaps, and evidence-supported benefits. |
| `/setup-delegation-policy` | Install machine-wide delegation and model-tier policy. |
| `/setup-git-hooks` | Configure versioned commit checks. |
| `/setup-git-guardrails` | Ask before destructive Git operations at supported enforcement layers. |
| `/address-feedback` | Assess review feedback from any source, implement approved changes, and deliver approved replies. |
| `/publish-message` | Publish established findings to any connected service after approval of exact text and destination. |
| `/work-in-tree` | Create or reuse an isolated task checkout. |
| `/sync-tree` | Transfer committed work to its verified corresponding local branch. |
| `/rebase` | Rebase branches with recovery state, intent checks, and separately approved publication. |
| `/swarm` | Fan independent pieces of a task out to fast, low-cost agents you select, then merge and spot-check their reports. Dependent tasks on one integration branch go to `/divide-and-conquer`. |
| `/memorize` | File lessons where the next agent will look, and reuse saved scripts before writing new ones. |

## Setup

Tell the user to run `/setup-ai-workspace` before a tracker-dependent flow when the tracker configuration is missing. It configures task authority, writing conventions, and triage roles. Tooling, commit hooks, Git guardrails, and the delegation policy are separate setups: `/setup-ai-tooling`, `/setup-git-hooks`, `/setup-git-guardrails`, and `/setup-delegation-policy`. `iterate` does not require tracker setup merely to maintain its local working documents.
