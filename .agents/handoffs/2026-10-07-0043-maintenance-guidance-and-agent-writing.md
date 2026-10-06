# Handoff: maintenance guidance and write-for-agents

Supersedes: [2026-10-06-2256-apm-install-route-and-forks-metadata.md](2026-10-06-2256-apm-install-route-and-forks-metadata.md). Earlier open work remains pending except where this handoff records a change.

## State and next session

The user requested this handoff, a commit, and a push. The receiving branch is `main`; the publication remote is `origin` at `git@github.com:Dyrits/SKILLS.git`. The session started at `6b8534d`. This handoff accompanies the delivery changes; verify the commit and remote status rather than treating this pre-commit document as proof of a successful push.

No further audit item is authorized. The user chose `write-for-agents` first because it guides the remaining skill work. Its focused revision is complete, but its behavioral evaluations were explicitly deferred. Start by reading the current skill and asking which remaining audit item the user wants next, rather than following the audit's old priority order automatically.

## Decisions and completed work

- There is no skill promotion or deprecation workflow. Every skill has the same manifest, listing, documentation, evaluation, and graph obligations. `AGENTS.md`, current documentation, and the scripts now use that rule. Historical records were preserved.
- Repository-maintenance guidance moved from `.agents/` to `documentation/maintenance/`. Start with its `README.md`. The installation guide is `standard-installation-wording.md`, and the evaluation guide is `writing-evaluations.md`. Agent helpers, installed skills, and session state remain in `.agents/`.
- The installation section in `README.md` now includes whole-set global APM installation and update commands for both skills.sh and APM. Standard wording is synchronized in the maintenance guide. Read those files for the commands rather than copying earlier handoffs.
- `skills/reference/write-for-agents/SKILL.md` retains its structure and useful defined terms. It now directly requires the official Anthropic authoring webpage for skill creation or editing, uses a conditional repetition test instead of "Go find them," removes decorative metaphors, qualifies behavioral claims, and allows leaving useful text unchanged. `SKILL-MECHANICS.md` points to the official page rather than copying frontmatter limits.
- `skill-creator` is an optional external dependency from `anthropics/skills` for requested skill evaluations. The invocation condition and missing-installation response are in the skill. `scripts/check-skills.py` recognizes it as external, so it is not incorrectly treated as a package shipped by this collection or added to generated sibling manifests.
- The skill's human-facing documentation and generated `index.html` were synchronized. Its description and trigger scope did not change.

## Evidence and limits

The following passed after the integrated changes:

- `python3 scripts/check-skills.py`: 47 skills, 47 plugin paths, 47 documentation pages.
- `python3 scripts/test-check-skills.py`: 36 tests.
- `python3 .agents/scripts/generate-skill-manifests.py --check`: 28 manifests current.
- `git diff --check`.

The graph was regenerated with `python3 scripts/build-skill-graph.py`. The checker tests cover uniform skill obligations across bucket names and recognition of external dependencies. They are repository tooling tests, not behavioral evaluations of the rewritten skill.

The user supplied real terminal evidence that `apm marketplace add Dyrits/SKILLS` registered 47 entries, and that a whole-set global installation with `--force` integrated 47 skills into four targets. Without `--force`, the installation failed at an existing `research` symlink and skipped locally managed files. A later `apm update --global` succeeded. The agent's own dry run established package-name acceptance only, not successful installation. These observations do not verify every single-skill dependency closure in global scope.

## Deferred work and boundaries

- Do not rewrite or run skill evaluations without renewed scope. `write-for-agents/evals/evals.json` still contains expectations tied to the previous wording and vocabulary. Opus suggested removing evaluation 7's routing expectation, but that would leave only one expectation, below the checker minimum of two. Revisit the evaluation set coherently when authorized.
- Global installed copies were not refreshed by the agent. User-supplied Opus feedback reported that `~/.agents/skills/write-for-agents` was a copy matching `HEAD`, not a repository symlink. This was not reverified after the APM update. Repository changes do not establish that the installed copy has changed.
- `scripts/link-skills.sh` was not run against the real home directory. It would replace installed copies with repository links and could conflict with the user's APM-managed setup. Ask before changing that installation strategy.
- The requested Claude Opus subagent was stopped by the user because Claude access was unavailable in Delta. The user later supplied Opus feedback directly; the focused revision follows that discussion. Do not claim an independent completed model review.
- `AUDIT.md` remains historical assessment, not current verified behavior. Its `write-for-agents` section is partly superseded by this work. The user rejected a broad rewrite in favor of keeping useful terminology and making focused changes.
- Other audit work, the earlier stale compaction-gate references, and the install-fallback redesign remain as described in the superseded handoff. They were not addressed here.

## Suggested skills

Invoke these through the Skill tool when their conditions apply:

- `take-over`: resume from this handoff.
- `address-feedback`: assess the next audit findings and agree their disposition before implementation.
- `write-for-agents`: reference guidance before skill or steering-file edits; read the working-tree version if the installed copy is stale.
- `skill-creator`: only when the user authorizes skill evaluation or trigger testing.
- `document`: synchronize human-facing documentation with approved behavior.
- `memorize`: record user corrections and standing rules in their existing authoritative home.
- `guide`: check routing when a skill's place in the workflows changes.
- `hand-off`: write the next versioned handoff at a requested boundary.
