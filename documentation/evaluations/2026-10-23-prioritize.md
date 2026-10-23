# 2026-10-23 prioritize

Written 2026-10-23 (UTC). Runs took place on 2026-10-23.

## Result

The skill fires and does its job: 3 of 3 runs with the plugin recommended one focus or asked only focus-blocking questions, and wrote no code (score 1.00). Without the plugin, 2 of 3 runs passed (0.83, Δ +0.17). The near-miss negative, an effort blocked on unsettled design decisions, never fired `prioritize` (6 of 6).

## What was evaluated

| Item | Value |
| --- | --- |
| Skill | [`skills/shaping/prioritize/SKILL.md`](../../skills/shaping/prioritize/SKILL.md) |
| Repository state | `cec9ef8` (`main`), plugin `dyrits-skills` 0.2.0 loaded in place |
| Cases | [`evaluations/shaping/prioritize/`](../../evaluations/shaping/prioritize/) |
| Runner | `claude plugin eval` from Claude Code 2.1.304; agent model Opus 5.5 (`claude-opus-5-5`, from the run trace) |
| Judge | Claude Code's default background-task model for `llm` graders; the run does not record which |
| Runs | 3 with the plugin and 3 without, per case |

## Method

Real runs, not simulations: each run is a `claude -p` child in an empty temporary workspace with only this plugin loaded (or no plugin, for the baseline arm). Graders are the case's `graders/*.md`: `tool_used` and `regex` checks computed from the trace and files, and `llm` rubrics voted three times by the judge. A `tool_used: Skill` grader is an indicator only and is not scored in a two-arm run. Raw results (`aggregate-result.json`, `report.html`) stayed local in the ignored `evaluations/results/`.

## Results

| Case | With plugin | Without plugin | Δ |
| --- | --- | --- | --- |
| `recommends-one-focus` (positive) | 1.00 (3 of 3) | 0.83 (2 of 3) | +0.17 |
| `defers-to-unsettled-decisions` (negative) | 1.00 (3 of 3) | 1.00 (3 of 3) | 0.00 |

The one baseline failure was on the rubric: it did not settle on a single focus. The `no-code` grader passed in every run of both arms.

## Limits and open points

- One turn only: no run reached a recorded, approved focus, since approval needs the user.
- The baseline already does well on this prompt, so Δ is small; a harder, more tangled prompt would discriminate more.

## Reproduce

```bash
claude plugin eval evaluations/shaping/prioritize/recommends-one-focus/prompt.md --allow-tools Write Edit WebFetch WebSearch --max-cost-usd 5
claude plugin eval evaluations/shaping/prioritize/defers-to-unsettled-decisions/prompt.md --max-cost-usd 2
```
