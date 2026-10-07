# Skills audit

Date: 2026-10-06. Scope: every skill outside `deprecated/` (47 skills, after the removal of `setup-auto-handoff` in `f0d00c9`).

## Method and limits

- Five Sonnet agents each read every `SKILL.md`, its sibling files and its `evals/evals.json` for one bucket, read-only, against one rubric: usefulness, description quality, problems, coupling (hard or soft), rule violations from `AGENTS.md`, eval quality, verdict.
- The coordinating session spot-checked these claims and confirmed them: the stale compaction-gate text, 13 skills with the `document` hard stop, 24 skills with the install-fallback paragraph, the Codex claim in `setup-git-guardrails/SKILL.md:86`, and the spaced hyphens in `teach`.
- Taken from the agents and not re-checked: the guardrail-script bypasses (the agent said it ran the script on test inputs), the Codex execution-policy finding (the agent read the Codex documentation through context7), the Biome 2 and `pnpm` claims, and the `debug` interactive-script limitation.
- The judgments are a model's reading, not tested behavior. A "low" usefulness rating means a capable agent mostly does this unprompted, not that the skill is wrong.
- Line numbers refer to the files as of this date.

## Follow-up (2026-10-07)

The findings below stay as written on 2026-10-06; their skill names and line numbers refer to that state. Since then:

- **Design question**: superseded by [architecture decision record 0004](./documentation/architecture-decision-record/0004-skills-know-each-other-only-by-contract.md). Each skill is complete for its own job, calls others for theirs, and knows them only by contract, never restating another skill's rules, formats, or paths.
- **Priority 1, resolved**: dependency paragraphs list skill names only. The install fallback and the wait for `document` are gone because APM installs dependencies, and `check-skills.py` enforces the wording. The evals that only tested the fallback were removed or trimmed.
- **Priority 7, in part**: the legacy-folder line in `PROJECT-DOCUMENTS.md` is gone, and the abbreviation for architecture decision record is spelled out in `teach`, `test-first`, `improve-codebase-architecture`, and the decision record format.
- **Priority 9, in part**: `model-domain` was split. Its glossary and decision record formats moved to `document`, its conventions interview became the new `codify`, and the term discipline was renamed `delineate`. `refine` was renamed `interview`, and both `delineate` and `codify` use it for their questions, which removes the one-question-at-a-time inconsistency. `memorize` stays one skill: the scriptbook is one row of its routing table.
- **`memorize`**: triggers narrowed to standing rules, corrections to how something is done, and pipelines longer than one line, with a filter for one-off corrections; the personal memory index is read only when the harness has not loaded it; usage examples run on scratch input or as a dry run; evals 1, 2, 3, and 5 have fixtures, and a one-off-correction no-trigger eval was added.
- **`document`**: owns where every shared document lives and its format, with the changelog, glossary, and conventions moved under `documentation/`; other skills name documents by role. An obligation is defined as imposed from outside the code and outranks a code convention. The undefined `Task` and `Revision` fields were dropped, the record weights name their workflows, a merge renumbers a duplicate `CHG-NNNN`, and evals 7 and 8 have fixtures.
- **Still open from this pass**: `setup-ai-workspace`'s local tracker template restates `graphify`'s map path; `codify` reads its decline marker from `.agents/domain.md`, a file `setup-ai-workspace` owns; and the APM manifests of `setup-ai-tooling` and `monitor-ai-tooling` depend on each other.

## Answer to the design question: should skills reference other skills?

_Superseded by architecture decision record 0004; see the follow-up above._

Mostly no. Default to autonomous, and reference another skill only when it earns it.

Where references work:

- `document` has 14 callers and one protocol, and `refine` is a 26-line discipline that would otherwise be pasted into 7 skills. Both are worth sharing, provided the call is optional.

Where references hurt:

- **Hard stops.** 13 skills say "wait until the user installs `document`". A background subagent cannot wait, so `divide-and-conquer` breaks as soon as an implementer runs a skill that stops this way.
- **Install-fallback boilerplate.** "If a called skill is not installed" appears in 24 skills. It only matters for partial installs (the plugin ships everything together), and four evals exist only to test that paragraph.
- **Hollow orchestrators.** `iterate` (9 skills called) and `graphify` (10) are mostly choreography. `rebase` over `resolve-merge-conflicts`, and `sync-tree` over `rebase`, are the same pattern at a smaller scale.
- **Duplicated knowledge.** `guide` restates other skills' bodies, and `ROUTING.md` in `divide-and-conquer` copies the global delegation tier table. Copies drift.

Rule of thumb:

1. Default to autonomous: inline a short rule, or point to a sibling file, instead of invoking a skill.
2. Share a skill only when three or more callers need the same content and it is large enough that copies would drift.
3. A shared dependency has a stated fallback and never stops the run.
4. State the fallback once, in one place, not in every caller.
5. Assume every skill may run in a subagent with no user to ask.

## Priority problems

1. **The `document` hard stop** (13 skills). Make it a soft fallback.
2. **Interactive gates versus subagents.**
   - `test-first/SKILL.md:28` requires the user to confirm seams, which blocks `divide-and-conquer` implementers.
   - Records ownership is unclear: `test-first/SKILL.md:14` and `review-and-refactor/SKILL.md:137` write `work-in-progress.md` and the changelog regardless of caller.
   - `divide-and-conquer` step 9 lets one implementer subagent edit after review, while `review-and-refactor/SKILL.md:102,112` says the coordinating agent edits.
3. **`setup-git-guardrails` does not guard what it claims.** The agent reported these pass without a prompt: `git push -fu origin feat`, `(git push origin main)`, `sudo git push origin main`, `bash -c "git push origin main"`, `command git reset --hard`, `xargs git reset --hard`, `sleep 1 & git reset --hard`, `git checkout -f`, `git switch --discard-changes`, `git stash drop`, `git worktree remove --force`, `git reflog expire`. With no `jq` on the path the script exits 0 and guards nothing. The claim at `SKILL.md:86` that Codex has no per-command rules appears wrong (Codex has an execution-policy rules file).
4. **Unsafe instructions.**
   - `triage/SKILL.md:83` runs tests and commands on an external pull request, which executes untrusted contributor code.
   - `improve-skills/SKILL.md:69` tells the agent to use the credential helper's stored GitHub credential.
5. **Instructions the agent cannot carry out.**
   - `debug`: the interactive `read -p` script has no terminal where the user can answer.
   - `improve-codebase-architecture`: the report needs CDN scripts and an `open` command.
   - `improve-environment` and `improve-skills`: both reconstruct the session from logs the agent often cannot read.
6. **Stale or contradictory text.**
   - The removed compaction gate is still named in the `hand-off` description (`skills/productivity/hand-off/SKILL.md:3`), `skills/productivity/README.md`, `documentation/skills/productivity/hand-off.md`, `index.html` and `hand-off` eval 5.
   - The handoff format is split between `hand-off` and `take-over` and has drifted: `take-over/SKILL.md:19` expects a "what's next" section that `hand-off` never requires.
7. **Rule violations.**
   - The abbreviation for architecture decision record appears in prose in `test-first` (`SKILL.md:16`), `hand-off` (`:24`), `take-over` (`:14`), `teach` (`LEARNING-RECORD-FORMAT.md:5`), `model-domain` (format file lines 5, 15, 19, 29 and `SKILL.md:68`), `improve-codebase-architecture` (`SKILL.md:15, 26, 58, 72`, `HTML-REPORT.md:63`) and `setup-ai-workspace/domain.md:61`.
   - `teach/SKILL.md` has spaced hyphens used in place of em-dashes (lines 7, 14, 26, 29, 63, 72, 115, 123).
   - `write-for-agents/SKILL.md:6,12` and `ask-someone-else/agents/openai.yaml:3` use the abbreviation for document in prose.
   - Legacy handling, against the standing no-legacy-migration rule: `document/PROJECT-DOCUMENTS.md:36`, `setup-delegation-policy/TIER-AGENTS.md:121,125` and the matching `fast.md` rename in its eval 3.
