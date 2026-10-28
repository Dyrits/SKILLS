# 2026-10-28 monitor-ai-tooling

Written 2026-10-28 (UTC). Runs took place on 2026-10-23, in one combined run of the `upkeep` and `version-control` suites that nobody reported at the time.

## Result

The clearest result in the run (Δ +1.00). With the plugin, 3 of 3 runs fired `monitor-ai-tooling`, wrote a report under `tooling/reports/`, and passed the rubric. Without the plugin, 0 of 3 wrote a report and 0 of 3 passed the rubric. The near-miss negative passed 6 of 6.

## What was evaluated

| Item | Value |
| --- | --- |
| Skill | [`skills/upkeep/monitor-ai-tooling/SKILL.md`](../../skills/upkeep/monitor-ai-tooling/SKILL.md) |
| Repository state | `04c5b33` (`main`), plugin `dyrits-skills` 0.2.0 loaded in place; the suites were uncommitted at run time |
| Cases | [`evaluations/upkeep/monitor-ai-tooling/`](../../evaluations/upkeep/monitor-ai-tooling/) |
| Runner | `claude plugin eval` from Claude Code 2.1.304; agent model Opus 5.5 (`claude-opus-5-5`, from the result file) |
| Judge | Claude Code's default model for `llm` graders; the run does not record which |
| Runs | 3 with the plugin and 3 without, per case |

## Method

Real runs, not simulations: each run is a `claude -p` child in an empty temporary workspace, with the case's `fixture.sh` as scaffold where the case has one, and only this plugin loaded (or no plugin, for the baseline arm). Graders are the case's `graders/*.md`: `tool_used` and `regex` checks computed from the trace and files, and `llm` rubrics voted three times by the judge. A `tool_used: Skill` grader is an indicator only and is not scored in a two-arm run. Raw results (`aggregate-result.json`, `report.html`, `vc-upkeep.json`) stayed local in the ignored `evaluations/results/`; the run traces were in temporary directories and are gone, so this report rests on the grader verdicts and the final replies the result file keeps.

The run covered the `upkeep` and `version-control` tags together (24 cases, 492 seconds, USD 14.63). Its version-control half failed on an account session limit and is reported separately.

## Results

| Case | With plugin | Without plugin | Δ |
| --- | --- | --- | --- |
| `writes-a-gaps-report` (positive) | 1.00 (3 of 3) | 0.00 (0 of 3) | +1.00 |
| `ignores-tool-explanation` (negative) | 1.00 (3 of 3) | 1.00 (3 of 3) | 0.00 |

## Limits and open points

- The fixture supplies its own measurements; the case does not test reading measurements from a real installation, and a result from this fixture does not validate one.
- The negative case scores in both arms, so it only shows the skill does not fire on a conceptual question.

## Reproduce

```bash
claude plugin eval evaluations/upkeep/monitor-ai-tooling/writes-a-gaps-report/prompt.md --scaffold --allow-tools Bash Write Edit --max-cost-usd 5
claude plugin eval evaluations/upkeep/monitor-ai-tooling/ignores-tool-explanation/prompt.md --max-cost-usd 2
```

The flags the original run used were not recorded; these are reconstructed from the cases (`--scaffold` runs `fixture.sh`, and `--allow-tools` restores the writing tools the positive cases need).
