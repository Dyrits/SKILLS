---
name: what-is-next
description: "Figure out the next move: which skill or flow fits your situation, or which boundary option (continue, clear, hand-off, compact) fits the moment. A router over the skills and flows in this repository."
disable-model-invocation: true
---

# What Is Next

You don't remember every skill or what to do next, so ask.

A **flow** is a path through the skills. Most paths run along one **main flow**, and two **on-ramps** merge onto it. Everything else is standalone, or a vocabulary layer that runs underneath.

## The main flow: idea → ship

The route most work travels. You have an idea and want it built.

1. **`/grill-with-documentation`** sharpens the idea by interview. Start here whenever you are **working in a working directory**: it's stateful, retaining what it learns in `GLOSSARY.md` and ADRs. (No working directory? Use `/grill-me` instead, covered under Standalone. Both run the same `/grilling` primitive; `grill-with-documentation` is the one that leaves a paper trail, which makes it the better of the two whenever a repository is there to leave it in.)
2. **Branch: can you settle every question in conversation?** If a question needs a runnable answer (state, business logic, a UI you have to see), detour through a prototype, bridged by **`/hand-off`** in both directions (a prototype lives in its own directory, which is exactly what `/hand-off` is for; see Phase boundaries):
   - **`/hand-off`** out, then **`/take-over`** in the fresh session against the newest file,
   - **`/prototype`** to answer the question with throwaway code,
   - **`/hand-off`** back what you learned, and reference it from the original idea thread.
3. **Branch: is this a multi-session build?**
   - **Yes** → **`/to-specifications`** (turn the thread into a specification), then **`/to-tickets`** to split it into tracer-bullet tickets, each declaring its **blocking edges**. Both stay under `.refinement/<issue-key>/` until the user explicitly publishes them to the system-of-record tracker. Tickets on a local markdown tracker are worked blockers-first by hand; published tickets use native blocking links where the tracker supports them, so any ticket whose blockers are done can be grabbed. Kick off **`/implement`** per ticket, **`/clear`ing context between each one**. Each ticket is self-contained, so the last one's context is disposable. **`/implement-all`** is the alternative for the whole task graph: implementer subagents build the ready frontier in background worktrees and merge their work onto one integration branch. A pull or merge request is optional, according to the tracker workflow or your instruction.
   - **No** → **`/implement`** right here, in the same context window.

   Either way, **`/test-driven-development`** establishes behavior through red/green, then **`/code-review-and-refactor`** owns the refactor phase.
   Standards and Specifications reviewers inspect the same starting diff independently, one coordinator applies supported refactors, and the same reviewers verify the result.
   `/implement` drives both phases per ticket; `/implement-all` runs the refactor phase over the combined integration branch after all tickets land.
   Reach for **`/test-driven-development`** on its own to build concrete behavior test-first, and **`/code-review-and-refactor`** on its own to review and refactor existing changes against a fixed point.

4. **The work leaves your machine.** **`/to-pull-request`** writes the body of the pull or merge request: one summary visual sized to the single point the change makes, before/after **evidence**, and the **merge danger** (a one-way or two-way door, and the blast radius). It writes the body and stops, so pushing the branch and opening the request stay yours, except under **`/implement-all`**, which opens one when the tracker workflow or your instruction calls for it. Why the change exists comes from its **primary source**, the ticket or specification, never from reading the diff back at a reviewer who already has it open. When reviewers reply, **`/address-feedback`** (under Standalone) works the thread back.

5. **`/improve-agent-environment`** closes a session worth learning from. It reads the session's record and suggests improvements to navigation, checks, standards, steering files, and tooling, ordered by severity. Mechanical mistakes call for deterministic checks; judgement calls belong in `GUIDELINES.md`, read by `/code-review-and-refactor`. You choose which candidates to implement.

### Context hygiene

