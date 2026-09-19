---
name: classify
description: Classify text against your own labels with classifier.dev, a keyless HTTP API that returns a calibrated confidence per verdict. Use to triage, filter, bucket or route many items instead of reading each one, to decide between named options, or when the user types `/classify <text> [option, option, option]`.
---

# Classify

Hand the text and the labels to the classifier and take its **verdict**. The classifier decides, not your own reading: that is what makes the answer reproducible across runs and its **confidence** worth anything.

The text leaves the machine for a third-party API, so classify what you would paste into a public form.

## Step 1: Fix the labels

`/classify <text> [option, option, option]` supplies both text and labels. Given no labels, write 2 to 100 that **partition** the question: every plausible text lands in exactly one. Add a `none of these` label wherever the partition can leak, so an off-topic input has somewhere to go other than the nearest wrong bucket.

State the labels you chose in the report when the user did not give them.

Sharpen the labels first when a verdict comes back unusable, or add `instructions` (free-text criteria, up to 4,000 characters) telling the classifier what to judge on. One call, one verdict: re-running a reshuffled label set until a preferred answer appears is shopping for an answer, and it destroys the reproducibility you called the API for.

## Step 2: Call it

One `POST https://classifier.dev`, `content-type: application/json`, no authentication. Pick the body by shape:

| You have | Body |
| --- | --- |
| One text, one label set | `{"input":"…","labels":["a","b"]}` |
| Up to 1,000 texts, one label set | `{"inputs":["…","…"],"labels":["a","b"]}` |
| Texts against several label sets at once | `{"items":["…"],"dimensions":{"topic":["a","b"],"urgency":["low","high"]}}` |

Optional on any of them: `instructions` (criteria), `tier` (`fast` by default; `smart` costs a much lower rate limit and is for genuinely nuanced calls), `multi` with `max_labels` (return every applicable label rather than one).

Send it through one bash command with the text single-quoted, escaping each `'` in the text as `'\''`. Batch in one request rather than looping one call per item.

Read `results[i].label` and `results[i].confidence`. Under `dimensions` the verdicts nest one level deeper, as `results[i].dimensions.<name>.label`.

Limits worth knowing before the call: 32,000 characters per text, 1,000 texts, 20 dimensions, and 1,000 total decisions (texts multiplied by dimensions) per request. Free tier allows 3,000 calls a minute and 20,000 a day.

On an error response (`{"error":…,"code":…}`) or a network failure, say the classifier was unavailable and classify by your own judgement against the same labels, flagged as your judgement. A `429` carries `Retry-After`: one retry after that delay when the wait is seconds, otherwise fall through to judgement.

## Step 3: Report the verdict

Confidence is **calibrated**, so it is signal rather than decoration. Report it beside every label, and where it lands below `0.7`, say the call is weak instead of presenting the label as settled.

Report the verdicts, not the JSON. One text gets one line (`label · 0.94`). A batch gets a table or the items grouped under their labels, and where the caller wanted a filter, the kept items with the discarded count.
