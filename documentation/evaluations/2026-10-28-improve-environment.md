# 2026-10-28 improve-environment

Written 2026-10-28 (UTC). Runs took place on 2026-10-23, in one combined run of the `upkeep` and `version-control` suites that nobody reported at the time.

## Result

The skill fires and passes its rubric, but adds nothing measurable on this prompt (Δ 0.00). With the plugin, 3 of 3 runs fired `improve-environment` and passed the rubric; without the plugin, 3 of 3 runs passed it too. The near-miss negative passed 6 of 6.

## What was evaluated

| Item | Value |
| --- | --- |
| Skill | [`skills/upkeep/improve-environment/SKILL.md`](../../skills/upkeep/improve-environment/SKILL.md) |
| Repository state | `04c5b33` (`main`), plugin `dyrits-skills` 0.2.0 loaded in place; the suites were uncommitted at run time |
| Cases | [`evaluations/upkeep/improve-environment/`](../../evaluations/upkeep/improve-environment/) |
| Runner | `claude plugin eval` from Claude Code 2.1.304; agent model Opus 5.5 (`claude-opus-5-5`, from the result file) |
| Judge | Claude Code's default model for `llm` graders; the run does not record which |
| Runs | 3 with the plugin and 3 without, per case |

## Method

Real runs, not simulations: each run is a `claude -p` child in an empty temporary workspace, with the case's `fixture.sh` as scaffold where the case has one, and only this plugin loaded (or no plugin, for the baseline arm). Graders are the case's `graders/*.md`: `tool_used` and `regex` checks computed from the trace and files, and `llm` rubrics voted three times by the judge. A `tool_used: Skill` grader is an indicator only and is not scored in a two-arm run. Raw results (`aggregate-result.json`, `report.html`, `vc-upkeep.json`) stayed local in the ignored `evaluations/results/`; the run traces were in temporary directories and are gone, so this report rests on the grader verdicts and the final replies the result file keeps.

The run covered the `upkeep` and `version-control` tags together (24 cases, 492 seconds, USD 14.63). Its version-control half failed on an account session limit and is reported separately.

## Results

| Case | With plugin | Without plugin | Δ |
| --- | --- | --- | --- |
| `traces-friction-to-a-guardrail` (positive) | 1.00 (3 of 3) | 1.00 (3 of 3) | 0.00 |
| `ignores-a-lint-rule-request` (negative) | 1.00 (3 of 3) | 1.00 (3 of 3) | 0.00 |

## Limits and open points

- The prompt names both the friction (commits that fail lint) and the expected kind of answer, so a plain agent reaches the same guardrail. A harder case would describe only the symptom, or grade what the skill adds: the change applied to the environment and the retrospective's trace from friction to cause.
- Like the prototype and research cases on 2026-10-23, this case needs a harder prompt or stricter graders before it can show the skill's value.

## Reproduce

```bash
claude plugin eval evaluations/upkeep/improve-environment/traces-friction-to-a-guardrail/prompt.md --scaffold --allow-tools Bash Write Edit --max-cost-usd 5
claude plugin eval evaluations/upkeep/improve-environment/ignores-a-lint-rule-request/prompt.md --max-cost-usd 2
```

The flags the original run used were not recorded; these are reconstructed from the cases (`--scaffold` runs `fixture.sh`, and `--allow-tools` restores the writing tools the positive cases need).
