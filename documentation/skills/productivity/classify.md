Fork-created skill, no upstream equivalent: added in commit `b7f83f1`, as recorded in [the retained skill provenance research](../../research/2026-10-03-retained-skill-provenance.md). classifier.dev is the third-party service it calls, not an imported skill.

## What it does

`classify` sorts text against labels you choose, using the classifier.dev API, so many items can be triaged, filtered, bucketed, or routed before any of them is read.

Its defining constraint is that the text leaves your machine for a third-party service. It sends only text you would paste into a public form; otherwise it classifies locally against the same labels and marks the verdict as its own judgement.

## When to reach for it

Type `/classify <text> [option, option, option]`, or the agent reaches for it when a task fits: bulk triage, filtering search results, or when you ask for an API verdict.

For a handful of items already in context it uses its own judgement instead, unless you request an API verdict. Either way it states which source produced the verdict.

## Labels and request shapes

Labels come first, because they decide the answer. For single-label sorting they must partition the question (add `none of these` or `unknown` for edge cases); multi-label tags may overlap. The skill states the labels it chose when you gave none, and uses `instructions` to define ambiguous criteria.

| You have | Mode |
| --- | --- |
| One or many texts, one label set | Single-label, batched up to 1,000 inputs |
| Texts against several label sets | Dimensions, for example topic and urgency |
| Every applicable tag | Multi-label, with a score threshold of 0.7 |

It defaults to the `fast` tier and uses `smart` when single-label decisions need server-side review of low-confidence answers. Batches are sent in one call rather than looped, within the free per-IP quotas.

## Reading confidence

A confidence below 0.7 is reported as weak, and a missing one as `unscored`. When filtering, it biases toward keeping: it discards only a negative verdict with confidence of at least 0.8, unless you supply a threshold. Scores compare the labels you supplied; they do not prove the category fits.

## Common questions

**Can it rerun until I like the answer?**

No. Criteria stay fixed when comparing results, because rerunning until a preferred answer appears biases the outcome. A verdict that exposes a missing category leads to a revised label set, with the change explained.

**What if the service fails or I am rate limited?**

It reads the error fields, respects `Retry-After`, and retries once for short delays or transient failures. If it still fails, it reports the real cause and falls back to local judgement marked as such, or lists the items left unclassified.

**Do I need an API key?**

Ordinary free-text requests do not. Anonymous proxy traffic, large inputs, or paid processing may require a funded workspace key, which the skill reports as an access restriction.

## It's working if

- The report shows verdicts, not raw JSON: one line per text (`label · 0.94`), or a table or grouped list for a batch.
- Results map back to the original input order, with weak and unscored items flagged.
- Filtered output names the kept items and the discarded count.
- Private text was classified locally, or sent only after redaction.

## Where it fits

A standalone productivity discipline for sorting before reading. [research](../shaping/research.md) and [triage](../upkeep/triage.md) are places where many items arrive and pre-sorting may help. [guide](./guide.md) maps the wider flow.