8. **Personal configuration in shared skills.** GLM and Gemini model ids and the coding-plan block (`setup-delegation-policy/TIER-AGENTS.md:37-71`), "Token Monitor" (`monitor-ai-tooling`, `setup-ai-tooling/TOOLS.md:45`), Biome `lineWidth 160` and sorted keys (`setup-git-hooks/SKILL.md:96-122`), `metadata: delta-action: land` (`sync-tree`).
9. **Skills that fuse two jobs.** `document` (generic documentation plus the project-documents protocol), `memorize` (lesson routing plus the scriptbook), `model-domain` (glossary and architecture decision records plus `CONVENTIONS.md`, which is domain-agnostic).
10. **`guide` is the main upkeep liability.** About 70 lines duplicate other skills, and the 26-row catalogue paraphrases each skill's own description. The distinctive content (workflow choice, on-ramps, session-boundary tree) is small.

## Cross-cutting patterns

- Evals are generally strong: seeded traps, scratch repositories, numeric fixtures, routing no-triggers. The recurring weakness is evals that assert behavior the skill text never states (`research` 1, 3, 4; `refine` 5; `debug` 5; `memorize` 2, 3, 5; `ask-someone-else` 4; `hand-off` 1 and 5). Fix the skill, not the eval.
- No-trigger evals that only assert "skill not invoked" are trivially passable (`setup-*`, `work-in-tree` 9 and 10, `resolve-merge-conflicts` 7 and 8).
- Several steps assume capabilities the agent may lack: an interactive terminal, session logs, a browser, subagents without a fallback, knowing whether the user is away, stored credentials.
- "Completion:" and "Done when" lines restate defaults in `prioritize`, `improve-environment` and `monitor-ai-tooling`, while real gaps (subagent failure, missing web access, untrusted code) go unaddressed.
- Neighboring skills overlap and send users back and forth: `improve-environment` and `improve-skills` share a near-identical front half; `graphify`, `prioritize` and `specify` overlap on "decide what to do"; the `triage` brief and `taskify` tasks are two overlapping templates; `optimize-process` and `design-workflow` are separated only by evals.
- Term collisions: "frontier" (`specify` against `taskify` and `divide-and-conquer`), "refine" (`refine` against the `triage` role), "workflow" (`guide` against `design-workflow`).
- `unslop` conflicts with `AGENTS.md` on punctuation (it forbids parentheses and restricts colons), and about ten skills use the jargon it bans.
- Everything hardcodes "Call the Skill tool with ...", which is Claude Code specific although `openai.yaml` files ship.

## Verdict summary

| Skill | Bucket | Usefulness | Verdict |
| --- | --- | --- | --- |
| address-feedback | workflow | Medium | Keep, small fix |
| divide-and-conquer | workflow | Medium-high | Fix |
| implement | workflow | Medium | Trim |
| iterate | workflow | Medium-high | Trim |
| review-and-refactor | workflow | High | Trim and fix |
| specify | workflow | Medium | Keep, small fix |
| taskify | workflow | Medium-high | Keep |
| test-first | workflow | Low-medium | Trim and fix |
| graphify | shaping | Medium-high | Trim |
| prioritize | shaping | Medium | Trim |
| prototype | shaping | Medium-high | Fix |
| research | shaping | Low-medium | Fix |
| debug | upkeep | High | Fix |
| improve-codebase-architecture | upkeep | Medium | Trim |
| improve-environment | upkeep | High | Keep |
| improve-skills | upkeep | Medium (author) | Fix |
| monitor-ai-tooling | upkeep | Low-medium | Trim |
| triage | upkeep | Medium-high | Trim |
| setup-ai-tooling | setup | Medium-low | Trim |
| setup-ai-workspace | setup | Medium | Trim |
| setup-delegation-policy | setup | Medium | Fix |
| setup-git-guardrails | setup | High script, low prose | Fix |
| setup-git-hooks | setup | Medium | Fix |
| draft-merge-request | version-control | Medium-low | Trim |
| rebase | version-control | Medium | Keep, trim |
| resolve-merge-conflicts | version-control | Medium-low | Keep, fix |
| sync-tree | version-control | Medium | Keep, trim |
| work-in-tree | version-control | Low-medium | Merge into `sync-tree` |
| ask-someone-else | productivity | Medium | Fix |
| classify | productivity | Medium, narrow | Trim |
| design-workflow | productivity | Medium-low | Fix |
| guide | productivity | Medium router, high upkeep | Trim hard |
| hand-off | productivity | Medium | Fix |
| illustrate | productivity | Low-medium | Trim |
| optimize-process | productivity | Medium | Trim |
| publish-message | productivity | High | Keep |
| re-explain | productivity | Low-medium | Fix |
| take-over | productivity | Medium-high | Fix |
| teach | productivity | Medium-high | Trim |
| walk-through | productivity | High | Fix |
| design-modules | reference | Medium | Trim |
| document | reference | Protocol high, generic half low | Split or fix |
| memorize | reference | Medium-high | Fix |
| model-domain | reference | Medium | Fix |
| refine | reference | Medium | Fix |
| unslop | reference | Medium-high | Trim |
| write-for-agents | reference | High here | Fix |

## Workflow

### address-feedback

- Usefulness: medium. Adds the disposition vocabulary (Accept, Adjust, Already addressed, Decline, Blocked), the every-unit-accounted rule, two approval gates, and the rule that a reply does not authorize resolving a thread.
- Problems: step 6 (`SKILL.md:79-88`) restates publishing mechanics that `publish-message` owns and never calls it, against the repository's own rule to keep concerns in the owning skill. `.agents/issue-tracker.md` (`:20`) has no behavior when absent. The `[AI] ` prefix rule (`:72`) is unexplained. Step 4 hands to `implement`, which waits on `document`, so an untracked non-code review inherits the wait.
- Coupling: `implement` soft (non-code subjects skip it); `publish-message` and a tracker command-line tool used silently.
- Evals: good, including a contradictory pair of points, a scope-expansion point and a hidden dependency.
- Verdict: keep. Point step 6 at `publish-message`.

### divide-and-conquer

- Usefulness: medium-high. The approval gate on the routing table, the one-shot escalation rule, the integration-branch merge choreography and review-once are non-obvious.
- Problems:
  - Each implementer runs `implement`, which runs `test-first`, which requires user confirmation of seams (`test-first/SKILL.md:28`). A background subagent has no user, and nothing in the task graph agrees seams in advance.
  - `implement` and `document` say "wait until the user installs it", which a subagent cannot do.
  - A merger subagent per merge (`SKILL.md:42`) is expensive, and `ROUTING.md:27` itself calls merges Light.
  - Step 5 is convoluted (`:34`). Exploration notes are saved "outside the repository" with no path (`:26`).
  - Step 9 lets one implementer fix and commit refactors, while `review-and-refactor` says the coordinator edits and leaves changes uncommitted.
  - "Hands over to /setup-ai-workspace" (`:10`) is a missing-prerequisite pointer, not a hand-over.
  - `ROUTING.md:5-19` duplicates the global delegation tier table.
- Coupling: `document`, `implement`, `review-and-refactor` hard; `draft-merge-request`, `setup-ai-workspace` soft. It cannot stand alone cheaply.
- Evals: good, simulation based, heavy to run.
- Verdict: fix. Agree seams in the routing-table approval, drop the merger subagent for clean merges, settle who edits after review.

### implement

