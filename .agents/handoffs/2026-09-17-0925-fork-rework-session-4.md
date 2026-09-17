# Skills repository fork rework, session 4

Supersedes: `.agents/handoffs/2026-09-17-0916-workflow-and-documentation-reorganization.md`

## Current state
All changes from this session are uncommitted on `main`. `HEAD` and `origin/main` remain at the prior commit (`f85ffd7` — "Reorganize skills into new buckets and update plugin manifest"). The working tree contains the complete change set described below. Existing work from earlier handoffs was preserved and extended rather than recreated.

## Decisions and completed changes

- `skills/flow/` is now `skills/workflow/`, with promoted documentation mirrored under `documentation/workflow/` and every manifest, link, script, repository instruction, changelog entry, changeset, and handoff reference updated.
- `skills/in-progress/` is now `skills/work-in-progress/`; it remains public, locally linked, excluded from the plugin, and without promoted documentation pages.
- Repository architecture decisions now live under `documentation/architecture-decision-record/`; the old `.agents/adr/` files were moved there and the domain-modeling convention no longer creates `docs/adr/`.
- `skills/reference/domain-modeling/ADR-FORMAT.md` is now `ARCHITECTURE-DECISION-RECORD-FORMAT.md` and its callers use the expanded name.
- `CLAUDE.md` now carries the repository-wide language convention: prefer full words such as repository, document or documentation, specification, and architecture decision record, with exceptions for literal external names, commands, APIs, URLs, established technical terms, and defined repeated abbreviations. `AGENTS.md` is a symlink to `CLAUDE.md`, so both harnesses receive the rule.
- `setup-custom-skills` supports GitHub, GitLab, Jira, local markdown, optional local refinement drafts, and an optional ticket-writing convention. It can point at a repository template or ticket-writing skill such as `create-jira-ticket` without making that skill mandatory or handing it control of decomposition and publication.
- `to-tickets` confirms the configured ticket-writing convention, keeps its built-in format as a fallback, and retains ownership of tracer-bullet decomposition, blocking edges, approval, and the local-versus-published boundary.
- `to-spec` was renamed to `to-specifications`, and generated specification artifacts use `specification.md`.
- Active repository prose and paths use `documentation` rather than a local `docs` directory. No `docs/` directory exists.
- Local Claude and Codex skill symlinks were refreshed with `scripts/link-skills.sh` and point at the renamed bucket paths.
- Out-of-scope convention moved from `.out-of-scope/` to `documentation/out-of-scope/`; triage SKILL.md, OUT-OF-SCOPE.md, AGENT-BRIEF.md updated; `.upstream/out-of-scope/` archive kept as upstream history.
- Triage-labels.md extended with category roles (`bug`, `enhancement`) alongside existing state roles; setup Section B offers both sets as defaults with customisable label strings; the role set itself stays canonical.
- `writing-docs.md` → `writing-documentation.md`; `CLAUDE.md` references updated.
- Plugin/package renamed: `mattpocock` → `dyrits`, `mattpocock-skills` → `dyrits-skills`; `package.json` name → `dyrits-skills`, repo URL → `Dyrits/SKILLS`; changesets scripts and devDependencies removed, lockfile regenerated.
- `.github/workflows/` deleted (release.yml).
- `.agents/adr/` deleted (empty).
- Install block `.agents/install-block.md` rewritten around `npx skills@latest add Dyrits/SKILLS` as the sole documented route; plugin now undocumented fallback (`marketplace add Dyrits/SKILLS` → `install dyrits-skills@dyrits`).
- `.upstream/` contains `changeset/` and `out-of-scope/` (moved from top-level).
- `loop-me` moved to `workflow/design-workflow` and promoted (plugin entry, docs page `documentation/workflow/design-workflow.md`, bucket + top-level README entries).
- `retro` moved to `upkeep/improve-agent-environment` as non-promoted skill (marked "(Not in the plugin)" + STUB in bucket README).
- `setup-ts-deep-modules` removed entirely (folder, SKILL.md, dependency-cruiser.config.cjs deleted; reference in `documentation/reference/codebase-design.md` updated).
- Plugin validates (`claude plugin validate . --strict` passes), `npm run check-plugin-version -s` passes, symlinks refreshed.

## Primary artifacts (paths relative to repository root)

- `.agents/install-block.md`: rewritten for `npx skills@latest add Dyrits/SKILLS`
- `.agents/writing-documentation.md`: renamed from `writing-docs.md`; `CLAUDE.md` references updated
- `.claude-plugin/plugin.json`: `dyrits-skills`/`dyrits`; skills list updated
- `.claude-plugin/marketplace.json`: `dyrits`/`dyrits-skills`
- `package.json`: `dyrits-skills`, repo `Dyrits/SKILLS`, changesets/scripts removed
- `CLAUDE.md`: references to `writing-documentation.md`; installation conventions
- `README.md`: badge `skills.sh/b/Dyrits/SKILLS`; install section for `npx skills@latest add Dyrits/SKILLS`
- `skills/workflow/README.md`, `README.md`: updated skill listings
- `skills/productivity/hand-off/SKILL.md`, `take-over/SKILL.md`: renamed frontmatter
- `skills/upkeep/debug/SKILL.md`, `resolve-merge-conflicts/SKILL.md`: renamed frontmatter
- `skills/workflow/test-driven-development/SKILL.md`: renamed from `tdd`
- `documentation/out-of-scope/`: new convention path
- `.upstream/`: contains `changeset/` and `out-of-scope/` (moved from top-level)
- `.agents/`: `install-block.md`, `invocation.md`, `writing-documentation.md`
- `documentation/workflow/design-workflow.md`: new docs page for promoted skill

## What is next

1. Commit and push changes to `github.com/Dyrits/SKILLS` so `npx skills add Dyrits/SKILLS` works
2. (optional) Clean remaining historical `mattpocock` citations if desired

## Suggested skills

The next agent should call the Skill tool for the following, in order:

1. **`code-review`** — two-axis review (Standards + Spec) of the consolidated commit against `f85ffd7`.
2. **`writing-for-agents`** — before further edits to skills or repository instructions (`AGENTS.md`, `CLAUDE.md`, plugin.json).
3. **`what-is-next`** — to re-read the router and verify the skill map stays accurate after these additions/renames.

(All three are model-invoked skills reachable via the Skill tool; their frontmatter carries `disable-model-invocation: false`.)
