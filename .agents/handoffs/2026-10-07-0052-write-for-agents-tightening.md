# Handoff: write-for-agents tightening

Supersedes: [2026-10-07-0043-maintenance-guidance-and-agent-writing.md](2026-10-07-0043-maintenance-guidance-and-agent-writing.md). Its deferred work and boundaries still hold except where this handoff records a change; they are not repeated here.

## State and next session

This handoff is committed and pushed to `origin/main` together with the change it describes. No further work is authorized. Start by asking the user which audit item (`AUDIT.md`) comes next instead of following the audit's old priority order.

## What this session did

The user reviewed the `write-for-agents` revision from `52e9cf3` and asked for the follow-up fixes. The diff of the commit carrying this handoff is the record; in short:

- The instruction to read the official best-practices page now lives only in `SKILL.md`; `SKILL-MECHANICS.md` points back to it. The duplicate `skill-creator` introduction near the top of `SKILL.md` was removed (the Pruning paragraph keeps the full rule; `scripts/check-skills.py` tracks external skills through its own `EXTERNAL_SKILLS` set).
- Disclaimers aimed at the audit ("not proof of its cause", "a hypothesis to check", "not a claim that negative instructions always fail") were replaced by one-clause reasons or actions. The Leading words section, which kept the strongest unsupported claims, was condensed to what to do.
- The file now uses American spelling (the repository majority). `SKILL.md` is about 1,417 words, down from 1,575.
- Eval 3's failure-mode list says "stale material" instead of "sediment", a term the skill no longer defines. No other eval was changed, and no eval was run.

The documentation page `documentation/skills/reference/write-for-agents.md` was re-read and still matches; it was not changed.

## Decisions

- Eval 7 keeps both expectations, including the one that routes a developer README to `document`. The user decided this: READMEs are inside `document`'s current scope. Revisit only if `document` is split. (The previous handoff's note that Opus suggested removing it is superseded.)
- `write-for-agents` stays in `skills/reference/`. The user asked about a new "documentation" bucket; the agent recommended against it and the user agreed: the skill matches the `reference` definition in `AGENTS.md`, the name clashes with the `documentation/` tree, and moving it changes the published APM install path. Open idea, not authorized: regroup `reference` by purpose (for example writing: `write-for-agents`, `unslop`, `document`), treated as its own audit item with its install-path cost.

## Evidence and limits

Passed after the change: `python3 scripts/check-skills.py`, `python3 scripts/build-skill-graph.py --check`, `python3 .agents/scripts/generate-skill-manifests.py --check`, `git diff --check`.

`python3 scripts/test-check-skills.py` fails one test, `test_linker_includes_every_bucket`, on this macOS machine, and fails identically on `52e9cf3` without this change. The temporary directory resolves to `/private/var/...` while the expected path is built from unresolved `/var/...`. Likely fix: resolve `self.root` before comparing. Not fixed; the previous handoff's "36 tests passed" does not hold here.

The rewrite is editorial judgment: no behavioral evaluation was run.

## Still open for this skill

- Trigger scope: add "reusable agent instructions and delegation briefs" to the description, with two trigger evals and one no-trigger eval (an ordinary chat request). Agreed in direction, not authorized.
- The installed copy at `~/.agents/skills/write-for-agents` was a plain copy matching an older `HEAD`, not a repository symlink. Not refreshed; ask before running `scripts/link-skills.sh`, which could conflict with the user's APM-managed setup.

## Suggested skills

Invoke these through the Skill tool:

- `take-over`: resume from this handoff.
- `address-feedback`: agree dispositions on the next audit findings before editing.
- `write-for-agents`: before editing any `SKILL.md` or `AGENTS.md`; read the repository copy, since the installed one may be stale.
- `skill-creator`: only when the user authorizes evaluations or trigger testing.
- `document`: re-sync a documentation page when a skill's behavior changes.
- `memorize`: when the user corrects you or states a standing rule.
- `guide`: re-check routing when a skill's place in the flows changes.
- `hand-off`: at the next phase boundary the user names.