- Usefulness: medium. Mostly a pointer hub. The real content is the authorized-work gate, the records-ownership handoff and the final report contract.
- Problems: `:12` (mechanical conventions in formatter configuration) belongs in `model-domain`. `:18` commits to the current branch with no branch check, which can mean `main` or a protected branch. `:16` "test-first where possible" has no criteria, and depends on `webapp-testing`, which is not in the repository. "Full suite once at the end" is prescriptive without a reason. `:18` and `:20` duplicate records-ownership text that `iterate`, `divide-and-conquer` and `address-feedback` also carry.
- Coupling: `document` hard; `test-first`, `debug`, `webapp-testing` soft.
- Evals: good.
- Verdict: trim. Remove generic style advice, add a branch check, say when `test-first` is skipped.

### iterate

- Usefulness: medium-high. The only skill running the whole loop, with "implemented and checked is not accepted" and a pause-on-cost rule.
- Problems: the description ("Build a living application", "continue building an existing project in batches") can be hijacked by plain "build X" requests that belong to `implement`. Nine skills called (`SKILL.md:13`), so much of the body is orchestration. Step 2 is a mini-interview that overlaps `refine` and `research`. `MILESTONE-REVIEW.md` is a thin wrapper over `review-and-refactor`. "Agreed milestone" is never defined. `:79` duplicates `:11`. `ARTIFACTS.md:1` is titled "Working state". "Quote measured costs only" (`:77`) repeats `divide-and-conquer`.
- Coupling: `document`, `implement` hard; `refine`, `prioritize`, `research`, `model-domain`, `design-modules`, `divide-and-conquer`, `review-and-refactor` soft. Without `refine` and `implement` it is only a state-keeping routine.
- Evals: good.
- Verdict: trim. Reduce approach selection to a pointer, fold the milestone review into `review-and-refactor` with a caller flag.

### review-and-refactor

- Usefulness: high for the independent two-axis review, behavior-agreement freezing and "do not weaken tests to fit". Low-medium for the 12-smell baseline (`:64-77`), which an agent already knows.
- Problems: 1,901 words, the heaviest skill. The description is three sentences including mechanism, and collides with the built-in `code-review` and `simplify`. No fallback when subagents or continuation are unavailable (steps 4 and 6, `:82`). Review artifacts are saved "outside the repository" with no path (`:38`). Step 3 (`:56`) invokes `model-domain` mid-review, which is a surprise interview and file creation in a skill that may be report-only (`:18`). `:137` writes working state and the changelog unconditionally, so there can be two writers. The 400-word reviewer cap (`:86`) conflicts with "every documented violation". "Why two axes" (`:150-154`) restates the introduction.
- Coupling: `document` hard; `model-domain`, `publish-message` soft.
- Evals: good (seeded float-money patch, dirty trees, report-only runs).
- Verdict: trim and fix. Cut the smell list to a pointer, add a no-subagent fallback and a records-ownership clause, remove the `model-domain` side effect.

### specify

- Usefulness: medium. A synthesis checklist, the rule that unresolved proposals stay in the draft, the prototype-approval gate.
- Problems: "frontier" (`:18`) means open decisions here but ready tasks in `taskify` and `divide-and-conquer`. It never says where the canonical specification lives. `:14` fetches remote records with no tracker pointer. "Without demanding an exhaustive specification" (`:30`) is unverifiable. "Full changelog records" is undefined here. The description uses jargon.
- Coupling: `document` hard; `refine`, `model-domain`, `prototype` soft.
- Evals: good; eval 5 is somewhat trivially passable.
- Verdict: keep. Rename "frontier", add the tracker and path pointers.

### taskify

- Usefulness: medium-high. "A criterion needing another task's result moves there or becomes a blocker" (`:31`), expand-contract, the early exit for small batches, blockers-first publication.
- Problems: "sized for a fresh implementation context" (`:20`) is unverifiable. `:16` does not name `.agents/issue-tracker.md`. The publish procedure (`:37`) lacks tracker mechanics and does not call `publish-message`. A known open item from the previous handoff: eval 2 partials.
- Coupling: `document` hard; the hand-overs are offered only at the end.
- Evals: very good.
- Verdict: keep. Name the tracker file.

### test-first

- Usefulness: low-medium. Adds the tautology anti-pattern, the confirm-seams gate, the horizontal-slicing warning, "refactoring is not in the loop". `tests.md` and `mocking.md` are generic TypeScript advice.
- Problems: `SKILL.md:28` requires seam confirmation, which blocks autonomous and subagent runs and is heavy for a one-line fix. Nothing says to run the new test and confirm it fails for the right reason, yet evals 1 and 3 expect it (`:42`). `:14` writes working state regardless of caller, so parallel worktrees collide on `work-in-progress.md`. `:16` uses the abbreviation for architecture decision record. `tests.md` says "one logical assertion per test", which is dogma, and its jest example (`:32`) is misused. The description duplicates `implement` and "wants integration tests" over-triggers. It claims bug fixing but has no reproduce step.
- Coupling: `document` hard; `design-modules` soft.
- Evals: mixed; eval 1 is passable by any TDD-aware model.
- Verdict: trim and fix. Add a "see it fail" step, make seam confirmation conditional on interactive use, cut the generic reference files.

## Shaping

### graphify

- Usefulness: medium-high. A persistent multi-session decision map with claim, frontier and fog rules. About a third is tracker plumbing that `.agents/issue-tracker.md` already carries.
- Problems: the description is circular (it needs the user to say "graphify", yet eval 1 expects a trigger without the name) and overlaps `specify`, `prioritize` and `refine`. "Sized for one 100K-token agent session" (`:66`) cannot be measured. `:110` is ambiguous when several research tasks sit on the frontier. `:121` forces a stop after charting. Step 5 (`:120`) starts research subagents but never says who resolves those tasks or what happens when one fails. `:116` and `:129` call `refine` and `model-domain` for every refine task, including non-code domains. `:10` lists `/setup-ai-workspace` as a hand-over although it is a precondition, and `taskify` and `prioritize` (`:30`) are leaned on but not listed. Research findings go on a "throwaway research branch" (`:120`) while `research` says to save where the repository keeps notes.
- Coupling: `document`, `/setup-ai-workspace` hard; `refine`, `model-domain`, `research`, `prototype`, `illustrate` soft.
- Evals: strong.
- Verdict: trim. Cut remote-tracker detail, name its situation in the description, define how research tasks resolve.

### prioritize

- Usefulness: medium. The ownership split between backlog, work-in-progress and changelog, the "replacing active work needs explicit confirmation" guardrail, "approval is an Agreement".
- Problems: status vocabulary drifts (`:42` against `:46`). Five "Completion:" lines restate defaults. `:8` and `:58` couple it to `/iterate`. "Reconcile actual progress" (`:18`) has no method. "Break down an idea" overlaps `graphify`, `taskify`, `specify`.
- Coupling: `document` hard; `refine`, `research` soft.
- Evals: good.
- Verdict: trim. Drop the Completion lines and the `iterate`-specific text.

### prototype

- Usefulness: medium-high. The one-question rule, pure-module separation, the `?variant=` switcher, capture and cleanup rules.
- Problems: `SKILL.md:28`, `LOGIC.md:24,37` force a single HTML and JavaScript file. For a backend in another language that means reimplementing the logic, contradicting the claim that the module can be lifted into the real codebase (`LOGIC.md:33,58`). `UI.md` is Next and React specific. `UI.md:107` ("Fold the winner into the real code") reads as unconditional, while `SKILL.md` rule 6 requires acceptance and production checks first. `SKILL.md:8` ("including during specify") is unexplained. `:23` "if the user isn't reachable" is unknowable. Rule 4 ("no error handling") conflicts with "liftable".
- Coupling: `document` hard.
- Evals: good; eval 4 partly unverifiable.
- Verdict: fix. Add a "logic in the project's language" option, make the `UI.md` gate consistent.

### research

- Usefulness: low-medium. Three lines: use a background agent, prefer primary sources, write one Markdown file.
- Problems: the evals expect rules the text never states (checked version or date, unresolved items listed separately, no recommendations, exactly one file). No instruction for how the parent receives the result, what to do without web access, or a citation format. "Spin up a background agent" has no fallback. It disagrees with `graphify` on where findings go.
- Coupling: none, a leaf with callers (`graphify`, `prioritize`).
- Evals: seven cases, partly trivially passable.
- Verdict: fix, or accept it as a thin delegation wrapper and trim the evals.

