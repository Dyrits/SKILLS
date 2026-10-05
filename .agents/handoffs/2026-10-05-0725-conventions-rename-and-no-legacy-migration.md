# Handoff: `GUIDELINES.md` renamed `CONVENTIONS.md`, legacy migration removed

Supersedes: [2026-10-05-0714-setup-bucket-and-agents-configuration.md](2026-10-05-0714-setup-bucket-and-agents-configuration.md) (its commit and push already landed as `1b49039`).

## Next session: commit and push

The working tree on `main` holds two finished, verified changes that the user approved but has not committed. The next step is to commit and push to `origin` (`git@github.com:Dyrits/SKILLS.git`). Pushing to `main` is outward-facing: confirm with the user before pushing unless they already said to.

1. Review `git status` and `git diff --stat` (about 23 files).
2. Re-run the checks below; all passed at handoff time.
3. Commit in the repository's style (subject line, short body, then `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`). The user had not yet chosen between one commit and two; ask, or default to two:
   - **Rename**: `skills/reference/model-domain/GUIDELINES-FORMAT.md` → `CONVENTIONS-FORMAT.md` and every `GUIDELINES.md` reference, "Guidelines step" → "Conventions step", `Guidelines:` → `Conventions:` in `skills/setup/setup-ai-workspace/domain.md`, plus the domain-agnostic wording (model-domain, its documentation page, both READMEs, `guide`, `flow.json`, regenerated `index.html`).
   - **Migration cleanup**: removed legacy-version handling from `skills/setup/setup-ai-workspace/SKILL.md` (the `documentation/agents/` move), `skills/setup/setup-auto-handoff/SKILL.md`, `skills/setup/setup-git-guardrails/SKILL.md`, and the documentation pages `setup-ai-workspace.md`, `setup-git-guardrails.md`, `take-over.md`.
   Include this handoff file in the commit: handoffs are committed as shared history here.
4. Push after confirmation.

## Verification commands

```sh
python3 scripts/build-skill-graph.py --check
python3 scripts/check-skills.py
python3 scripts/test-check-skills.py
claude plugin validate . --strict
git diff --check
```

No skill folder was renamed, so `scripts/link-skills.sh` does not need re-running.

## Decisions from this session

- **Keep `GLOSSARY.md`** (not `DOMAIN.md`): the glossary holds vocabulary only, functional rules live in requirements and specifications, `DOMAIN.md` would clash with `.agents/domain.md` and diverge from upstream's own `CONTEXT.md` → `GLOSSARY.md` rename.
- **`GUIDELINES.md` → `CONVENTIONS.md`**, uppercase like `GLOSSARY.md`. The file is explicitly **domain-agnostic**: the test is that it could be copied whole into another project on the same stack, with an unrelated domain, and every rule still applies. The new-file template's lead line says so; see `skills/reference/model-domain/CONVENTIONS-FORMAT.md`.
- **Skills never handle migration from older versions** of the skills (renamed files, moved folders, older hooks). They describe only current conventions. Saved as user memory `no-legacy-migration-in-skills`.
- History records (older handoffs, `.upstream/`, architecture decision records, research) keep old names on purpose.

## Carried over, still undecided

- `~/.agents/skills/improve-agent-environment` is a real directory copy, not a symlink; removal awaits go-ahead.
- Plugin version stays at 0.2.0; no bump decided.

## Suggested skills

- `guide` (model or user): if the user wants a next step after pushing.
- `model-domain` (model): to try the Conventions interview or audit on a real project such as LIFELINE, which still has a `GUIDELINES.md` that the skills no longer look for (how it gets renamed is the user's call).
- `hand-off` (user): at the next session boundary.
