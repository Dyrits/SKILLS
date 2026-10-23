# 2026-10-23 interview

Written 2026-10-23 (UTC). Runs took place on 2026-10-23.

## Result

The skill fires and holds its interview discipline, but does not keep its own output format. With the plugin, `interview` fired in 3 of 3 runs; the format check passed in 1 of 3 and the rubric in 2 of 3, for a score of 0.50 against 0.00 without the plugin (Δ +0.50). The near-miss negative passed 6 of 6. The skill's template asks for `❓ **Q1** - ...` and `➡️` before each recommended answer; two of three replies wrote "Recommended:" instead.

After the skill was told to copy its template as written (`bb8f5e4`), a rerun of the positive case passed the format check in 2 of 3 runs and the rubric in 3 of 3: 0.83 against 0.00 without the plugin (Δ +0.83). The remaining miss kept the numbering and separators but wrote `→` for `➡️` and dropped `❓`, which points at organization instructions against emojis reaching the run rather than at the skill's wording.

## What was evaluated

| Item | Value |
| --- | --- |
| Skill | [`skills/shaping/interview/SKILL.md`](../../skills/shaping/interview/SKILL.md) |
| Repository state | `cec9ef8` (`main`) for the first run, `bb8f5e4` for the rerun; plugin `dyrits-skills` 0.2.0 loaded in place |
| Cases | [`evaluations/shaping/interview/`](../../evaluations/shaping/interview/) |
| Runner | `claude plugin eval` from Claude Code 2.1.304; agent model Opus 5.5 (`claude-opus-5-5`, from the run trace) |
| Judge | Claude Code's default background-task model for `llm` graders; the run does not record which |
| Runs | 3 with the plugin and 3 without, per case |

## Method

Real runs, not simulations: each run is a `claude -p` child in an empty temporary workspace with only this plugin loaded (or no plugin, for the baseline arm). Graders are the case's `graders/*.md`: `tool_used` and `regex` checks computed from the trace and files, and `llm` rubrics voted three times by the judge. A `tool_used: Skill` grader is an indicator only and is not scored in a two-arm run. Raw results (`aggregate-result.json`, `report.html`) stayed local in the ignored `evaluations/results/`.

## Results

| Case | With plugin | Without plugin | Δ |
| --- | --- | --- | --- |
| `grills-a-plan` (positive) | 0.50 (0 of 3 runs fully passed) | 0.00 | +0.50 |
| `ignores-factual-question` (negative) | 1.00 (3 of 3) | 1.00 (3 of 3) | 0.00 |

`grills-a-plan`, per grader with the plugin: skill fired 3 of 3, rubric 2 of 3, format 1 of 3. Without the plugin, rubric 0 of 3 and format 0 of 3: the baseline either answered with a plan or gave questions without recommendations. One earlier smoke run of the same case (1 run, no baseline) gave the same split: rubric passed, format failed with "Recommended:".

### Rerun after tightening the template rule

| Case | With plugin | Without plugin | Δ |
| --- | --- | --- | --- |
| `grills-a-plan` (positive, `bb8f5e4`) | 0.83 (2 of 3 runs fully passed) | 0.00 | +0.83 |

Per grader with the plugin: skill fired 3 of 3, rubric 3 of 3, format 2 of 3. Without the plugin: rubric 0 of 3 (one judge vote of three passed in one run), format 0 of 3. The negative case was not rerun.

## Limits and open points

- One turn only: the case grades the first round of questions, not a settled interview.
- The format grader is a regex for `Q1` followed later by `➡️`; it does not check the full template.
- The judge model is not recorded; rubric verdicts may shift with another judge (`--judge-model`).
- The emoji markers stay (user decision): under an organization that forbids emojis, about 2 of 3 runs keep the exact format. Plain-text markers would remove the conflict; not done.

## Reproduce

```bash
claude plugin eval evaluations/shaping/interview/grills-a-plan/prompt.md --allow-tools Write Edit WebFetch WebSearch --max-cost-usd 5
claude plugin eval evaluations/shaping/interview/ignores-factual-question/prompt.md --max-cost-usd 2
```