## Upkeep

### debug

- Usefulness: high. Feedback-loop-first gate, "red-capable" completion, minimise step, falsifiable hypotheses, tagged logs, redaction rules, "no correct seam is itself the finding".
- Problems: the interactive human-in-the-loop script (`SKILL.md:35,65`, template `:3-4,15`) cannot be run by an agent with no terminal the user can answer in; eval 7 expects it to work. It needs a non-interactive variant (the user runs it and pastes the output). `:122` "Flag this for the next phase" points at a phase with no such step, and eval 5 expects `improve-codebase-architecture`, which the text never names. `:22` and `:37` are rhetoric ("Refuse to give up") that conflicts with `:55-56` "stop and say so". "Fast: seconds" (`:63`) contradicts the performance and non-deterministic branches. `:98` "if the user is AFK" is unknowable. `:140` requires a commit or pull request message though nothing says a commit is made. `:118` assumes a specification exists. The description ("broken/throwing/failing/slow") over-triggers on trivial errors, while the body says hard bugs, and overlaps `test-first`.
- Coupling: none (reads the glossary and decision records when present).
- Evals: strong.
- Verdict: fix. Repair the human-in-the-loop path and the dangling reference, narrow the description.

### improve-codebase-architecture

- Usefulness: medium. Value is the `design-modules` vocabulary, the deletion test, history hot-spot scoping and decision-record gating. The 133-line HTML specification is cosmetic.
- Problems: `SKILL.md:43` recommends collapse animations while `HTML-REPORT.md:110` says no interactivity. Two card formats (`SKILL.md:48-50` against `HTML-REPORT.md:61-62`). `HTML-REPORT.md:57` badges use dependency categories defined only in `design-modules/DEEPENING.md`. The report needs CDN scripts (Tailwind, Mermaid with `securityLevel: "loose"`), and its own documentation page (`documentation/skills/upkeep/improve-codebase-architecture.md:62`) records that this breaks when scripts are blocked. `:29` "spawn a sub-agent ... explore organically" is vague and does not pass the vocabulary. `open` is unusable headless. Uses the abbreviation for architecture decision record in prose.
- Coupling: `design-modules` hard in practice although declared soft; `model-domain`, `refine` soft.
- Evals: strong.
- Verdict: trim. Reduce `HTML-REPORT.md` to the card schema, use inline CSS and SVG.

### improve-environment

- Usefulness: high. Category table, "wire the existing check first", mechanical against judgment classification, "standards belong to review, not the implementer".
- Problems: no definition of "oversized" for `AGENTS.md` (`:33,40`), and judging a line a no-op (`:41`) needs behavioral evidence the agent mostly lacks. Session reconstruction from "local agent logs" (`:15`) has no format or location. Ping-pong with `improve-skills` (`:47,66` against `improve-skills:43`).
- Coupling: `memorize`, `write-for-agents`, `/improve-skills`, `/setup-git-hooks` soft. Stands alone cheaply.
- Evals: strong.
- Verdict: keep. Add a threshold for "oversized".

### improve-skills

- Usefulness: medium for the author, low for anyone else, because the target repository is hard-coded (`:7`). The privacy scrub, four-home sorting, duplicate-issue check and `.agents/feedbacks/` fallback are the non-obvious parts.
- Problems: `:69` says to try "every available" route and use the credential the git helper stores for `https://github.com` without printing it. That is credential scavenging and should be limited to credentials the user configured for this purpose. `:55` ("the skills version ... when it can be found") is rarely discoverable. Steps 1 to 3 depend on log access and duplicate `improve-environment`. `:73` runs a pending-feedback sweep on every run.
- Coupling: `memorize`, `unslop`, `/improve-environment` soft.
- Evals: good.
- Verdict: fix. Narrow the credential instruction, consider merging steps 1 to 3 with `improve-environment` into one retrospective.

### monitor-ai-tooling

- Usefulness: low-medium. Only matters to someone running RTK, CodeGraph and ast-grep. Real guardrails: do not sum RTK estimates into provider tokens, counter-reset handling, zero-denominator, "unknown is not unused", "bypass is a quality finding".
- Problems: tool names are hard-coded, so on other tooling it can only produce a gaps report. `SKILL.md:42` "Token Monitor" is never defined here. `MEASUREMENT.md:15` links a brittle `develop` branch page. `:20` assumes the command-line tool. No path for measuring when no source exists.
- Coupling: `.agents/ai-tooling.md` from `/setup-ai-tooling` soft.
- Evals: strong, the best-designed numeric fixtures in the group.
- Verdict: trim. Generalize the tool names or move them to a reference, define Token Monitor.

### triage

- Usefulness: medium-high. A state machine with exactly one category and one state, conflict handling, a hold template with a checkable "Waiting on", the out-of-scope knowledge base, durable-brief principles.
- Problems: `SKILL.md:83` runs relevant tests or commands on an external pull request, which executes untrusted contributor code with no sandbox or confirmation. The backlog-authority sentence repeats in `SKILL.md:25`, `:87` and `OUT-OF-SCOPE.md:78`. `AGENT-BRIEF.md` is 216 lines and its examples describe a different project. It overlaps `taskify` with a second task template and never says how they relate. "Search for an existing implementation by domain concept" (`:81`) has no bound.
- Coupling: `document` and `/setup-ai-workspace` hard (stops without the tracker files); `refine`, `model-domain` soft.
- Evals: strong (11 cases, a 10-file fixture).
- Verdict: trim. Add a safety note for untrusted code, dedupe the backlog sentence, shorten the examples.

## Setup

### setup-ai-tooling

- Usefulness: medium-low. "Inspect first, reuse working integrations, verify a known symbol" are real rules. The rest is a personal stack (CodeGraph, RTK, Context7, ast-grep, Serena) written as steps.
- Problems: step 4 (`SKILL.md:52-67`) asks for baseline counters, schema version and verified session recovery per client, which an agent cannot verify generically. `:65-66` ("compaction against exhausted plan allowance, recovery without a new model-generated handoff") is not actionable, and that last phrase leaned on the removed auto-handoff idea. `TOOLS.md:45` mentions "Token Monitor" undefined. `:10` and `:12` require `write-for-agents` for a setup that rarely edits instructions. `TOOLS.md:14-19,28-38` hard-code flags that were not verified.
- Coupling: `write-for-agents` soft and gratuitous; `monitor-ai-tooling` soft. Standalone already.
- Evals: nine cases; 8 and 9 trivial; all graded from a transcript only.
- Verdict: trim. Cut step 4 to record fields an agent can collect, drop the `write-for-agents` and recovery requirements.

### setup-ai-workspace

- Usefulness: medium. Scaffolds `.agents/issue-tracker.md`, `triage-roles.md`, `domain.md` and an `AGENTS.md` block. Its value depends on `specify`, `taskify`, `triage` and `graphify` reading them.
- Problems: `domain.md` (61 lines) mostly restates "read the glossary, use its terms, flag conflicts" and each project gets a drifting copy. `:68` skips the triage configuration when `triage` is not installed and offers no reconfigure path later. `:111` ("omit the reusable knowledge block when ... already points at the scriptbook") is vague. `:79` describes the `Conventions:` line three ways. Four 40 to 55 line tracker templates copy commands an agent knows, and `issue-tracker-github.md:52` has unverified sub-issue and dependency calls. The interview is long for a one-time scaffold. `domain.md:61` uses the abbreviation for architecture decision record.
- Coupling: `document` hard; the other setups, `model-domain`, `memorize` soft.
- Evals: ten cases, the strongest in the group.
- Verdict: trim. Shrink `domain.md`, collapse the tracker templates, decouple from `document`.

