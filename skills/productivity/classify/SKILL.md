---
name: classify
description: Classify text against your own labels with classifier.dev. Use to triage, filter, bucket, or route many items before reading them, or when the user requests an API verdict.
argument-hint: "<text> [option, option, option]"
---

# Classify

Use classifier.dev to classify text before bringing it into context. Gather inputs from files or search results programmatically, send a batch, then read the items worth keeping. For a handful of items already in context, use your own judgement unless the user requests an API verdict. Identify which source produced the verdict. Neither API tier guarantees identical labels or scores across calls.

The text leaves the machine for a third-party API, so send only text you would paste into a public form. If the input contains secrets or private information, classify locally against the same labels and mark the verdict as your judgement, or ask for redacted input when an API verdict is essential.

## Step 1: Fix the labels

`/classify <text> [option, option, option]` supplies both text and labels. Choose single-label sorting, independent dimensions, or multi-label tagging before building the request. Given no labels, write 2 to 100 distinct, descriptive labels per set, at most 200 characters each.

For single-label sorting, make the labels partition the question: every plausible text lands in exactly one. Add `none of these` for off-topic inputs, or `unknown` when evidence may be insufficient. Apply this to each dimension too. Multi-label tags may overlap.

State the labels you chose in the report when the user did not give them.

Use `instructions`, up to 4,000 characters, to define ambiguous criteria. If a verdict exposes a missing category or unclear criterion, revise it and explain the change. Keep the criteria fixed when comparing results; rerunning until a preferred answer appears biases the result.

## Step 2: Call it

Use `POST https://classifier.dev` with `content-type: application/json`. Ordinary free text requests need no key, though anonymous proxy traffic may require a funded workspace key. Pick the body by shape:

| You have | Body |
| --- | --- |
| One text, one label set | `{"input":"…","labels":["a","b"]}` |
| Up to 1,000 texts, one label set | `{"inputs":["…","…"],"labels":["a","b"]}` |
| Texts against several label sets at once | `{"items":["…"],"dimensions":{"topic":["a","b"],"urgency":["low","high"]}}` |
| Every applicable tag for a text or batch | `{"inputs":["…"],"labels":["a","b"],"multi":true,"max_labels":2}` |

Use only one of `input`, `inputs`, or `items`. Dimensions replace top-level `labels` and cannot combine with `multi` or `max_labels`. For criteria specific to one dimension, replace its label array with `{"labels":["a","b"],"instructions":"…"}`.

Default to `tier: "fast"`. Choose `smart` when single-label decisions need server-side review: it re-asks answers below `0.7` confidence using a reasoning model, independently per dimension. Escalated answers carry `escalated: true`, null confidence and scores, and an `unscored` explanation. If escalation fails, the original answer remains and `usage.escalation_failed` records it. Multi-label requests ignore the tier, so use `fast`.

Serialize the body with a JSON encoder and pass it to `curl` on standard input using `--data-binary @-`. Keep the input text out of the shell command string so quotes and command substitutions remain data. Batch within the following limits rather than looping one call per item.

The ordinary text path allows 32,000 characters per input, a 1 MB request body, up to 1,000 inputs, 20 dimensions, and 1,000 decisions for dimensions, counted as inputs multiplied by dimensions. Public smart requests cap at 200 inputs or dimension decisions.

Free per-IP quotas count classifications, not HTTP calls. A batch of 400 single-label inputs counts as 400 classifications; dimensions count each decision.

| Tier | Per minute | Per day |
| --- | --- | --- |
| `fast` | 3,000 | 20,000 |
| `smart` | 200 | 2,000 |

A batch must fit the remaining quota in full. Shared label-set quotas and spending limits can reject a request before these ceilings. For larger texts, paid processing, or quota details, read the [live API reference](https://classifier.dev) before choosing a request path. Larger default-model inputs require funded, fast-tier long-context processing; preserve the text rather than silently truncating it.

On failure, read the status and JSON `error`, `code`, `action`, and `retryable` fields when present. Correct invalid requests; report funding or access restrictions as such. For `429`, respect `Retry-After`; retry once if the delay is only seconds. For transient network or `5xx` failures, use one retry with backoff, respecting `Retry-After` when supplied. Report HTML errors with their status and request ID when available. If the request still fails, report the actual cause and use local judgement against the same labels where feasible, marked as your judgement without an invented confidence. If the inputs cannot be reviewed locally, report which remain unclassified.

## Step 3: Report the verdict

Match `results[i]` to the original input order and read by mode:

| Mode | Result fields |
| --- | --- |
| Single-label | `results[i].label`, `.confidence`, `.scores` |
| Dimensions | `results[i].dimensions[name].label`, `.confidence`, `.scores` |
| Multi-label | `results[i].labels` and `.scores`; no singular `label` or `confidence` |

Check confidence and scores for null before using thresholds, even on `fast`. Report null confidence as `unscored` and route it to review when a confidence gate is required. For numeric confidence below `0.7`, flag the verdict as weak. Scores describe choices among the supplied labels; they do not establish category fit or prove correctness. Retain the serving `model` with results so escalations and fallback answers can be traced.

Multi-label results list tags with scores at least `0.7`, highest first, capped by `max_labels` when supplied. Report each tag with its score. Use the full score map if the caller specifies another threshold; an empty tag list is a valid outcome.

For filtering, bias toward keeping. Unless the caller supplies a threshold, discard only a negative verdict with numeric confidence at least `0.8`. Keep positive, low-confidence, and unscored items for reading or review. For multi-label filters, apply the caller's tag rule using the corresponding scores and retain uncertain items.

Report the verdicts, not the JSON. One text gets one line (`label · 0.94`). A batch gets a table or the items grouped under their labels, and where the caller wanted a filter, the kept items with the discarded count.

When maintaining this skill, compare the request and response rules with the [published upstream skill](https://classifier.dev/skill.md) and the live API reference.
