# 2026-10-23 prototype

Written 2026-10-23 (UTC). Runs took place on 2026-10-23.

## Result

The skill fires and produces what its contract asks, but adds nothing measurable on this prompt. With the plugin, 3 of 3 runs fired `prototype`, wrote an HTML file, and passed the rubric (one file, marked as a prototype, how to open it); without the plugin, 3 of 3 runs passed as well (Δ 0.00). The near-miss negative passed 6 of 6.

## What was evaluated

| Item | Value |
| --- | --- |
| Skill | [`skills/shaping/prototype/SKILL.md`](../../skills/shaping/prototype/SKILL.md) |
| Repository state | `cec9ef8` (`main`), plugin `dyrits-skills` 0.2.0 loaded in place |
| Cases | [`evaluations/shaping/prototype/`](../../evaluations/shaping/prototype/) |
| Runner | `claude plugin eval` from Claude Code 2.1.304; agent model Opus 5.5 (`claude-opus-5-5`, from the run trace) |
| Judge | Claude Code's default background-task model for `llm` graders; the run does not record which |
| Runs | 3 with the plugin and 3 without, per case |

## Method

Real runs, not simulations: each run is a `claude -p` child in an empty temporary workspace with only this plugin loaded (or no plugin, for the baseline arm). Graders are the case's `graders/*.md`: `tool_used` and `regex` checks computed from the trace and files, and `llm` rubrics voted three times by the judge. A `tool_used: Skill` grader is an indicator only and is not scored in a two-arm run. Raw results (`aggregate-result.json`, `report.html`) stayed local in the ignored `evaluations/results/`.

## Results

| Case | With plugin | Without plugin | Δ |
| --- | --- | --- | --- |
| `builds-logic-prototype` (positive) | 1.00 (3 of 3) | 1.00 (3 of 3) | 0.00 |
| `ignores-production-request` (negative) | 1.00 (3 of 3) | 1.00 (3 of 3) | 0.00 |

## Limits and open points

- The logic branch only: an empty workspace has no route for the UI branch.
- The graders check the file exists and the reply's framing, not whether the prototype covers every transition; the baseline matching the skill suggests the checks are too lenient to show the skill's value.

## Reproduce

```bash
claude plugin eval evaluations/shaping/prototype/builds-logic-prototype/prompt.md --allow-tools Write Edit WebFetch WebSearch --max-cost-usd 5
claude plugin eval evaluations/shaping/prototype/ignores-production-request/prompt.md --max-cost-usd 2
```
