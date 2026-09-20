# Tier agents across binding harnesses

**Supersedes:** [2026-09-20-0005-delegation-policy-replaces-routing.md](2026-09-20-0005-delegation-policy-replaces-routing.md)

The previous handoff left `setup-delegation-policy` as a steering-file installer that had never been run. This session ran it end to end, found the gap that running it exposed, and closed that gap: on harnesses that bind a model per named agent, installing the rule alone installs something unfollowable, because the agent can only name a tier and no agent carries that name. The skill now writes those agents.

Everything below is **committed and pushed to `main`** unless stated otherwise.

## What the skill is now

`skills/experimental/setup-delegation-policy/`, user-invoked, not promoted. Four files:

- `SKILL.md`: five steps (read policy, install into five steering files, write tier agents per binding harness, report how tiers bind, verify), plus `## Removing it`.
- `POLICY.md`: the rule, 427 words, copied verbatim into steering files.
- `TIER-AGENTS.md`: new. Disclosed reference for harnesses that bind per agent.
- `agents/openai.yaml`: Codex metadata.

Re-synced alongside it: both `README.md` entries, `skills/getting-started/what-is-next/SKILL.md` line 84.

## Decisions settled this session

Do not relitigate these without new information.

- **Harnesses fall into exactly three lever shapes**, and the skill handles all three: per-call model override (Claude Code, nothing to configure), per-agent model binding (OpenCode, ZCode, Gemini CLI, write agent files), session-level only (Codex, report and leave it). A new harness is cheap to add precisely because it lands in one of these.
- **No harness-specific model guidance in `POLICY.md`.** The line telling the agent to prefer the OpenCode Go catalogue was deleted: on OpenCode the runtime agent picks a `subagent_type`, never a model, so the instruction was addressed to nobody. For the same reason ZCode and Gemini get **no columns** in the tier table, though the user proposed adding them. `POLICY.md` is loaded every turn of every session, so a no-op there is the most expensive kind.
- **One agent per tier, never one agent per model.** One-per-model was considered and rejected: it turns a 4-item choice into a 28-item one, and every agent description is a pointer the orchestrator reads before choosing, to gain a distinction it cannot act on.
- **Only OpenCode asks.** Its catalogue spans five providers and rotates, so its ladder is chosen live. ZCode and Gemini run one model family each, so their ladders are pre-defined in `TIER-AGENTS.md`.
- **One file, not two.** The user floated reverting to an OpenCode-only `OPENCODE-AGENTS.md`. Rejected: all three harnesses share the output shape, the frontmatter discipline, the verification and the short-ladder rule, so a split would duplicate all of it. What was wrong was the file's shape, fixed by a "Choosing the model" table row and a `Pre-defined ladders` section.
- **A harness with fewer rungs than the policy gets no filler.** Two tiers on one binding is a distinction that does not exist. Both ZCode and Gemini stop at Heavy, by user decision for Gemini.

## Facts established by inspection

Verified against this machine or vendor source, not memory.

- **Steering files, five of them**: `~/.claude/CLAUDE.md`, `~/.config/opencode/AGENTS.md`, `~/.codex/AGENTS.md`, `~/.zcode/AGENTS.md`, `~/.gemini/GEMINI.md`. ZCode is documented as not reading `CLAUDE.md` at runtime, so it has no fallback.
- **OpenCode**: `task` takes `description`, `prompt`, `subagent_type`, `task_id`, `command`, `background`. No model parameter (`packages/opencode/src/tool/task.ts`). `agent.<name>.model` is a single string; no arrays, no per-call override. Built-ins: `build` and `plan` primary, `general` and `explore` subagents, `build` the default.
- **Gemini CLI**: agents at `~/.gemini/agents/<name>.md`, snake_case frontmatter `name`, `description`, `model`, `tools`, `temperature`, `max_turns`, `timeout_mins`. **No reasoning field**, so the level comes from `modelConfigs.customAliases` in `settings.json`, which the agent's `model:` names.
- **ZCode**: agents at `~/.zcode/agents/<name>.md`, camelCase and case-sensitive, `name` and `description` required. `thoughtLevel` only takes effect beside an explicit `model`. No project-level subagents yet.
- **`~/.agents/skills/*` are real copies, not symlinks**, and `~/.claude/skills/*` symlink into those. Something other than `scripts/link-skills.sh` owns that layout, so repository edits do **not** reach installed skills and `git pull` will not either. This contradicts both `CLAUDE.md` and the superseded handoff. Only `setup-delegation-policy`'s copy was refreshed by hand; every other installed skill is a stale snapshot.

## Machine state, outside the repository

- All five steering files carry the current policy, one heading each, diffing identical to `POLICY.md`.
- `~/.claude/agents/{Fast,General,Heavy}.md` **deleted** and the `Agent(general-purpose)` deny **removed** from `~/.claude/settings.json`. The per-call override makes named tier agents unnecessary on Claude Code, and the deny would otherwise have blocked the only remaining target. Backups in `/tmp/claude-agents-backup/`.
- `~/.config/opencode/agents/`: `light`, `balanced`, `heavy`, `frontier`. **These bindings were picked by hand, not derived by the skill**, and all sit on metered `opencode-go/*` while `zai-coding-plan` covers part of the ladder at zero marginal cost. Re-running the skill is what fixes this.
- `~/.zcode/agents/`: `light`, `balanced`, `heavy` on `glm-5.3-flash`, `glm-5.3`, `glm-5.3` + `thoughtLevel: high`. Balanced was moved off `glm-5.2` after occurrence-counting suggested that id is listed rather than served.
- `~/.gemini/agents/`: `light`, `balanced`, `heavy` pointing at aliases `tier-light`, `tier-balanced`, `tier-heavy` in `~/.gemini/settings.json` (backup at `settings.json.bak`), all on `gemini-3.8-flash` at `LOW`, `MEDIUM`, `HIGH`.
- `gemini-cli` upgraded 0.26.0 to 0.46.0 via brew. **The formula is now deprecated** and 0.46.0's bundle lists ids only up to `gemini-3.5-flash`.

## Open, and why

1. **Gemini is unverified end to end.** `GEMINI_API_KEY` is not in the environment, so `gemini -p` never returns. `gemini-3.8-flash` is newer than anything in the 0.46.0 bundle and relies on the model string passing through to the API. If it is rejected, the fallback is `gemini-3.5-flash` in the three aliases and nothing else changes. Consider an npm install over the deprecated brew formula.
2. **ZCode is unverified end to end**: a desktop runtime with no CLI available here to spawn a subagent.
3. **OpenCode bindings should be re-derived** by running `/setup-delegation-policy` rather than left as this session's hand-picks.
4. **The installed-skills layout** (copies, not symlinks) means every other installed skill is stale. Re-running `scripts/link-skills.sh` would convert them, which is a machine-wide change nobody has approved.
5. Carried over and still open: the Codex CLI row in `setup-git-guardrails`, and promotion criteria for experimental skills.

## Suggested skills

- `/writing-for-agents` before touching `POLICY.md`, `SKILL.md` or `TIER-AGENTS.md`. `POLICY.md` is always-loaded, so its word count is the binding constraint; `TIER-AGENTS.md` was pruned 1757 to 1283 words this session and should not drift back.
- `/setup-delegation-policy` to re-derive the OpenCode ladder properly.
- `/code-review` against this session's commit.