### setup-delegation-policy

- Usefulness: medium. The idempotent "replace the section in place, verify with search and diff" install is the real value.
- Problems: `TIER-AGENTS.md:37-71` hard-codes GLM and Gemini ids, "the user's coding plan" and a custom-alias block, none verified. `TIER-AGENTS.md:95` names `AskUserQuestion`, which is Claude only. `:121` and `:125` carry legacy-rename logic ("survives under an older name (`fast`)", "no legacy duplicate"). `SKILL.md:8` is a long justification for a four-line install. `POLICY.md:25` ("check model versions before every dispatch") and `:29` ("State which agent handled the work") add overhead the author's own global copy lacks. The step 4 report is long.
- Coupling: none.
- Evals: eight cases; 7 and 8 trivial; eval 3 enforces the legacy `fast.md` rename.
- Verdict: fix. Move harness ladders into optional per-harness files, remove the legacy rename.

### setup-git-guardrails

- Usefulness: high for the script (branch-aware and chain-aware), low for the prose.
- Problems: see "Priority problems" 3 for the confirmed-by-agent bypasses and the fail-open without `jq`. In addition: the pre-push fallback is referenced twice (`:86`, `:94`) but no script is given; it does not mention that `core.hooksPath` collides with `setup-git-hooks` (`.githooks`); the Claude settings block (`:39-57`) has no merge instruction while OpenCode has one (`:84`); the OpenCode `git push *` rule misses `git -C x push`; `jq` is never listed as a requirement. Eval 5 enforces the wrong Codex claim and no eval covers a missing `jq` or flag bundling.
- Coupling: `setup-git-hooks` for the pre-push fallback, unstated.
- Verdict: fix. Correct the Codex section (execution-policy rules), mention `jq`, close the bypasses or state the limits, supply the pre-push script.

### setup-git-hooks

- Usefulness: medium. The formatter-coverage mapping and the Husky stop are the value.
- Problems: it reads as "Biome plus lint-staged" and has no path for a Python or Go project (`:10-14`). `:96-122` bakes in personal style (`lineWidth` 160, `trailingComma: none`, `useSortedKeys: on`, which reorders keys in every JSON file including `package.json`). `:111` uses the Biome 1.x `organizeImports` key while `:28` says Biome 2.x, and the schema is `latest`. `:22` lists `bun.lockb`, which is stale. `:49` says `pnpm --if-present` is unsupported although `pnpm run --if-present` exists. `:45-46` runs a full build on every commit by default. `:24` offers to migrate off Husky with no procedure. `:156` commits without being asked. The Prettier block (`:132-142`) duplicates Biome defaults.
- Coupling: none.
- Evals: nine cases; 8 and 9 trivial.
- Verdict: fix. Neutral defaults, a correct Biome 2 configuration, state the Node scope, make the build opt-in and the commit conditional.

## Version control

### draft-merge-request

- Usefulness: medium-low. The Door and Blast radius vocabulary and the Before and After pair are non-obvious; the rest is "write a body".
- Problems: no heading or introduction (`:5-8`). Ignores an existing pull request template and the title. `:47` prefers a screenshot as evidence, but an agent cannot embed a local image through the command-line tools and the skill does not say how. No handling when no "before" exists, no source ticket (eval 6) or when the request must not be opened (eval 7). `:51` mixes "door" (binary) with "risk" (graded). `:31` is filler. The description collides with `illustrate` and `publish-message`.
- Coupling: `illustrate` soft.
- Evals: nine cases; 5, 6 and 7 assert behavior the skill never states and pass on default behavior; 4 tests only the fallback paragraph.
- Verdict: trim. Keep the template and definitions, add a rule for evidence an agent can attach and a missing-source rule.

### rebase

- Usefulness: medium. Pin, lease, backup reference and `range-diff` validation are above default. About 133 lines, batch directories, per-branch records and subagent fan-out are heavy for most rebases.
- Problems: the undo command at `SKILL.md:56` gives `git branch -f <name> refs/rebase-backup/<name>` "when it is not checked out", but a branch rebased in a skill-created worktree (`:23`) stays checked out there until `:81`, so git refuses. `--update-refs` (`:38`, `BRANCH.md:8`) needs git 2.38 and the version is never checked. The batch records mainly serve `RESUME.md`, which includes a "live subagent" check (`:5`) an agent cannot reliably perform. Single-branch work builds the full machinery.
- Coupling: `resolve-merge-conflicts` is soft on paper but hard in practice (`BRANCH.md:9`); `sync-tree` depends on this skill.
- Evals: eleven cases against a real scratch repository, among the most meaningful; case 9 hard to run reliably.
- Verdict: keep and trim. Fix the undo command, add a minimal single-branch path.

### resolve-merge-conflicts

- Usefulness: medium-low. 14 lines of mostly default practice. Non-obvious: never abort on your own, stop and ask when intent is uncertain, stage only reviewed paths, `GIT_EDITOR=true`.
- Problems: no heading or preamble. Missing the one real gotcha, that `--ours` and `--theirs` are swapped during a rebase, and modify and delete, rename, binary and lockfile conflicts. `:8` "check the pull requests, original issues" often cannot be done. `:10`'s sentence about a goal that names no outcome is cryptic. `:12` runs full checks at every stopped commit and `rebase` validates again, so checks run twice.
- Coupling: none.
- Evals: nine cases; 7 and 8 trivial.
- Verdict: keep and fix.

### sync-tree

- Usefulness: medium. Compare-and-swap `update-ref`, `--ff-only` from the target checkout, never touching a dirty target, diverged-history options.
- Problems: `:4-6` and `:17-18` add `metadata: delta-action: land` for a "Delta" product never defined in this repository. `:16-18`, `:25-28` and `:44-46` carry harness-specific text ("isolated child session", "request attachment or direct-edit authorization") that an agent cannot verify or reach in Claude Code. `:79-85` delegates the diverged case to `rebase` and then forbids its push step. `:99-100` requires the user to uncheck the target. No cleanup of the source worktree after landing.
- Coupling: `rebase` soft on paper, heavy in practice; implicit coupling to `work-in-tree`'s handoff (`:40`).
- Evals: twelve cases with a real scratch script, strong.
- Verdict: keep and trim. Remove the Delta metadata and harness-specific text, or merge with `work-in-tree`.

### work-in-tree

- Usefulness: low-medium. `git worktree add -b` is trivial and Claude Code has built-in `EnterWorktree` and `isolation: worktree`, which the skill ignores. What it adds: "a linked worktree on the target's shared ref is not isolation", the dirty-checkout refusal, unique-name and existing-path checks, the handoff fields.
- Problems: `:68-71` ("ask the user to attach the new worktree or authorize direct edits") applies to another harness. `:49` is vague. Step 4's handoff is the only link to `sync-tree`. The branch it creates (`worktree/<task-name>`) has no owner for deletion. The description over-triggers on any "don't touch my checkout". `:12` prints `<name>` as a literal placeholder.
- Coupling: hands over to `sync-tree` (soft).
- Evals: ten cases; strong on refusals; 9 and 10 trivial.
- Verdict: merge into `sync-tree` as one worktree skill, or trim hard and mention the native tools.

## Productivity

### ask-someone-else

- Usefulness: medium. "Grill the send, not the subject" (`:8`), one recipient per document (`:10`), a fixed template, one idea per question.
- Problems: the template needs a deadline and "how answers will be used" (`:27-36`) but steps 1 and 2 never ask for them, so the agent invents them. No intake step for returned answers although `guide` says "then bring the answers into refinement". "Fill out together over a meeting" (`:6`) has no template variant. Eval 4 expects a pointer to `publish-message` the text never states. `agents/openai.yaml:3` uses the abbreviation for document.
- Coupling: none; fully standalone.
- Evals: good.
- Verdict: fix. Add a deadline and use question, add a "bring answers back" line.

### classify

