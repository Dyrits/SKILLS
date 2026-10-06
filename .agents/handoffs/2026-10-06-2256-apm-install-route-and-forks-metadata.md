# Handoff: APM install route and `forks` metadata, ready to commit

Supersedes: [2026-10-06-2135-remove-auto-handoff-and-skills-audit.md](2026-10-06-2135-remove-auto-handoff-and-skills-audit.md). Its open items are still open and unchanged (the user set them aside for this session); they are not repeated here, except where this session's work touches them.

## State

Everything below is committed and pushed to `origin/main` (commits `c91a54a`, `8eea64b`, `5c0663e`, and the one adding this handoff). The working tree was clean after the push. The next session has no required task from this one: pick from the open items below, and start by testing the marketplace route against the real GitHub repository now that `marketplace.json` is on `main`.

## What this session did

The user wanted skills to declare dependencies on each other with Microsoft APM (`apm`, 0.33.0, run through `uvx --from apm-cli apm`), while staying installable with `npx skills` and `apm`.

1. **Per-skill manifests.** 27 skills that call or hand over to another skill now have an `apm.yml` beside their `SKILL.md`, listing every referenced skill (soft ones too, at the user's request) as a `git: parent` sibling dependency. Cycles exist (8) and APM accepts them.
2. **Root marketplace.** The root `apm.yml` publishes all 47 skills as `<name>@dyrits` through `marketplace:` with local `./skills/...` sources and no tag (the user said not to tag). `apm pack` writes them to a root `marketplace.json` (`claude: output: marketplace.json`). APM reads a root `marketplace.json` before `.claude-plugin/marketplace.json`, and Claude Code reads only the second, so the 47 skills do not show up as junk plugins there. `.claude-plugin/marketplace.json` is untouched.
3. **Generator.** `.agents/scripts/generate-skill-manifests.py` writes all 28 manifests (27 skills plus the root) from the existing `SKILL.md` references, reusing `scripts/check-skills.py`. `--check` lists missing, stale, or orphaned files. Indexed in `.agents/scripts/INDEX.md`; `npm run check-skill-manifests` runs it. Publishing steps: generator, `apm pack`, commit `marketplace.json`.
4. **Docs.** `.agents/install-block.md` has the new APM canonical block, the warning not to use `--skill`, and the publishing steps. `README.md` has the two-line APM install.
5. **`forks` metadata.** 32 skills carry `metadata: forks: "<owner>/<repo>/<path>"` in their frontmatter: the shorthand of the upstream skill they derive from, unpinned (it follows the default branch; GitHub URLs cannot omit the ref, so the user chose the shorthand). `mattpocock/skills` paths were checked against its `main` tree; two skills list two space-separated values (`refine`, `specify`). The other sources are `document` (`anthropics/knowledge-work-plugins`), `unslop` (`cursor/plugins`) and `illustrate` (`humanlayer/skills`). The 14 fork-created skills have none, and neither has `resolve-merge-conflicts`, whose upstream skill was deleted (the user said to drop the key rather than point at history). Renamed from `fork` to `forks` at the user's request (reads as a verb, suits skills with two upstreams).

## What was committed

- `c91a54a`: the generator, 27 per-skill `apm.yml` files, root `apm.yml`, `marketplace.json`, `package.json` script, and the `INDEX.md` line.
- `8eea64b`: `.agents/install-block.md` and `README.md`.
- `5c0663e`: the `forks` metadata on 32 `SKILL.md` files (frontmatter only).

## Facts verified in this session

All APM tests ran against a **local stand-in for the GitHub repository** (a bare clone behind a `GIT_CONFIG_GLOBAL` `insteadOf` rewrite, on a fake non-GitHub host), never the real remote. Test files are deleted; no marketplace is registered in the user's global `apm` config.

- `apm install Dyrits/SKILLS/skills/<bucket>/<name>` installs the skill and its whole dependency closure (tested: `implement` brought 10 skills).
- `apm install Dyrits/SKILLS --skill <name>` does **not**: APM ignores the nested manifests in that form and installs the one skill. No flag forces it. This is why the marketplace route exists.
- `apm marketplace add <fake-host git URL>#main`, then `apm install implement@dyrits --target claude`, installed the same 10 skills, with `.claude-plugin/marketplace.json` untouched.
- `apm pack --check-clean` reports `marketplace.json` unchanged. `check-skills.py`, `build-skill-graph.py --check`, the manifest check, and `claude plugin validate . --strict` all passed after the last change.
- Install scope: project by default, `-g` for user scope. Targets: `--target`, then `apm.yml` `targets:`, then `apm config`, then auto-detection; `--target all` excludes `agent-skills`, `antigravity`, `hermes`, `intellij`. ZCode has no APM target; `--target agent-skills` writes `.agents/skills/`, which ZCode reportedly reads (from a third-party guide, untested).

## Not verified, do not state as fact

- The marketplace route against the **real** GitHub repository: `marketplace.json` is now on `main` but `apm marketplace add Dyrits/SKILLS` followed by `apm install implement@dyrits --target claude` has not been run against it. Test it in a scratch project and remove the marketplace afterwards (`apm marketplace remove dyrits --yes`), since the registration is global.
- `apm install -g` pulling the dependency closure (only project scope was tested).
- `apm` auto-detection with several harness folders present (every test passed `--target claude`).
- `npx skills` ignores `apm.yml` and `metadata.forks` (it listed all skills with the manifests present; the `metadata.internal` behaviour comes from secondary documentation).
- The `forks` values are unpinned, so an upstream rename or removal breaks them silently, as happened to `resolving-merge-conflicts`. The revision each skill was adopted from lives only in the documentation pages.

## Open items touched by this work

- The user said they will later remove the "if a called skill is not installed" install paragraphs from skills (audit item). When they do, the generator still finds plain "Call the Skill tool with X" references; if those lines go too, it must read `flow.json` instead.
- The skill upstream name now lives in two places: each documentation page's provenance line and `metadata.forks`. Decide whether a check should compare them.
- Still open from the previous handoff and not touched: the stale compaction-gate text in `hand-off` (description, `skills/productivity/README.md`, its documentation page, `index.html`, eval 5), and the `README.md` setup paragraph that still names "automatic handoff". Also the stale installs of `setup-auto-handoff` under `~/.agents/skills` and `~/.claude/skills`, and the audit follow-ups.
- `.claude-plugin/plugin.json` carries the version the manifests copy; a version bump means rerunning the generator and `apm pack`. Whether `scripts/sync-plugin-version.mjs` should run them is undecided.

## Suggested skills

- `memorize`: for any standing rule the user states.
- `write-for-agents`: before editing any `SKILL.md` body or description (this session only changed frontmatter metadata).
- `skill-creator`: re-run an eval after a skill change.
- `guide`: re-read after any change to how skills fit the flows (`AGENTS.md` requires it).
- `hand-off` and `take-over`: to write and resume from the next handoff.
