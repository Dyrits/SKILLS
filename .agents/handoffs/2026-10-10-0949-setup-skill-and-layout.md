# Handoff: one setup skill, skill folder layout, and the bucket structure

Supersedes: `2026-10-08-2109-agnostic-setup-skills.md`
Workspace: Dyrits/SKILLS repository, branch `main`

To resume: read this whole file first. Treat every claim in State not marked verified as unverified, and check it against the Sources. Read the superseded handoff only when something here cannot be resolved from this file and its Sources. Confirm what was in flight and what you will do next with the user before starting. Never edit this file: a later state goes into a new handoff.

## Goal

Settle where the merged `setup` skill lives now that the `setup/` bucket holds a skill also named `setup` (`skills/setup/setup/`), by reconsidering the bucket folder structure under `skills/`. Then carry on with the open `AUDIT.md` priorities the superseded handoff lists.

## State

Done and committed on `main` (commits `ba72ae6`, `57e8eb8`, `ef8384b`, `067c4ee`, plus the commit carrying this handoff):

- The `guide` skill is removed (`ba72ae6`). Its thread is finished, so its `AGENTS.md` pointer was removed with this handoff. Verified: `git log`.
- `setup-ai-workspace`, `setup-git-hooks`, `setup-git-guardrails`, and `setup-ai-tooling` are merged into one skill at `skills/setup/setup/` (`57e8eb8`), recorded in `documentation/architecture-decision-record/0007-merge-project-setup-into-one-skill.md`, which supersedes the setup and `codify` bullets of 0005. `SKILL.md` runs `scripts/inspect-project.py`, offers four areas (workspace, code checks, Git guardrails, AI tooling), and reads one reference per picked area. Tools install through their own command-line installers listed in dated catalogues, with output sent to a log. lint-staged is gone. `codify` moved to `skills/upkeep/codify/`. `setup-delegation-policy` stays separate. Verified: file reads and the checks below.
- Code checks keep language-neutral steps in `references/CODE-CHECKS.md` and one catalogue per language: `references/CHECKS-JAVASCRIPT.md`, `CHECKS-PYTHON.md`, `CHECKS-GO.md`, `CHECKS-RUST.md` (`ef8384b`). Commands were checked on 2026-10-10 against the official documentation (Bun `bun check`, Biome, oxlint, oxfmt, Ruff, ty, golangci-lint, Clippy, CodeGraph, RTK, Context7, Playwright CLI, Chrome DevTools MCP, ast-grep). Not checked: the `gh` and `glab` install lines, rustfmt's commands, and golangci-lint's configuration file names. `bun check` could not be run locally (installed Bun is 1.3.14).
- Each catalogue carries `Verified: YYYY-MM-DD`; `scripts/check-skills.py` prints a non-failing `WARNING` once that date is over 183 days old. `AGENTS.md` says what to do with the warning. Verified: `scripts/test-check-skills.py` covers stale and fresh dates.
- Every skill now follows the Agent Skills specification layout (`067c4ee`): `scripts/` for code the agent runs, `references/` for documents it reads (UPPERCASE names), `assets/` for templates and payloads copied elsewhere (kebab-case names). 157 files moved; links and plain-text paths were rewritten. `check-skills.py` fails on a misplaced or misnamed file. The rule is in `AGENTS.md`. Historical records (handoffs, decision records, `documentation/research/`) were left unchanged, so some of their links to skill files are now broken on purpose.
- Verified at the end of the session, all passing: `npm run -s test-inspect-project`, `test-detect-harnesses`, `test-guard-git`, `test-skills-check`, `test-scriptbook-helpers`, `check-skills`, `check-skill-manifests`, `check-plugin-version`, and `claude plugin validate . --strict`.
- Found and left alone: `skills/productivity/teach/references/GLOSSARY-FORMAT.md` is linked from nowhere in its skill, and was not linked before the move either (checked at `99d9b00`).
- Not done: `scripts/link-skills.sh` was not run, so the user's installed links in `~/.claude/skills` and `~/.agents/skills` may still include the four removed setup skills and `guide`. Assumed, not checked.

## Decisions

- One `setup` skill for per-repository setup; machine-wide delegation stays in `setup-delegation-policy`. Recorded in 0007.
- No repository-specific installer command-line tool: catalogues of upstream commands, quiet output, documentation read only on failure. Recorded in 0007; the broader installer question stays deferred in `.agents/deferred-tooling.md`.
- In an empty project, `setup` asks for the stack but does not choose it; choosing belongs to `architect`. Recorded in 0007.
- Older tooling (ESLint, Prettier, Black, isort, Flake8) gets an offered move, never an automatic one. Recorded in the catalogues and 0007.
- Catalogue staleness warns rather than fails, at six months (the user left the choice to the agent). Recorded in `scripts/check-skills.py` and 0007.
- Skill layout: `references/` UPPERCASE, `assets/` kebab-case, executable code in `scripts/` (so `scripts/pre-push` and `scripts/guard-git.py` stay in `scripts/` although they get copied). Recorded in `AGENTS.md`.

## Next

1. Reconsider the bucket structure under `skills/` (`productivity`, `setup`, `shaping`, `upkeep`, `version-control`, `workflow`). The trigger: `skills/setup/setup/` reads as a stutter, and with `codify` moved out the `setup/` bucket holds only `setup` and `setup-delegation-policy`. Options to put to the user: move both into another bucket and drop `setup/`; rename the bucket; keep it. Present a recommendation. Any move must update `.claude-plugin/plugin.json`, both READMEs, the documentation tree (`documentation/skills/<bucket>/`), `scripts/skill-graph/flow.json` and a rebuild of `index.html`, the manifests (`python3 .agents/scripts/generate-skill-manifests.py`), the paths in `scripts/test-*.py`, and the bucket list in `AGENTS.md`. Then rerun the checks listed in State.
2. Ask whether to run `scripts/link-skills.sh` and delete the stale installed links in the home directory.
3. Continue the open `AUDIT.md` priorities listed in the superseded handoff (2, 4, 5, the rest of 8, 9). 10 is resolved by the `guide` removal. The Biome and "Token Monitor" items of 8 no longer apply in their old form; recheck them against `skills/setup/setup/references/`.
4. Try `setup` in a real repository (one JavaScript or TypeScript project, one Python project) and correct what it gets wrong.

## Open questions

- Where should `setup` and `setup-delegation-policy` live, and should the `setup/` bucket remain? The user decides.
- Should the orphaned `teach/references/GLOSSARY-FORMAT.md` be linked from `teach/SKILL.md` or deleted? The user decides.
- 0005 still plans to retire `setup-delegation-policy`; 0007 left that untouched. Does the plan stand? The user decides.

## Sources

- `documentation/architecture-decision-record/0007-merge-project-setup-into-one-skill.md` and `0005-make-skills-autonomous.md`.
- `skills/setup/setup/` (`SKILL.md`, `references/`, `assets/`, `scripts/inspect-project.py`), `documentation/skills/setup/setup.md`.
- `scripts/check-skills.py`, `scripts/test-check-skills.py`, `scripts/test-inspect-project.py`.
- `AGENTS.md` (layout rule, catalogue warning, bucket list).
- Commits `ba72ae6`, `57e8eb8`, `ef8384b`, `067c4ee`.
- `AUDIT.md`, section "Priority problems", and `.agents/handoffs/2026-10-08-2109-agnostic-setup-skills.md`.
- Agent Skills specification: https://agentskills.io/specification