Keep steps 1–3 in **one unbroken context window** (don't compact or clear until after `/to-tickets`) so the grilling, specification, and tickets all build on the same thinking. Each `/implement` then starts fresh, working from the ticket. Run `/improve-agent-environment` before clearing the session it should examine, or point a fresh run at that session's log.

The limit on this is the **smart zone**: the window (~150k tokens on state-of-the-art models) within which the model still reasons sharply. If a session approaches it before `/to-tickets`, don't push on degraded; `/compact` at the nearest phase boundary and carry on (see Phase boundaries).

## On-ramps

A starting situation that generates work, then merges onto the main flow.

- **Bugs and requests piling up** → **`/triage`**. It moves issues through triage roles and produces agent-ready issues, which **`/implement`** later picks up.

  Triage is only for issues **you didn't create**: bug reports, incoming feature requests, anything that arrives raw. Tickets that `/to-tickets` produced are already agent-ready, so **don't triage them**.

- **Something's broken** → **`/debug`**. For the hard ones: the bug that resists a first glance, the intermittent flake, the regression that crept in between two known-good states. It refuses to theorise until it has a **tight feedback loop** (one command that already goes red on *this* bug), then fixes with a regression test. Its post-mortem hands off to **`/improve-codebase-architecture`** when the real finding is that there's no good seam to lock the bug down.

- **A huge, foggy effort: a greenfield project or a huge feature build, too big for one session** → **`/wayfinder`**, the most cognitively demanding flow here. When the way from here to the destination isn't visible yet, it charts a **shared map** of **decision tickets** on the issue tracker and resolves them one at a time, producing **decisions, not deliverables**, until the fog is pushed back and the way is clear. Where **`/grill-with-documentation`** sharpens an idea you can hold in one session, wayfinder is for the idea you can't, and it's slower and denser, so save it for exactly that, never a well-scoped feature.

  When the map clears, **it hands off, it doesn't build**: merge onto the main flow at **`/to-specifications`**, which collapses the map's linked decisions into a buildable plan, then `/to-tickets` and `/implement` as usual. Looping the map straight into `/implement` skips that collapse and throws the linked detail away, so go straight to `/implement` only when the effort turned out genuinely small.

## Codebase health

Not feature work, just upkeep.

- **`/improve-codebase-architecture`** runs whenever you have a spare moment to keep the codebase good for agents to operate in. It surfaces **deepening opportunities**; picking one _generates an idea_ you can take into the main flow at `/grill-with-documentation`. It's the survey that finds the candidates; **`/codebase-design`** (below) is the bench you design the chosen one on.

## Vocabulary underneath

Two model-invoked references that run *beneath* the other skills, each the single source of truth for its vocabulary. Reach for them directly when the **words**, not the process, are the problem; or let the skills above pull them in.

- **`/domain-modeling`**: sharpen the project's *domain* language: challenge a fuzzy term, resolve an overloaded word ("account" doing three jobs), record a hard-to-reverse decision as an ADR. It's the active discipline `/grill-with-documentation` drives to keep `GLOSSARY.md` a clean glossary. It also interviews you to create `GUIDELINES.md` when the review or architecture skills find it missing.
- **`/codebase-design`** is the deep-module vocabulary (module, interface, depth, seam, adapter, leverage, locality) for designing a module's *shape*: a lot of behaviour behind a small interface at a clean seam. `/test-driven-development` and `/improve-codebase-architecture` both speak it.

## Phase boundaries

A **phase** is a chunk of work inside a session: the grilling, the implementation, the QA. At the **boundary** between two of them you have five options, and picking between them is the fuzziest decision in this whole map:

- **Continue**: stay put. Costs nothing, loses nothing.
- **`/clear`**: empty the window, when nothing here matters to what's next.
- **`/hand-off`** writes a portable markdown file. Narrow: only for a **new harness**, a **new directory**, a **colleague**, or forking a side task **mid-phase**. What it buys is portability. **`/take-over`** is its far side: the first thing you type in the fresh session, resuming from the newest handoff in `.agents/handoffs/` without pasting a path.
- **Subagent**: send a tightly-scoped task to its own window and get a report back. Which subagent, and on which model tier, is a standing rule rather than a per-boundary decision: **`/setup-delegation-policy`** (under Standalone) installs it once into your global steering files, and every session carries it from then on.
- **`/compact`** compresses this context and seeds a fresh session with it. The **default**, at the bottom of the tree rather than the first reach.

Read [PHASE-BOUNDARIES.md](PHASE-BOUNDARIES.md) for the ordered tree: the five questions, the reasoning behind each branch, and why the primary-source cost makes **Continue** the one to rule out first. Make the decision **at** a boundary; mid-phase, continue or split the rest into subagents.

## Standalone

Off the main flow entirely.

- **`/work-in-tree`** is experimental and installed separately from the plugin. It creates or reuses an isolated Git checkout before task edits, keeps the original checkout unchanged, and records the repository and branch that should receive the completed work. Use it before implementation when you want worktree isolation.
- **`/sync-tree`** is its separately invoked return step. It transfers committed work to the verified original local branch. Linked worktrees already share same-named refs; a different target can fast-forward, while a history replacement needs explicit approval and an exact ref comparison. It does not publish upstream. Delta users can also invoke it through Land Changes.
- **`/setup-ai-tooling`** is experimental and installed separately from the plugin. It provisions free tools for this project and missing global dependencies, reuses existing integrations, verifies complete review evidence, and records a baseline in `documentation/agents/ai-tooling.md`. Reach for it directly when setting up tools, or select the optional tooling stage in `/setup-ai-workspace`, which invokes the same procedure when available. It is model-invoked so workspace setup can reach it, with installation limited to an explicit setup request.
- **`/monitor-ai-tooling`** is experimental and installed separately from the plugin. It is the user-invoked report after tools have collected measurements. It reads existing analytics, distinguishes output reduction from actual provider usage, and reports quality findings and attribution gaps. Setup owns configuration changes; monitoring owns the recurring report and runs no background model analysis.
- **`/optimize-process`** maps a recurring work process, finds waiting and rework, and proposes a better sequence with impact stated in realistic human and agent time. Reach for it when a workflow has too many steps, handoffs, or delays; take an implementation idea into the main flow if it needs building.
- **`/grill-me`**: the same relentless interview as `/grill-with-documentation`, but **stateless**: it saves nothing locally and builds no `GLOSSARY.md`. Reach for it when you are **not working in a working directory** (sharpening a plan, a design, a piece of writing, anything with no repository under it). If you are in a working directory, use `/grill-with-documentation` instead: it runs the same interview and leaves a paper trail, so it is strictly the better one.
- **`/grilling`** is the interview primitive itself: rounds, the frontier, facts are the agent's job and decisions are yours. `/grill-me` and `/grill-with-documentation` are the two named ways in, and `/triage`, `/wayfinder` and `/improve-codebase-architecture` all run it internally. Reach for it directly only when you want the interview with no wrapper around it.
- **`/resolve-merge-conflicts`** works an in-progress merge or rebase conflict hunk by hunk, resolving by **intent** traced to each side's primary source rather than by picking lines, then finishes the operation. It never runs `--abort`. Standalone and off every flow: reach for it when you are already mid-conflict.
- **`/prototype`** is a small, throwaway program that answers one design question: does this state model feel right, or what should this UI look like. Throwaway is a constraint on how the code is written, not a promise to destroy it: the answer folds into the real code, and the prototype itself is kept as a **primary source** on a `prototype/<name>` branch out of main, pointed at from the implementation issue. It's the detour in step 2 of the main flow, but reach for it any time a design question is hard to settle on paper.
- **`/research`**: delegate reading legwork to a **background agent**: it investigates a question against **primary sources**, then leaves a cited Markdown file in the repository. Keep working while it reads. The file it produces is something to take *into* the main flow at `/grill-with-documentation`, since research feeds the thinking rather than replacing it.
- **`/address-feedback`** takes an existing pull request, merge request, issue, or ticket thread through one closed loop: account for every substantive comment, recommend dispositions and changes, wait for approval, implement and validate the approved plan, then draft every reply and wait for approval before posting. It is experimental because the final step writes to other people's tracker threads.
- **`/publish-message`** publishes conclusions already reached in the conversation as a tracker comment, review summary, or requested set of inline suggestions. It accepts findings from any review source and is experimental because it posts to tracker threads.
- **`/classify`** sends text and labels to classifier.dev for sorting, independent dimensions, or multiple tags. Use it to filter batches before reading them, or request an API verdict with `/classify <text> [option, option, option]`. It reports available scores and keeps uncertain filter results for review. Experimental, because the text goes to a third-party API.
- **`/setup-delegation-policy`** installs one standing rule into the global steering files on this machine: at the top of a fresh unit of work, decide whether it runs here, in one subagent, or split across several, and on which model tier. It is a steering file rather than a skill on purpose, because the decision has to happen **before** any reasoning has bent it, which is exactly when nothing thinks to invoke a skill. Its one rule is to choose the least expensive model capable of finishing the bounded task reliably, expressed in four tiers (**Light**, **Balanced**, **Heavy**, **Frontier**). Before each dispatch, it checks for the latest available version within the chosen model family and respects any user-specified version. In Codex sessions with a spawn tool, use its available per-call model choice. On OpenCode, ZCode and Gemini CLI it also writes one subagent per tier, because those bind a model per named agent. Run once per machine. Experimental, because it writes outside the repository, into your machine-wide configuration.
- **`/ask-someone-else`** comes in when the thing blocking you isn't in your head or the codebase but in **someone else's**, and it writes them a questionnaire to fill in. It's the inverse of `/grill-me`: instead of interviewing you about the subject, it interviews you about the **send** (who it's going to, what you need back) and aims the questions at the gap. What comes back is material for `/grill-with-documentation` or `/to-specifications`.
- **`/wizard`** is for the steps only a **human** can take: provisioning infrastructure, setting up credentials or CI secrets, clicking through an unfamiliar third-party dashboard, running a one-off migration or cutover. It generates an interactive bash script that opens each URL, captures each value, and writes it into `.env` and GitHub secrets, so the procedure stops being something you re-explain to an agent every time. Model-invoked, so the agent reaches for it the moment it hits a wall only you can pass. If the agent could just do it itself, it should; this is for where a human is genuinely in the loop.
- **`/wait-what`** is the corrective for a message that didn't land. Use it mid-conversation, inside any other skill, and the agent re-pitches what it just said with the context you were missing, in plain English, using the `GLOSSARY.md` vocabulary. It works after the fact; `/grill-with-documentation` is the upfront cure, because a shared language agreed early is what stops the jargon arriving at all.
- **`/teach`**: learn a concept over multiple sessions, using the current directory as a stateful workspace.
- **`/show-me`** explains the current topic with the smallest useful visual: a diagram, code sketch, or focused HTML artifact. Use it when you need to see structure, flow, or a comparison; use `/wait-what` to rephrase an explanation, and `/prototype` to settle a design question through experimentation. Model-invoked, so other skills can also reach it.
- **`/writing-for-agents`** is the reference for writing documents agents consume: skills, AGENTS.md, pointed-at docs.
- **`/documentation`** writes and maintains technical documentation such as README files, API references, runbooks, architecture documents, and onboarding guides. Use `/writing-for-agents` alongside it when the document instructs agents.
- **`/unslop`** applies to writing in any language. It preserves meaning and tone while removing recurring language and structure patterns.

## Precondition

Every repository drafts under `.refinement/` first, whether its tracker is a remote or the local `backlog/`. Explicit publication selects which artifacts become tracker records; an issue's links to working notes do not promote those notes.

**`/setup-ai-workspace`**: run before a tracker-dependent flow to configure the system-of-record issue tracker (local markdown or remote), ticket-writing convention, triage roles, and documentation layout. Custom issue trackers and team ticket templates also work.
Its optional tooling stage calls the separately installed experimental `setup-ai-tooling` when available; a project can use the tracker workflow without selecting that stage.
