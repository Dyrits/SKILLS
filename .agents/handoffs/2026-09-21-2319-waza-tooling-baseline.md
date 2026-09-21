# Waza tooling baseline and documentation reorganisation

Supersedes: none (new thread; the previous handoff, `2026-09-20-1011-upstream-sync-to-pull-request.md`, covers unrelated work).

## What this session did

Installed and exercised `waza` (Microsoft's agent-skills evaluation CLI) against this repository, fixed what it caught, and landed the documentation tree reorganisation.

- `waza` 0.38.7 installed at `~/bin/waza` (bash installer; `/usr/local/bin` was not writable). Fish shell set up: `fish_add_path "$HOME/bin"` in `~/.config/fish/config.fish`, completions at `~/.config/fish/completions/waza.fish`.
- `waza check` run over all 38 skills; the report lives at `documentation/evaluation/waza.md`. Headline: 0 of 38 "ready", 37 Low / 1 Medium compliance, 28 over waza's 500-token default limit, 0 eval suites, and spec friction from `argument-hint` (8 skills) and `disable-model-invocation` (21 skills), which are deliberate Claude Code conventions here, not defects.
- Fixed `skills/getting-started/what-is-next/SKILL.md`: the unquoted `description:` contained a colon plus space, which is invalid YAML for any strict parser. Now double-quoted, matching the other skills. The bug was inherited from upstream at the fork point.
- Documentation reorganisation (done outside this session, verified and repaired here): 29 pages moved from `documentation/<bucket>/` to `documentation/skills/<bucket>/` (verified 1:1, nothing lost), `waza.md` report moved to `documentation/evaluation/`. Repairs that followed from the move: three `../../skills/...` links in `documentation/skills/workflow/to-pull-request.md` needed a third `../`; the what-is-next link in `.agents/writing-documentation.md`; the layout line in `CLAUDE.md`.
- `.DS_Store` added to `.gitignore`.
- Upstream comparison for context: `mattpocock/skills` at HEAD scores essentially the same under waza (0 ready, 36 Low / 2 Medium, 28 over limit, 0 evals). Conclusion reached: `waza check`'s readiness framing encodes the agentskills.io submission spec, which this repository deliberately does not target. The relevant subset of its findings is YAML validity, eval coverage, and token cost awareness.

## Known issue

`waza quality <skill-path>` fails on waza 0.38.7 (embedded Copilot CLI 1.0.64) with `parsing judge response: invalid judge JSON: invalid character '\'' in string escape code`. Looks like a waza-side bug parsing the judge model's output. Not investigated further.

## Open follow-ups

1. `upkeep/improve-agent-environment` is a promoted skill with no documentation page (never existed, not lost in the move; `git log --all` on the path is empty). Per `CLAUDE.md`, a promoted skill needs a page written per `.agents/writing-documentation.md`.
2. `documentation/skills/getting-started/setup-custom-skills.md` exists although `setup-*` skills are non-promoted and per `CLAUDE.md` should carry no page. Pre-existing, and other pages link to it; decide keep-plus-exception or remove-plus-relink.
3. Decide whether to adopt waza eval suites (`waza suggest <skill> --apply` to draft, review, then `waza run`). Zero coverage today means skill changes have no regression gate.
4. The waza report at `documentation/evaluation/waza.md` is a snapshot of 2026-09-21; re-run after skill changes if it is to stay meaningful.

## Suggested skills

- `/take-over` to resume from this handoff.
- `/writing-for-agents` for any follow-up editing of `SKILL.md` content.
- `/triage` if the follow-ups above should become tracker tickets instead of living only here.

Handoff written before the commit that carries it, so reference the log rather than a hash: the commit titled "Move skill documentation under documentation/skills and add waza evaluation baseline".
