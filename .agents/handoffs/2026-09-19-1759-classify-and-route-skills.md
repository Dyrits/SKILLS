# Handoff: classify and route as experimental skills

Supersedes: `.agents/handoffs/2026-09-18-0108-tracker-kinds-and-triage-roles.md`

Created 2026-09-19 17:59. Session goal: turn an ad hoc OpenCode router command into real skills, backed by classifier.dev.

## Starting point

The untracked `opencode/` folder held a `command/route.md` that classified the user's request with two `curl` calls to classifier.dev and dispatched it to an OpenCode subagent, plus two agent definitions (`build-fast`, `build-heavy`) pinning a fast and a heavy model. The session also began by removing the installed `bulk-classify` skill (`npx skills remove bulk-classify -g -y`), which had wrapped the same API.

## Decisions made this session

All the user's calls:

1. **Two skills, not one.** `route` keeps its name and owns the dispatch policy; `classify` is a new skill that classifies any text against any labels and reports the verdict. The seam: `classify` owns the transport and API semantics, `route` owns the label taxonomy and the routing table, and calls the Skill tool with `classify` rather than embedding its own `curl`. One place to change when the API moves.
2. **Both in `skills/experimental/`.** So neither is promoted: no `.claude-plugin/plugin.json` entry, no documentation page under `documentation/`. The bucket's framing in both READMEs was widened, because these two are externally visible by sending the user's text to a third-party API rather than by posting to a tracker.
3. **Both model-invoked.** The user asked for automatic classification before the agent acts, and `route` has to be able to reach `classify`, which only works when `classify` carries a description.
4. **`opencode/` deleted.** The agent definitions survive as installable snippets inside `route/SUBAGENTS.md`; the two thin command files written mid-session went with the folder.

## What changed

See the commit diff rather than a file list. The shape of it:

- `skills/experimental/classify/`: three steps (fix the labels, call it, report the verdict). Covers all three request bodies (`input`, `inputs` batch, `dimensions`), the optional `instructions` / `tier` / `multi` parameters, the size and rate limits, and the failure path. Two disciplines are the substance: one call one verdict (sharpen labels or `instructions` instead of reshuffling until a preferred answer appears), and confidence is calibrated, so a verdict below `0.7` is reported as weak rather than as settled.
- `skills/experimental/route/`: route at the top only (a table covering the subagent case, the follow-up turn whose context a subagent would not get, and the user naming an agent), then classify, then a harness-neutral **role** layer (`planner`, `explorer`, `reviewer`, `implementer-fast` / `implementer` / `implementer-heavy`), then binding, then dispatch with a one-line report. `SUBAGENTS.md` holds the per-harness bindings and the agent definitions to install.
- Improvement over the original `route.md`: one request instead of two, using classifier.dev's `dimensions` form to return task type and complexity together.
- `what-is-next` gained both skills under Standalone, and its Subagent bullet under Phase boundaries now points at `/route`.

## Verification done

Exercised classifier.dev live and confirmed the documented shapes: singular `input`, batch `inputs`, and `dimensions` with `instructions`, including a deliberately ambiguous request that returned a low complexity confidence (`0.38`), which is the calibration the `classify` skill leans on. `claude plugin validate . --strict` passes. `scripts/link-skills.sh` re-run; both skills resolve in `~/.claude/skills` and `~/.agents/skills`.

## Open items for a next session

- Neither skill has been run end to end from its own invocation. The API calls are verified, the skill bodies driving them are not.
- `route`'s binding step names Claude Code's `Agent` tool and OpenCode's `task` tool from this session's environment. Confirm OpenCode's built-in agent names against a live OpenCode session before trusting that row of the table.
- Codex CLI is documented as having no delegation tool, so every role runs inline there. Unverified against a current Codex build.
- Promotion is still open: if either skill proves itself, moving it out of `experimental/` means a plugin entry, both README listings, and a documentation page per `.agents/writing-documentation.md`.

## Suggested skills

- `/writing-for-agents` before editing either `SKILL.md`, and its `SKILL-MECHANICS.md` for the invocation choice.
- `/code-review` against this session's commit for a second opinion on the two new skills.

## Git boundary

The user asked for a commit and a push at the end of this session. Verify actual local and remote state before any follow-up: this document is part of the commit and cannot record its own hash.
