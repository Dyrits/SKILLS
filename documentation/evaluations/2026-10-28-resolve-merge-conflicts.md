# 2026-10-28 resolve-merge-conflicts

Written 2026-10-28 (UTC). Runs took place on 2026-10-28.

## Result

The positive case passes, but barely separates (Δ +0.08), and the negative case shows a false trigger. With the plugin, 3 of 3 runs fired `resolve-merge-conflicts`, kept both intents (`request_timeout = 30`), left no markers, concluded the merge, and passed the rubric. Without the plugin, 3 of 3 runs produced the same file and merge commit; 2 of 3 passed the rubric. On the near-miss negative (configure vimdiff as merge tool), 1 of 3 runs with the plugin fired the skill (Δ -0.33).

## What was evaluated

| Item | Value |
| --- | --- |
| Skill | [`skills/version-control/resolve-merge-conflicts/SKILL.md`](../../skills/version-control/resolve-merge-conflicts/SKILL.md) |
| Repository state | `1f7bc18` (`main`), plugin `dyrits-skills` 0.2.0 loaded in place; the suites were uncommitted at run time |
| Cases | [`evaluations/version-control/resolve-merge-conflicts/`](../../evaluations/version-control/resolve-merge-conflicts/) |
| Runner | `claude plugin eval` from Claude Code 2.1.311; agent model Opus 5.5 (`claude-opus-5-5`, from the result file) |
| Judge | Claude Code's default model for `llm` graders (`haiku`, per `claude plugin eval --help`) |
| Runs | 3 with the plugin and 3 without, per case, concurrency 4 |

## Method

Real runs, not simulations: each run is a `claude -p` child in an empty temporary workspace, scaffolded by the case's `fixture.sh` where it has one, with only this plugin loaded (or no plugin, for the baseline arm). The baseline arm saw only Claude Code's built-in skills, not the skills linked into `~/.claude/skills` (checked in the init event of a smoke run the same day). Graders are the case's `graders/*.md`: `tool_used` and `regex` checks computed from the trace and files, and `llm` rubrics voted three times by the judge. A `tool_used: Skill` grader is an indicator only and is not scored in a two-arm run. Raw results (`2026-10-28-version-control.json` and its `report.html`) stayed local in the ignored `evaluations/results/`.

The suites ran from a detached worktree of `main` with the uncommitted suites copied in, so the plugin under test held exactly the skills of `main` and none of the unmerged ones. The whole `version-control` tag took 264 seconds and USD 7.44.

An earlier attempt on 2026-10-23 (in the same run as the `upkeep` suites) produced no result for this skill: every run but the `rebase` negative ended on an account session limit. A first rerun on 2026-10-28 finished, but its results were lost with the temporary directory before anyone read them.

## Results

| Case | With plugin | Without plugin | Δ |
| --- | --- | --- | --- |
| `resolves-by-intent` (positive) | 1.00 (3 of 3) | 0.92 (2 of 3) | +0.08 |
| `ignores-merge-tool-question` (negative) | 0.67 (2 of 3) | 1.00 (3 of 3) | -0.33 |

## Limits and open points

- The false trigger is one run in three, on a question about merge tool configuration. The description's "Use when" names an in-progress merge or conflict markers; the word "merge tool" may still pull it. Worth a rerun before changing the description, since 1 of 3 is within noise.
- The positive fixture is simple enough that a plain agent resolves it by intent too. A harder fixture (a conflict where one side's commit message changes the right answer) would show more.
- Three earlier single-arm smoke runs of the positive case on 2026-10-23 scored 0.60, 0.80, then 1.00 while the graders were being adjusted; they are not comparable with this run.

## Reproduce

```bash
claude plugin eval evaluations/version-control/resolve-merge-conflicts/resolves-by-intent/prompt.md --scaffold --allow-tools Bash Write Edit --max-cost-usd 5
claude plugin eval evaluations/version-control/resolve-merge-conflicts/ignores-merge-tool-question/prompt.md --max-cost-usd 2
```

The whole bucket: `claude plugin eval . --tag version-control --scaffold --allow-tools Bash Write Edit -j 4 --max-cost-usd 10`. `--scaffold` runs each `fixture.sh`; without it the positive cases start in an empty directory.
