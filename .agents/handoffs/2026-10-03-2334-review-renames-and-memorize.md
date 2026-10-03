# Review, renames, buckets, and memorize

Supersedes: [2026-10-03-2055-shared-workflows-0-2-0.md](./2026-10-03-2055-shared-workflows-0-2-0.md). Its installed-copy warning still applies and has grown (see below); its paths and skill names are now historical.

## Resume here

The user asked for a review of the day's work, then approved fixes, renames, a bucket reorganization, and a new `memorize` skill. Everything below was implemented in one working tree together with the user's own earlier in-flight renames, then committed and pushed to `origin/main` as requested. Check Git for the actual commit and push result; this handoff was written before them.

No version bump was requested; the plugin stays at `0.2.0`.

## Authoritative artifacts

- [Shared project documents](../../skills/reference/document/PROJECT-DOCUMENTS.md): now opens with the four terms every caller relies on (authorized, obligation, lazy, pointer) and defines full and light changelog records.
- [README](../../README.md): bucket layout, rename table ("Intentional workflow drift"), separately installed skills.
- [Repository instructions](../../CLAUDE.md): bucket definitions, including the new `version-control/` and the sharpened `reference/` rule, plus the scriptbook pointer.
- [Provenance audit](../../documentation/research/2026-10-03-retained-skill-provenance.md): current names with their earlier ones.
- [guide](../../skills/getting-started/guide/SKILL.md): routing, including the decomposition border table.
- [memorize](../../skills/reference/memorize/SKILL.md) and its [SCRIPTS.md](../../skills/reference/memorize/SCRIPTS.md).
- [Script index](../scripts/INDEX.md) and [update-references.py](../scripts/update-references.py).

Read those rather than reconstructing decisions from this summary.

## Decisions made this session

- **No legacy handling.** Skills are independent, not migration tools: every mention of `.refinement/`, old `backlog/` folders, and historical inputs was removed. Tracker labels moved from `wayfinder:` to `graphify:`; old upstream maps are not read.
- **Single source for document rules.** Callers say "call document; its terms and rules apply" instead of restating authorization, obligation, and publication rules. Prohibitions were rewritten as positive instructions; per-skill "if unavailable" fallbacks became one sentence.
- **Changelog weights.** Same format for both workflows: full records in the planned workflow and team use; light records (Summary, References, Validation; Agreement only for consequential decisions) in `iterate`.
- **`document`** lost its generic document-type checklists; it is now the project-document contract plus four writing habits.
- **Names read as commands.** Final renames: `what-is-next` → `guide`, `documentation` → `document`, `writing-for-agents` → `write-for-agents`, `code-review-and-refactor` → `review-and-refactor`, `to-pull-request` → `draft-merge-request` (the user's renames), then `divide-and-conquer` → `prioritize`, `test-driven-development` → `test-first`, `wizard` → `walk-through` (its artifact is still called a wizard), `codebase-design` → `design-modules`, `domain-modeling` → `model-domain`, `scriptbook` absorbed into `memorize`.
- **Decomposition border:** `graphify` when what to build is undecided and needs several sessions; `prioritize` when what to build is known and the question is which outcome first (it keeps the rest in the backlog); `taskify` for splitting agreed behavior; `refine` for one decision.
- **Buckets.** `reference/` holds only disciplines other skills call that produce no result of their own. New `version-control/` holds branch and merge request skills. `design-workflow`, `walk-through`, and `classify` moved to `productivity/`. Empty leftover folders of retired skills were deleted.
- **`update-references.py`** (renamed from `propose-reference-updates.py`) now emits a `git apply` diff by default, keeps Codex `--format apply-patch`, and adds `--apply`, `--search`, and `--exclude`.

## Verification and its limits

Passing at handoff: `npm run check-skills`, `npm run test-skills-check`, `npm run test-scriptbook-helpers` (seven tests, including the new diff, search, and apply cases), `npm run check-plugin-version`, `claude plugin validate . --strict`, `git diff --check`. `check-skills` now also rejects Skill-tool calls to every retired name, including today's.

These are structural checks. No skill was run: the rewritten `iterate`, `prioritize`, `document`, and new `memorize` have no runtime evidence. Evaluations were explicitly deferred by the user.

Observed failure worth keeping: during this session the agent never consulted `scriptbook` while repeatedly writing inline Python for bulk reference edits, although the skill was listed and a matching project script existed. That is the evidence behind the pending `memorize` fixes below.

## Pending, by owner

User, after this push:

- Refresh installed copies. Moves changed paths, so re-run `scripts/link-skills.sh`; it never deletes, so also remove installed entries for every retired name (`what-is-next`, `documentation`, `writing-for-agents`, `code-review-and-refactor`, `to-pull-request`, `divide-and-conquer`, `test-driven-development`, `wizard`, `codebase-design`, `domain-modeling`, `scriptbook`). `~/.agents/skills` held real directories, not symlinks; preserve their contents before the script replaces them. This was the user's choice to do themselves.

Proposed, deferred by the user ("later, maybe"):

- `memorize` trigger fixes: rewrite the description to lead with recall and name concrete actions (inline snippets, bulk find-and-replace); inline the one-command index lookup in `SKILL.md`; extend the Pointers step to global instruction files (`~/.claude/CLAUDE.md`, `~/.agents/AGENTS.md`), which currently carry no scriptbook pointer. Writing global files needs the user to see the exact line first.
- Optional `PreToolUse` reminder hook for inline scripts, as a setup skill or a `setup-ai-tooling` step. Codex support unverified.

Proposed, not yet answered:

- `prioritize` branch for many small independent items: keep them unmerged, rank by list order, allow one approval for a bundle, skip the interview, no changelog entry for ranking.
- A "README at boundaries, not in every folder" rule in `document`'s principles.
- Whether `memorize` should be promoted to the plugin (it would need a documentation page).

Later: bounded `skill-creator` evaluations of `iterate` and `prioritize` (new project, clear small change that must not decompose, tangled idea), plus a description trigger test for `prioritize` and `memorize`.

## Suggested skills and invocation modes

- Model-invoked, through the Skill tool: `write-for-agents` before editing any skill or instruction file; `document` for project-document rules; `memorize` before writing any script (read `.agents/scripts/INDEX.md` first; use `update-references.py` for renames); `review-and-refactor` for review with a fixed starting revision; `skill-creator` when evaluations resume.
- User-invoked, for the human to run: `/guide`, `/iterate`, `/specify`, `/taskify`, `/graphify`, `/setup-ai-workspace`, `/hand-off`, `/take-over`.

Installed copies may lag the repository until the refresh above; check availability before claiming a renamed skill is callable.

## Publication

Branch `main`, destination `origin/main` (`git@github.com:Dyrits/SKILLS.git`). Normal push only; no force, tag, or package publication. Upstream publication stays disabled.
