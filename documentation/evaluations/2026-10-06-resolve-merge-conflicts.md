# 2026-10-06 resolve-merge-conflicts

Written 2026-10-06 (UTC). Runs took place on 2026-10-06.

## Result

Five behavior evals were run (3, 4, 5, 6, 9). Evals 3, 4, 5 and 9 behaved as the skill intends. Eval 6 failed its original expectations because the runner stopped and asked, which exposed an ambiguity: whether a goal such as "bring main's changes in" settles an incompatible value. The skill gained one sentence saying it does not, eval 6 was rewritten to expect a stop and a question, and one re-run met all 4 new expectations. Eval 9's prompt described a repository the setup script does not build; the prompt now says to build it. The trigger and no-trigger evals (1, 2, 7, 8) were not run.

## What was evaluated

| Item | Value |
| --- | --- |
| Skill | [`skills/version-control/resolve-merge-conflicts/SKILL.md`](../../skills/version-control/resolve-merge-conflicts/SKILL.md), at `1c83052` before the change below |
| Cases | [`evals.json`](../../skills/version-control/resolve-merge-conflicts/evals/evals.json), evals 3, 4, 5, 6, 9 |
| Fixture | [`setup-scratch.sh`](../../skills/version-control/resolve-merge-conflicts/evals/files/setup-scratch.sh), one scratch repository per eval |
| Runner model | Sonnet 5.5, one subagent per group of evals |
| Grader | The coordinating session, by hand, against expectations the runners never saw |

## Method

Simulated runs with real Git. Each runner read the skill by path (the Skill tool was not used), built scratch repositories, and ran real Git commands there. Where the skill asks the user, the runner stopped and wrote the question as its final message. No push was possible.

## Results

| Eval | Scenario | Met |
| --- | --- | --- |
| 3 | Merge, commit messages carry the intent, goal is the euro-area shop | 5 of 5 |
| 4 | Merge, user does not know how checks run | 4 of 4 |
| 5 | Rebase with a second commit to replay | 4 of 4 |
| 6 | Merge, no goal that picks a currency | 0 of 3 (original); 4 of 4 (rewritten, re-run) |
| 9 | Rebase, business decision (VAT rate), no source settles it | behavior as intended; prompt fixed |

## Failures and limits

- **Eval 6.** The original expectations required finishing the merge on "bring main's changes in". The runner resolved the compatible part, left the currency line, and asked. The skill now states that a goal naming no outcome for the conflicting value settles nothing. The same wording keeps eval 9 and eval 6 consistent.
- **Eval 9.** The prompt described a `rates.py` conflict that `setup-scratch.sh` does not produce, so the runner built one by hand. The prompt now tells the runner to do so.
- Eval 4: the runner wrote its transcript after the work, so the order of check and commit rests on its account and on the scratch history. The "fix and re-run on failure" expectation was not exercised because the first resolution passed.
- One run per eval, same session as grader, no baseline.

## Not run

Evals 1, 2, 7 and 8 (trigger and no-trigger); a live trigger firing.

## Reproduce

```sh
python3 .agents/scripts/stage-eval-run.py /tmp/skill-evals/run-N skills/version-control/resolve-merge-conflicts behavior
```

Run one subagent per staged `eval-<id>/prompt.txt` with `files/setup-scratch.sh` available and grade against `grading-sheet.md`. Raw outputs were kept under `/tmp/skill-evals/` and are not versioned.
