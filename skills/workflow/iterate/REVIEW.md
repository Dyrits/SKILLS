# Review and refactor the batch

Adapted from the `review-and-refactor` skill, without its publication step: publication of the integration branch follows the run's own authorization rules.

This is the **refactor** phase of red-green-refactor.
Implementation establishes the required behavior with passing tests; this skill then checks standards and compliance with specifications and applies supported refactors while preserving behavior.

Two independent axes inspect the same starting diff:

- **Standards**: does the code conform to the repository's documented coding standards, and which baseline smells justify a refactor?
- **Specifications**: does the code faithfully implement the originating behavior agreement, and does the refactor preserve its requirements?

Reviewers gather evidence and propose concrete changes.
The coordinating agent checks their evidence and performs the edits, then asks the same reviewers to verify the result using their existing context.
A request for a report alone ends after review, with findings and no edits.

## Process

### 1. Pin the starting state

Resolve the fixed point the user supplies, such as a commit, branch, tag, `main`, or `HEAD~5`.
If none is supplied, ask for one.
When an implementation workflow supplies its starting commit, use it as the fixed point.
Resolve the fixed point and `HEAD` to commit IDs, and record their merge-base once.

Capture the starting diff against that merge-base before any refactor:

- For committed work, use `git diff <merge-base> <starting-HEAD>`.
- For work in progress, use `git diff <merge-base>` to include the current state of tracked files, including staged and unstaged changes.
- Include untracked files belonging to the requested work as separate new-file patches or snapshots, without staging them; record which paths are included.

Read `git status --short` to distinguish the requested work from unrelated local edits, and preserve unrelated edits throughout the run.
If file ownership is unclear, resolve that scope with the user before editing those files.
Restrict every captured diff to the agreed work scope.
Save the starting patch, starting contents of reviewed files, commit list (`git log <fixed-point>..<starting-HEAD> --oneline`), and review scope outside the repository for both reviewers.
A bad reference or an empty complete diff ends the run before dispatch.

### 2. Identify the originating behavior agreement

The project documents and their rules are in [PROJECT-DOCUMENTS.md](PROJECT-DOCUMENTS.md); its terms apply.
Recover the authorized behavior from the caller or user, tasks, specifications and requirements, or a user-approved batch in working state.

When `AGENTS.md` points to a task tracker configuration, fetch relevant task references through its workflow.

Freeze copies or revisions of the originating agreement and the verification evidence alongside the starting diff for both reviewers. Distinguish agreed behavior from unresolved proposals in a capability's draft and unapproved backlog candidates. Do not infer the agreement solely from the implementation under review.

If no behavior agreement is recoverable, ask the user to supply it or explicitly consent to Standards alone. Only after that consent skip the Specifications reviewer and report "no specifications available".

### 3. Identify the standards sources

Find repository instructions about how code should be written: the conventions file and other standards documents `AGENTS.md` points to, `CONTRIBUTING.md`, and applicable steering files.
Read the conventions file first when it exists.
When it is missing and no other standards document turns up, continue with the smell baseline alone, and report that the repository documents no coding standards.
Read relevant decision records and the glossary when they constrain the changed code.

On top of whatever the repository documents, the Standards axis always carries the **smell baseline** below: a fixed set of Fowler code smells (_Refactoring_, ch.3) that applies even when a repository documents nothing. Two rules bind it:

- **The repository overrides.** A documented repository standard always wins; where it endorses something the baseline would flag, suppress the smell.
- **Always a judgement call.** Each smell is a labelled heuristic ("possible Feature Envy"), never a hard violation. Like any standard here, skip anything tooling already enforces.

Each smell reads *what it is* → *how to fix*; match it against the diff:

- **Mysterious Name**: a function, variable, or type whose name doesn't reveal what it does or holds. → rename it; if no honest name comes, the design's murky.
- **Duplicated Code**: the same logic shape appears in more than one hunk or file in the change. → extract the shared shape, call it from both.
- **Feature Envy**: a method that reaches into another object's data more than its own. → move the method onto the data it envies.
- **Data Clumps**: the same few fields or params keep travelling together (a type wanting to be born). → bundle them into one type, pass that.
- **Primitive Obsession**: a primitive or string standing in for a domain concept that deserves its own type. → give the concept its own small type.
- **Repeated Switches**: the same `switch`/`if`-cascade on the same type recurs across the change. → replace with polymorphism, or one map both sites share.
- **Shotgun Surgery**: one logical change forces scattered edits across many files in the diff. → gather what changes together into one module.
- **Divergent Change**: one file or module is edited for several unrelated reasons. → split so each module changes for one reason.
- **Speculative Generality**: abstraction, parameters, or hooks added for needs the specifications do not have. → delete it; inline back until a real need shows.
- **Message Chains**: long `a.b().c().d()` navigation the caller shouldn't depend on. → hide the walk behind one method on the first object.
- **Middle Man**: a class or function that mostly just delegates onward. → cut it, call the real target direct.
- **Refused Bequest**: a subclass or implementer that ignores or overrides most of what it inherits. → drop the inheritance, use composition.