- Usefulness: medium, narrow; only valuable if classifier.dev is wanted. Real value: the privacy gate (`:11`), "bias toward keeping" thresholds (`:67`), curl over stdin (`:38`).
- Problems: hard-coded quotas, limits and tier behavior (`:36-49`) go stale and cannot be verified offline. `:71` is maintainer chatter ("compare with upstream skill.md"). `:9` says classify before reading, then use own judgment for a handful, with no threshold. Dense paragraphs (`:36`, `:51`). "Or when the user requests an API verdict" is vague.
- Coupling: hard on a third-party network service with a stated local fallback.
- Evals: strong.
- Verdict: trim. Drop the quota tables in favor of the live reference, delete `:71`.

### design-workflow

- Usefulness: medium-low. A thin wrapper around `refine` plus vocabulary (trigger, checkpoint, push right, brief) and a "done" bar. Push-right and brief are good ideas.
- Problems: the `workflows/*.md` format is never specified, so "implementable" rests on taste. The description ("recurring loops in their work") is narrower than the body (`:13` reaches career, week, morning). It uses the current directory as workspace and can drop `NOTES.md` and `workflows/` into a code repository with no safety check. "Nothing is done while a question remains" (`:28`) has no escape for an interview that never converges. It overlaps `optimize-process`, separated only by evals 6 and 7, and "workflow" collides with `guide`.
- Coupling: `refine` soft (fallback at `:9`, tested in eval 4).
- Evals: good.
- Verdict: fix. Add a minimal `workflows/<name>.md` skeleton and a "not in a code repository without asking" guard.

### guide

- Usefulness: medium as a router, low-medium for upkeep cost. The distinctive part is the session-boundary decision tree (`:62-68`, `PHASE-BOUNDARIES.md`).
- Problems: about 70 lines duplicate content owned by other skills (planned development `:18-25`, just-in-time `:27-35`); the claims were accurate when spot-checked. Lines 76 to 101 paraphrase each skill's own description. The two boundary tables are near duplicates (`:62-68`, `PHASE-BOUNDARIES.md:7-38`). The "about 150k tokens smart zone" is an unexplained number. `/clear` and `/compact` are user-only commands. `:8` and `:39` repeat one sentence. `:70` ("Live working state does not replace the session handoff") is vague. `AGENTS.md` forces re-reading it on every skill change, so any rename leaves silent stale routes.
- Coupling: names essentially every skill, all soft.
- Evals: good and grounded.
- Verdict: trim hard. Keep the three-row workflow choice, the on-ramps table and the boundary tree. Delete the catalogue and the restated workflow bodies.

### hand-off

