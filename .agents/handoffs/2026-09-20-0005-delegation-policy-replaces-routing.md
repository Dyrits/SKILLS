# Delegation policy replaces classifier routing

**Supersedes:** [2026-09-19-2020-auto-route-change-detection.md](2026-09-19-2020-auto-route-change-detection.md)

The previous two sessions built classifier-driven routing: a `UserPromptSubmit` hook calling classifier.dev on every prompt, and a `dispatch` skill binding its verdict to a tiered subagent. The user rejected the whole bet this session. Classification was not the problem worth solving: the real goal is cheaper, better-scoped work through delegation, and a per-prompt verdict does not deliver it. Both skills were deleted and replaced with one **standing rule** installed into the machine's global steering files.

The work is **staged but not committed**. Nothing has been installed to any steering file yet.

## What exists now

`skills/experimental/setup-delegation-policy/`, user-invoked, not promoted (no `plugin.json` entry, no documentation page). Three files:

- `SKILL.md`: four steps (read policy, install into global steering files, report how tiers bind on this machine, verify), plus a `## Removing it` section.
- `POLICY.md`: the rule itself, 428 words, the single source of truth copied verbatim into steering files.
- `agents/openai.yaml`: Codex metadata with `policy.allow_implicit_invocation: false`.

**Deleted:** `skills/experimental/dispatch/` (including `scripts/setup-agents.sh`), `skills/getting-started/setup-routing-for-claude/` (including the hook script), and the root `context.md` scratch file. `skills/experimental/classify/` was kept as a standalone primitive.

**Re-synced:** top-level `README.md`, `skills/experimental/README.md`, `skills/getting-started/README.md`, and `skills/getting-started/what-is-next/SKILL.md` (the Subagent phase-boundary bullet, the deleted `/dispatch` and `/setup-routing-for-claude` bullets, the `/classify` bullet that defined itself by reference to the dead hook, and a new `/setup-delegation-policy` bullet).

## Decisions settled this session, with their reasoning

These are the ones a next session should not relitigate without new information.

- **A steering file, not a skill.** The routing decision has to happen before any reasoning has bent it, which is exactly when nothing thinks to invoke a skill. This is the reason the whole artifact is an install rather than an invocation.
- **No tiered subagent roster.** Claude Code's `Agent` tool takes a per-call `model` override (`haiku`/`sonnet`/`opus`/`fable`) that beats an agent definition's frontmatter, so named tier agents are unnecessary there. `ROSTER.md` and `setup-agents.sh` were written, then deleted on that basis.
- **Tiers, not model names, as the vocabulary:** `Light`, `Balanced`, `Heavy`, `Frontier` (capitalized). The headline rule is the user's own wording: *If delegating, choose the least expensive model capable of completing the bounded task reliably.*
- **Bucket is `experimental/`**, by user instruction, because the skill writes outside the repository into machine-wide config. Note this does not match the bucket's stated definition in `AGENTS.md` (externally visible actions or third-party APIs); if that bothers a future session, the definition is what needs widening, not the placement.
- **Prohibitions inverted to positives.** "Do not delegate solely to reduce model cost" from the user's original draft became "Delegation earns its place when...", per `writing-for-agents` on negation.
- **No hard wrapping.** `POLICY.md` was initially wrapped at 80 columns and unwrapped to one paragraph per line, matching every other document in the repository.

## Facts established by inspection, not memory

Verified against this machine and the vendors' own data. Worth trusting; worth re-checking if stale.

- **OpenCode global rules live at `~/.config/opencode/AGENTS.md`**, with `~/.claude/CLAUDE.md` as a fallback used only while that file does not exist (opencode.ai/docs/rules). An earlier draft of step 2 named `~/.agents/AGENTS.md`, which is a skills-CLI install directory that no harness reads. This was a real bug, caught and fixed.
- **Codex model ladder is Luna → Terra → Sol → Astra**, from the vendor descriptions in `~/.codex/models_cache.json` (Luna "fast and affordable", Terra "balanced", Sol "reliable workhorse", Astra "most capable"). The user's initial guess had Terra and Luna the other way round.
- **Claude ladder is Haiku → Sonnet → Opus → Fable** ($1/$5, $2/$10, $5/$25, $10/$50 per MTok), from the `claude-api` skill's model table.
- **Codex has no delegation tool**; its lever is session-level `model` + `model_reasoning_effort` in `~/.codex/config.toml`. The routing half of the policy is inert there by design.
- **OpenCode Go pricing and tiering** was derived from `~/.cache/opencode/models.json`. No model names for it reached `POLICY.md` by user instruction, because the free list rotates. The tiering itself is in this session's transcript if ever needed again.

## Machine state, outside the repository

- `~/.claude/CLAUDE.md` and `~/.codex/AGENTS.md` both exist and are **empty**. `~/.config/opencode/AGENTS.md` does not exist. The policy has not been installed to any of them.
- `~/.claude/agents/{Fast,General,Heavy}.md` and the `Agent(general-purpose)` deny in `~/.claude/settings.json` survive from the deleted `setup-agents.sh`. Now unmanaged by any skill, harmless, and still usable as named tier targets. The user was offered removal and did not take it.
- `~/.config/opencode/opencode.json` binds `opencode-go/glm-5.3` (Heavy tier, $1.40/$4.40) to `general`, `explore` **and** `plan`. Read-only agents on a Heavy model is the clearest saving available and step 3 of the skill is written to surface it. Untouched: it is the user's config.
- Stale symlinks for `dispatch` and `takeover` were removed and `scripts/link-skills.sh` re-run; 74 skills link cleanly with none broken.

## Verification already done

Do not redo these unless something changed:

- `claude plugin validate . --strict` passes.
- No stale references to `dispatch`, `setup-routing-for-claude`, `ROSTER`, `setup-agents`, the old tier names, or `~/.agents/AGENTS.md` anywhere in `skills/`, `README.md` or `documentation/`. The remaining `dispatch` hits in `documentation/workflow/` and `documentation/reference/grilling.md` are the ordinary English word.
- Install, re-sync and uninstall were tested on temporary fixtures: exactly one heading per file, the installed section diffs **identical** to `POLICY.md`, re-sync replaces stale content while preserving the following section, and uninstall leaves the rest of the file intact.

## What is next

1. **Commit.** Everything is staged on `main`. No commit has been made this session.
2. **Install, if wanted.** Run `/setup-delegation-policy`. It has never been run end to end against real steering files, only against fixtures.
3. Open question the user raised and has not decided: whether a Haiku orchestrator spawning Opus subagents is worth doing. The answer given was that it works mechanically but inverts the useful pattern, since the routing judgement and the briefing quality then sit with the weakest model. No change was made on the strength of it.
4. Carried over from the superseded handoff and still open: `shellcheck` was never run on the deleted `setup-agents.sh` (now moot), the Codex CLI row in `setup-git-guardrails`, and promotion criteria for experimental skills.

## Suggested skills

- `/writing-for-agents` before editing `SKILL.md` or `POLICY.md` again. `POLICY.md` is always-loaded on every turn of every session, so its word count is the constraint that matters; it grew from 383 to 428 words in the last round of fixes.
- `/code-review` against the commit, once made.
