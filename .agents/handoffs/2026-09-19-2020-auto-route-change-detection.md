# Auto-route: change-only firing, new label set

**Supersedes:** [2026-09-19-1759-classify-and-route-skills.md](2026-09-19-1759-classify-and-route-skills.md)

This session continued the classify-and-route work in two moves: first the previous session's `route` → `dispatch` replacement was finished on disk (README re-links, `skills/experimental/route/` deleted, `dispatch/` and `getting-started/setup-auto-route/` written), then the auto-route hook was redesigned around **change-only firing** and a **new label set**, decided through a `/grill-me` interview.

## What changed in this session

All under `skills/`, none of it committed before this session's commit:

- **`getting-started/setup-auto-route/scripts/classify-and-route.sh`**: rewritten.
  - Task labels: `Implementation or refactoring` · `Debugging or diagnosis` · `Planning or design` · `Specification refinement` · `Codebase exploration` · `Code review` · `Undefined` (capitalized; classifier.dev echoes labels verbatim so casing is ours).
  - Complexity labels: `Fast and simple` · `Moderate` · `Large or risky change`.
  - `INSTRUCTIONS` reworked: scope/risk wording kept, plus two discriminators (exploration describes what is, planning decides what will be; debugging investigates before any fix), and deliberately **no tier/agent names**, keeping the hook decoupled from the agent set.
  - **Change detection**: verdict recorded per session in `${TMPDIR:-/tmp}/classify-and-route-<session id>.json` (session id from the hook's stdin, sanitized); the `systemMessage` fires only when task or complexity label changes, never on transitions to `Undefined`; returns from `Undefined` and first prompts always fire. The state is written even when silent, so a return from `Undefined` fires. Thresholds unchanged (0.7 task / 0.6 complexity; low-confidence task reads as `Undefined`).
  - **Message format** (user's design, no role token; dispatch deduces):
    - First: `Route: <task> (<conf>) | <complexity> (<conf>). Use the relevant skill. Consider /dispatch.`
    - Changed: `... (Previous route: <task> | <complexity>). Use the relevant skill. Consider /dispatch as a priority.`
- **`getting-started/setup-auto-route/SKILL.md`**: re-synced (change-only description, verify section now tests the silent repeat and clears `$TMPDIR` state files first).
- **`experimental/dispatch/SKILL.md`**: Step 1 now carries the new message shape plus a verdict→role table (`Debugging or diagnosis` → explorer; `Specification refinement` → planner, or a specification skill inline); the "fires on every prompt" paragraph became "announces change only"; report-line example updated. The hook's line carries labels only; role→agent→model binding stays in dispatch, with models pinned per agent by `setup-agents.sh`.
- **`getting-started/what-is-next/SKILL.md`** and **`skills/getting-started/README.md`**: the `/setup-auto-route` mentions re-worded to change-only firing.
- Top-level `README.md` and `skills/experimental/README.md`: the previous session's `route` → `dispatch` re-links.

Verified live against classifier.dev: first-prompt fires, unchanged verdict silent, label change fires with previous route, transition to `Undefined` silent, return from `Undefined` fires. One bug found and fixed in session: `jq -r`'s trailing newline was sanitized into a trailing `_` in the state filename; now `jq -j`.

Facts settled in session: `systemMessage` is the only `UserPromptSubmit` output field that reaches the model's context (other keys are ignored); hook output never names an agent so tier/model changes touch only `dispatch/SUBAGENTS.md`.

## Late-session addition: the skill was renamed

After the first commit, `setup-auto-route` was renamed to **`setup-routing-for-claude`** (directory, frontmatter `name`, `openai.yaml` display name, bucket README, both `what-is-next` mentions, and all three `dispatch` references), committed as a separate rename commit and then amended to carry this paragraph. The hook script itself is unchanged, including its filename `classify-and-route.sh`. The installed entry `~/.claude/skills/setup-auto-route` is a symlink to the old path and is now stale: re-run `scripts/link-skills.sh` to relink under the new name.

## Open items for a next session

- The unexercised paths from the previous handoff remain: `planner`, `explorer`, `reviewer`, and the heavy tier have never been dispatched end to end; the hook's change-only firing has been tested by piping, not from inside a live Claude Code session.
- The pre-existing open items in the superseded handoff (OpenCode heavy-model choice, `shellcheck` on `setup-agents.sh`, Codex CLI row, promotion criteria) still stand.
- `context.md` at the repository root is session scratch from this conversation and was deliberately left uncommitted; delete or ignore it as preferred.

## Suggested skills

- `/writing-for-agents` before editing either `SKILL.md` again.
- `/code-review` against this session's commit for a second opinion on the hook rewrite.
- `/retro` if the grill-driven design round is worth capturing.

## Git boundary

The user asked for a commit and a push on `main` at the end of this session. This document is part of that commit and cannot record its own hash; verify actual local and remote state before any follow-up.