- Usefulness: medium. Mostly default behavior. Non-obvious: timestamped never-overwrite file, supersedes line, the local-or-shared gitignore decision, redaction, validating suggested skills, reference rather than copy.
- Problems: the description ("Compact the current conversation ...") collides with `/compact`, and `:3` still says "or when a compaction gate blocks until a fresh handoff exists", which referred to the removed `setup-auto-handoff`. The same text remains in `skills/productivity/README.md`, `documentation/skills/productivity/hand-off.md`, `index.html` and eval 5. No required sections, although eval 1 expects decisions and a next step and `take-over:19` expects "what's next". Asking "gitignore or commit?" mid-run is friction. No failure handling. `:24` uses the abbreviation for architecture decision record.
- Coupling: `take-over` consumes its output (the format contract is split across two skills).
- Evals: good; eval 5 now tests a dead feature.
- Verdict: fix. Remove the gate clause everywhere, define required sections (state, decisions, what's next, open questions, suggested skills, supersedes).
- Status (2026-10-07): addressed together with `take-over`, so the line numbers above no longer match. Both skills now ship an identical `HANDOFF-FORMAT.md` (location, threads, a fixed template, rules) that `scripts/check-skills.py` keeps identical. The gate clause is gone everywhere, the description says "Write" instead of "Compact", and the abbreviation is spelled out. Changed from the verdict: suggested skills are dropped rather than required, so a handoff works in any harness. Kept on purpose: the one-time local-or-shared question. A merge into a single `relay` skill was considered and rejected: the two run in different sessions, and guessing the direction is less reliable than two explicit names.

### illustrate

- Usefulness: low-medium. The shape-selection table (`:15-24`), the smallest-view rule, and labeling proposed against current.
- Problems: the description ("Explain the current topic visually") is broad and overlaps `re-explain`, `prototype`, `draft-merge-request` and the `dataviz` skill. `HTML.md:5` ("a writable artifact location that follows the workspace's conventions") is unverifiable. `HTML.md:9-10` assume a browser or open tool exists. Mermaid against text fallback depends on knowing whether the destination renders. The generic delivery paragraph (`:46-52`) restates defaults.
- Coupling: none outbound; `graphify` and `draft-merge-request` call it.
- Evals: good.
- Verdict: trim.

### optimize-process

- Usefulness: medium. The guardrails: find why a step exists before removing it, count agent work as runtime plus human setup and review, no invented percentages, "say it is already sound".
- Problems: five headed sections of near-generic process analysis. "Ask for the few missing facts" has no stop condition if the user has no real cycle to trace. No explicit "Use when" sentence. Overlaps `design-workflow` and `debug` (performance).
- Coupling: none.
- Evals: strong.
- Verdict: trim. Collapse "Find friction" and "Design" (`:14-20`).

### publish-message

- Usefulness: high. Approval of exact text and destination, audience and language fitting, local against published honesty (`:35-37`), read-back verification, head-revision revalidation for inline suggestions.
- Problems: `:12` and step 2 both restate how `.agents/issue-tracker.md` is resolved. The style rules (`:52-56`) duplicate `unslop`, called at `:57`. `:54` bans abbreviations in messages to others, in tension with "unless it is what the codebase calls it" and chat norms. Step 5 read-back is impossible on some services (handled by reporting the limit).
- Coupling: `unslop` soft; `.agents/issue-tracker.md` soft.
- Evals: excellent.
- Verdict: keep. Trim the redundant tracker restatement and the prose rules.

### re-explain

- Usefulness: low-medium. Any agent re-explains when told "I didn't get it". It adds reply in the user's language, a plain-English controlled vocabulary, glossary vocabulary, and the ask-first rule on language ambiguity.
- Problems: written in the user's voice ("Re-explain that ... I have been writing in", `:6`) rather than as agent instructions, and "that" has no referent. The English controlled vocabulary is imposed on every English answer, even for experts. "Unsure" is undefined. Nothing says to take a new angle after a repeated failure, although eval 6 requires it.
- Coupling: `GLOSSARY.md` and `GLOSSARY-MAP.md` soft.
- Evals: good for six lines.
- Verdict: fix. Rewrite as agent-voice instructions in 5 to 8 lines and add the "new angle, not a rewording" rule.

### take-over

- Usefulness: medium-high for its size. Newest by filename, read the whole handoff, follow the chain only when needed, resolve artifacts as primary sources, confirm the brief, never edit handoff files.
- Problems: step 2 (`:12`) flags assumptions "while reading" but verification only happens in step 4 (`:14`), so the order is wrong. Step 5 "verify their current names" (`:15`) does not say against what. "Newest wins" breaks with `guide`'s forked side-task handoff (`guide:66`), with no disambiguation. `:19` references a "what's next" section `hand-off` does not require. `:14` uses the abbreviation for architecture decision record.
- Coupling: `hand-off` hard (it consumes that format), with a fallback only for an empty directory.
- Evals: strong.
- Verdict: fix. Reorder steps 2 and 4, define the fork case, align section names with `hand-off`.
- Status (2026-10-07): addressed with `hand-off` (see its status line). Claims marked assumed or unmarked are checked against the Sources before the brief; separate threads (a fork or unrelated work) are named and the user picks one, unless a path or topic is passed; the skill-name step is gone with the suggested skills. Kept on purpose: the step order, now explicit that step 3 checks what step 2 noted.

### teach

- Usefulness: medium-high when used. The multi-session workspace model, retrieval and spacing guidance, equal-length quiz options, "never trust parametric knowledge".
- Problems: heavy philosophy prose ("Think Tufte", `:50`; `:21-44`) restates pedagogy defaults. Lessons must be short and quick (`:52`) yet carry citations, a primary source, links and a follow-up reminder (`:54-60`). "Never trust your parametric knowledge" (`:29`) conflicts with "default to attempt to answer" (`:115`). Each lesson needs polished HTML with asset reuse and a shared stylesheet, with no size budget. "Find high-reputation communities" (`:119`) is an unverifiable web task. Spacing and interleaving need due dates the record format lacks. Spaced hyphens stand in for em-dashes (`:7, 14, 26, 29, 63, 72, 115, 123`). `LEARNING-RECORD-FORMAT.md:5` uses the abbreviation for architecture decision record.
- Coupling: no skill calls; hard on web search for `RESOURCES.md`, with no fallback.
- Evals: very good.
- Verdict: trim. Cut the philosophy, resolve the lesson-size tension, fix the dashes and abbreviation.

### walk-through

- Usefulness: high. The tested `template.sh` library (stage progress, hidden secret entry, idempotent `.env` upsert, secret and variable writes, WSL-aware URL open) is non-trivial to rebuild, and the staged-scoping gate is a good guardrail.
- Problems: the title is `# Wizard` (`:6`) while the skill is `walk-through`. `template.sh` `write_env` writes secrets to `.env` with no check that `.env` is gitignored and no `chmod 600`, and the verify step (`:41-44`) never checks it. `finish` always says "Setup complete" and the example stage is Stripe, awkward for migrations and cutovers the skill claims to support (`:8`, `:20`). `:43` the trace check applies only to CI-secret wizards. Bash only, no guidance when `gh` or `tput` are missing beyond SKIPPED.
- Coupling: none outbound; `memorize:21` calls it.
- Evals: strong.
- Verdict: fix. Add the gitignore and permissions check, use one term throughout.

## Reference

### design-modules

- Usefulness: medium. The ideas are known; the value is the enforced vocabulary and "one adapter is a hypothetical seam".
- Problems: the description invites a design session while `test-first:32` calls it "a reference to consult, not a session to run". Sediment: "adapter" defined twice (`:18`, `:24`), the "boundary" ban at `:12`, `:22`, `:109`, the "interface is not the TypeScript keyword" point at `:16` and `:108`, "Rejected framings" (`:105-109`) is meta commentary, the seam-count rule duplicated at `SKILL.md:65` and `DEEPENING.md:29`, internal seams at `:62` and `:30`. The `processOrder` examples have empty bodies. `DEEPENING.md:34` says delete old tests with no approval gate. `DESIGN-IT-TWICE.md:21` needs three or more parallel subagents with no fallback. "Minimize" and "Maximise" spellings differ (`:25`).
- Coupling: none; `improve-codebase-architecture` restates its vocabulary list.
- Evals: only eval 1 has a fixture; 2 to 4 are passable by any agent that knows the topic; eval 6 expects a refusal to explore, contradicting the description.
- Verdict: trim about a quarter. Borderline as a separate skill with three callers; the callers could read its sibling files directly.

### document

- Usefulness: `PROJECT-DOCUMENTS.md` high (a real protocol: layout, authorization terms, changelog format). The generic half of `SKILL.md` (`:12-19`) is low.
- Problems: two skills fused. "Write and maintain project documentation ... README, API reference, runbook" pulls the heavy protocol into plain README work (`write-for-agents` eval 7 routes READMEs here), and it will over-trigger on any documentation request. `PROJECT-DOCUMENTS.md:36` is legacy-migration text. Terms are used before they are defined ("Agreement" at `:35`, defined at `:72`). "Full" against "planned workflow" (`:77`) names no workflow. `Task` and `Revision` fields are unspecified (`:70`). "Allocate the next free CHG-NNNN" (`:70`) has no collision rule for branches or teams. "Review evidence" (`:82-84`) is review policy in a documents skill. `:31` leans on `GLOSSARY.md` and `:40` on `.agents/issue-tracker.md` with no stated coupling. The Calls line (`:10`) is repeated at `:19`. The stated reason for the wait rule ("this skill's rules use its terms") is thin; `memorize` uses only the phrase "shared project documents".
- Coupling: `write-for-agents` soft; for callers it is hard in practice (13 skills say wait).
- Evals: the strongest of the group; only evals 1 and 8 touch the generic half.
- Verdict: split or fix. Keep the project-documents protocol as the shared skill and name it for what it is, drop the generic steps or move them to `write-for-agents`, delete `:36`, make the wait a soft fallback.

### memorize

- Usefulness: medium-high. The routing table (a project lesson goes to the project, not the harness memory) and the scriptbook lookup are non-default.
- Problems: the description (about 90 words) over-triggers: "the moment the user corrects you" turns every "no, make the button blue" into a filing event, and "before writing any script or multi-step shell pipeline" triggers on every `grep | sort`. It fuses lesson routing and the scriptbook. `:10` makes `document` a hard dependency on a thin reason. `:29` "read the personal memory index" duplicates the harness, which loads `MEMORY.md`. `:50` and every "Call the Skill tool with" are Claude Code specific. `SCRIPTS.md:43` requires auditing the whole scriptbook on every save, and `SCRIPTS.md:35` "run that example once before indexing" runs an unreviewed script. No guidance on when a lesson is too trivial to file.
- Coupling: `document` hard-wait; `model-domain`, `walk-through`, `write-for-agents` soft; hands over to `/improve-skills`.
- Evals: evals 2 and 5 have `files: []` so conditional expectations are unverifiable; eval 3 expects an existing glossary read first with none supplied; eval 4 passes with either of two homes.
- Verdict: fix. Narrow the description to explicit statements ("always", "never", "remember"), drop the blanket correction and pipeline triggers, remove the `document` hard stop.

### model-domain

- Usefulness: medium. The glossary and decision-record discipline (no implementation details, all-three-criteria gate, `_Avoid_` and `_Why_`) is non-default. "Challenge, sharpen, cross-reference" (`:44-58`) is what a good agent does when told to.
- Problems: three unrelated jobs. `CONVENTIONS.md` is domain-agnostic (`CONVENTIONS-FORMAT.md:5`) yet lives in a skill named for the domain. "Discussing codebase terminology" over-triggers on any naming chat. The three-criteria gate is duplicated verbatim (`SKILL.md:66-74`, `ARCHITECTURE-DECISION-RECORD-FORMAT.md:29-37`). The single and multi-context layout is duplicated (`SKILL.md:12-38`, `GLOSSARY-FORMAT.md:38-66`). Per-context decision-record numbering (`SKILL.md:34`) is unspecified in the format file (`:27`). Interview mode is one question at a time (`CONVENTIONS-FORMAT.md:30`) while `refine` asks the whole frontier, and `triage:84` calls both with no reconciliation. `CONVENTIONS-FORMAT.md:25-26` are two stacked sentences. `:64` says to skip recording the decline when `.agents/domain.md` is absent, so the user is asked again every run. An architecture decision record and a changelog "Agreement" (`PROJECT-DOCUMENTS.md:35`) are never disambiguated. Uses the abbreviation for architecture decision record in prose (`ARCHITECTURE-DECISION-RECORD-FORMAT.md:5,15,19,29`, `SKILL.md:68`).
- Coupling: `document` soft; the implicit `.agents/domain.md` owned by `setup-ai-workspace`. No Calls line.
- Evals: strong (eleven, well fixtured); eval 4's "says which test fails" is garbled.
- Verdict: fix. Split `CONVENTIONS` out or rename the skill, dedupe the decision-record and layout text, spell out the term.

### refine

- Usefulness: medium. Frontier-batching of numbered questions with a recommended answer is distinctive; "grill me" in general a model does already.
- Problems: the word collides with `triage`'s "refine" role (`triage:3,84`) and everyday "refine this plan". "Stress-test their thinking" overlaps `specify`, `design-workflow`, `ask-someone-else`. No cap on frontier size, yet eval 5 expects a "short set" and a "split the scope" warning the skill never states. `:24` "delegating exploration when available" and "unsettled prerequisite" are fuzzy. `:26` "user confirms the shared understanding" has no criterion. No heading. Decorative emojis in the template (`:11`).
- Coupling: none; seven callers use it as a protocol.
- Evals: good; eval 5 tests unspecified behavior.
- Verdict: fix. Add a frontier size bound and a split rule, or drop those eval expectations, consider a more distinctive name.

### unslop

- Usefulness: medium-high. The concrete banned-word and pattern lists work as a checklist models do not apply on their own. About a third (hedging, chatbot phrases, sycophancy, filler) is a no-op for a modern agent.
- Problems: "before a final report" and "before writing prose into a repository" make it fire on nearly every turn, yet only `publish-message` and `improve-skills` call it. No stop rule (`:14` can loop). `:34` forbids parentheses and restricts colons while `AGENTS.md` endorses comma, colon, period and parentheses. `:55`'s banned jargon (harness, primitive, surface, scaffolding, gold-plating, north star, ratchet) appears in about ten `SKILL.md` files, and `write-for-agents` ("ladder", "levers", "legwork", "coin-flip", "sediment", "rung") is the mannered prose `:64` bans. `:26` "features" is ambiguous. "Any language" is asserted but the list is English.
- Coupling: none.
- Evals: strong, possibly the best-built set of the seven.
- Verdict: trim. Cut the no-op patterns, reconcile the punctuation rules with `AGENTS.md`, narrow the trigger to text meant for others.
- Status (2026-10-07): partly addressed, so the line numbers above no longer match. Done: the trigger covers only prose other people will read, the em dash rule allows the punctuation the sentence wants (parentheses and colons included) and the skill stays universal by deferring to a project's own writing rules, the self-audit is one pass, and "features" is marked as the verb. Kept on purpose: the chatbot, sycophancy, hedging, and filler patterns (cheap, and weaker models still produce them) and the explicit calls in `publish-message` and `improve-skills`. Still open: the metaphorical "surface" in `design-modules` and `triage`.

### write-for-agents

- Usefulness: high for this repository's idiom (pointer wording, completion criteria, disclosure, no-op pruning, negation). Medium generally. The best content is `:12` (pointer wording decides reach), `:49` (hiding steps only works across a real context boundary), `:78-80` (environment as source of truth).
- Problems: it coins about 20 terms (context pointer, two loads, ladder, co-location, sprawl, sediment, legwork, post-completion steps, leading word) while `:63` says made-up words cost definition tokens. `:72` ("Assume every document is carrying restatements ... Go find them") mandates edits with no evidence test. `:80` "settle it by running the document" is not something a normal run can do. Many claims (negation drag, completion-pull) are unsupported. `SKILL-MECHANICS.md:3` promises frontmatter and covers only invocation flags: no name rules, length limits or template. `AGENTS.md` demands reading the official best-practices page, which the skill does not cite. `:74` preaches positive phrasing while sibling skills are full of "do not". Under-triggers on subagent briefs and prompts. The listing copy still says `CLAUDE.md`, so the installed link is stale relative to this file. `SKILL.md:6,12` use the abbreviation for document.
- Coupling: none; four soft callers.
- Evals: good; eval 7 asserts `document` shapes a README, cementing the over-trigger.
- Verdict: fix. Add real frontmatter mechanics or point to the official page, prune coined terms, remove "Go find them", spell out "document".
- Status (2026-10-07): addressed in `52e9cf3` and the commit that adds this status line, so the line numbers above no longer match. Done: the official page is the frontmatter source, decorative metaphors are cut (defined terms kept), "Go find them" became a conditional test, behavioral claims carry a reason instead of being stated as fact, "document" is spelled out, and the stale "sediment" expectation in eval 3 is updated. Kept on purpose: eval 7's routing expectation (READMEs are in `document`'s scope). Still open: the trigger expansion for agent instructions and delegation briefs, and a behavioral evaluation of the rewrite. Reasoning in `.agents/handoffs/2026-10-07-0052-write-for-agents-tightening.md`.