### 4. Review in parallel

Dispatch separate Standards and Specifications subagents with fresh contexts containing the working directory, captured starting patch and scope, resolved references, and commit list.
Wait for both reports before editing, and retain their agent identifiers for verification.

Both briefs require stable finding identifiers, file and hunk references, supporting evidence, a concrete proposed change, and the expected effect on behavior.
Tell each reviewer: "Perform your assigned axis directly, without editing files, running this review procedure, or spawning further agents."
Keep each report under 400 words without omitting findings; split a longer report into continuations when necessary.

The **Standards** brief includes the standards-source paths and the smell baseline from step 3 in full.
Ask for every documented violation, citing its source file and rule, and each plausible baseline smell, naming it and quoting the relevant hunk.
Distinguish documented violations from judgement calls, honor repository overrides, and skip rules already enforced by tooling.
For a smell, explain the concrete benefit of the proposed refactor rather than treating its label as sufficient evidence.

The **Specifications** brief includes frozen contents or revisions of the originating agreement, applicable requirements, and verification evidence.
Ask for missing or partial requirements, behavior beyond the agreed scope, and requirements implemented incorrectly.
Quote the originating agreement for each finding, and identify which existing tests or acceptance evidence establish the required behavior. Appearance and interaction acceptance may need human judgment; do not claim success from automated checks alone.

### 5. Apply supported refactors

Check each finding against its cited source and the current code before acting.
Keep identifiers and axes intact, and record each finding as accepted, dismissed with evidence, or awaiting a decision.

The coordinating agent applies accepted Standards changes, including supported smell refactors, in small steps while preserving observable behavior and the agreed public interfaces.
Use the existing tests as the behavior baseline and run relevant checks before and after the edits.
If those tests already fail, report the failure and establish which behavior is reliable before refactoring the affected code.

Specifications findings that require behavior changes belong to the **red/green** implementation phase.
Report the requirement and evidence back to the calling workflow or user for implementation; keep those findings open until implementation and its checks establish the required behavior.
A refactor cannot resolve a missing requirement by changing the specifications or weakening its tests.
Ask for a decision only when a finding needs a new business rule or interface agreement, and continue independent supported refactors while waiting.

Complete this step when every finding has a disposition and every accepted refactor has been applied or has a concrete reason it remains open.
Leave the refactors uncommitted for the caller or user to commit with the implementation.

### 6. Verify with the same reviewers

Capture the patch from the starting state to the final state, including changes to new files, and the complete final diff against the pinned merge-base.
Send these artifacts, finding dispositions, and check results back to the original reviewers.
Reuse their contexts rather than dispatching a new full review.

Each reviewer checks the accepted changes on its own axis and marks its original findings resolved or open with evidence.
The Standards reviewer verifies the applied refactors; the Specifications reviewer checks that required behavior and interfaces remain intact.
Both also inspect for regressions introduced by the refactor.

Run the checks required by the repository and relevant to the changes.
After formatting or lint auto-fixes, rerun only lint or typechecking unless a new behavioral change requires tests.
If verification finds a concrete regression, correct it and recheck the affected change.
Stop when the accepted refactors are verified or a specific blocker remains; further subjective smell suggestions stay in the report rather than starting an endless review loop.

### 7. Report the result

Present separate `## Standards` and `## Specifications` sections.
For each finding, give its evidence, disposition, applied change when relevant, and verification status.
Distinguish verified refactors from outstanding implementation requirements, rejected suggestions, and decisions still needed.
Include the checks run and their results, and say that edits remain uncommitted.
With no specifications, state "no specifications available" in that axis.

Update working state with open findings, evidence, blockers, and resumption pointers. Record completed agreements and deliveries in the changelog; a Delivery needs the agreed checks, beyond this report.

End with findings resolved and still open per axis, and the worst remaining issue within each axis.
Keep both axes separate rather than choosing one overall verdict.

## Why two axes

A change can follow every standard while implementing the wrong requirement, or satisfy the requirement while breaking repository conventions.
Independent review and separate reporting make both visible.
The refactor phase improves the implementation's structure; gaps in required behavior send the work back to red/green.