## Suggested order of work

1. Remove the stale compaction-gate text (`hand-off` description, `skills/productivity/README.md`, the `hand-off` documentation page, `index.html`, `hand-off` eval 5) and regenerate the map. This is a leftover of the `setup-auto-handoff` removal.
2. Replace the `document` hard stop with a soft fallback, and state the install-fallback rule once instead of in 24 skills.
3. Fix `setup-git-guardrails`, `triage` (untrusted code) and `improve-skills` (credentials).
4. Slim `guide`.
5. Resolve the interactive-gate and records-ownership conflicts between `test-first`, `review-and-refactor`, `implement` and `divide-and-conquer`.
6. Sweep the rule violations (abbreviations, spaced hyphens, legacy text).
7. Split or rename the fused skills (`document`, `memorize`, `model-domain`); merge `work-in-tree` into `sync-tree`.

## Name conflicts with other skill collections

Many skill names are generic (`debug`, `document`, `implement`, `research`, `triage`, `rebase`, `prioritize`) and clash with skills from other collections.

Where the clash happens:

- **Claude Code plugin:** no clash. Plugin skills are namespaced as `plugin-name:skill`.
- **`scripts/link-skills.sh`, skills.sh and APM:** clash. `~/.claude/skills`, `~/.agents/skills` and project skill directories are flat, so two skills with the same name collide and one wins or overwrites the other.

### Potential solution: a `d4s-` prefix

Prefix every skill with `d4s-`, a numeronym of the owner handle (**D**yrit**s**: four letters between the D and the s, built like `i18n`). Examples: `d4s-debug`, `d4s-implement`, `d4s-triage`.

Why this prefix:

- It is tied to the owner, not to a bucket, so a skill moving between buckets keeps its name.
- It is short, and it is unlikely to clash with another collection.
- Digits and hyphens are valid in skill names (lowercase letters, digits, hyphens, at most 64 characters). A colon is reserved for plugin namespacing, so the separator is a hyphen.

Constraints:

- **The name must match the folder.** The Agent Skills standard requires the `name` in `SKILL.md` frontmatter to equal the parent directory name. Prefixing only the installed name (a renamed symlink from `link-skills.sh`) breaks this at the destination, so it is not an option. The folder and the `name` both change.
- **Prefix every skill, not only the clashing ones.** A mixed set hides which skills are this collection's.
- **Keep upstream names in the provenance notes**, so each skill still maps back to the original it forks.
- The prefix is not needed for the Claude Code plugin route alone, since the plugin name already namespaces it. It pays off on the skills.sh, APM and symlink routes.

Blast radius of the rename:

- The skill folder and the `name` in `SKILL.md`.
- The documentation page at `documentation/skills/<bucket>/<skill-name>.md` and the `evals.json` path, which both follow the folder.
- `.claude-plugin/plugin.json`, the top-level `README.md` and the bucket `README.md` entries.
- `scripts/skill-graph/flow.json` and the generated `index.html` (run `python3 scripts/build-skill-graph.py`).
- `guide`, and every cross-reference between skills, including the "Calls" lines and eval fixtures.
- The generated `apm.yml` manifests (run `python3 .agents/scripts/generate-skill-manifests.py`, do not edit them by hand) and the root `marketplace.json`.
- The install commands in `documentation/maintenance/standard-installation-wording.md`, then re-run `scripts/link-skills.sh`.

Verification: run `scripts/check-skills.py` and `claude plugin validate . --strict`.

Not verified: the name-equals-folder rule is stated from knowledge of the Agent Skills standard and has not been checked against the current specification or against how `scripts/check-skills.py` enforces it. Check both before starting the rename.
