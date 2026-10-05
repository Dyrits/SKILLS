Upstream source: `wait-what`, verified in the `d81f3a1` tree. This fork names the action `re-explain`; the old name is not an alias.

## What it does

`re-explain` asks the agent to explain again when you stopped following. It adds the missing premise, uses your project's vocabulary, and answers in the language you have been using. It repairs understanding rather than shortening the message until important context disappears.

## When to reach for it

Type `/re-explain`, or an agent or another skill can reach for it when the task fits. You are usually the one who knows when an explanation stopped making sense.

Use it when the agent invents jargon, stacks acronyms, or explains a decision without its premise. For an unresolved decision that needs discussion rather than another explanation, use [refine](../reference/refine.md).

## Explain again, not just less

"Be concise" can produce clipped sentences that are shorter and harder to understand. **Re-explain** asks for the context you need as well as simpler wording. What lost you may span several paragraphs, so the skill lets the agent go back far enough to restore the premise.

The glossary supplies the nouns. ASD-STE100 Simplified Technical English supplies the register when the answer is in English. Other languages keep the same plain-technical intent in their own idiom.

## Common questions

**Does it work without a glossary?**

Yes. Without `GLOSSARY.md`, or a `GLOSSARY-MAP.md` pointing to the relevant glossary, it uses plain simplified language. You lose the domain-vocabulary guidance, not the explanation.

**Where did `/wait-what` go?**

This fork renamed it to `/re-explain`. Update saved prompts and wrappers; there is no old-name alias. The job remains restoring understanding, not producing a terse summary.

**Does it always answer in English?**

No. It follows the language you have been using and asks when the preference is unclear. Simplified Technical English applies only to English answers.

## It's working if

- The new explanation is clearer, not merely shorter.
- It adds the premise you were missing.
- Project nouns replace invented jargon.
- Asking again does not degrade the answer into terse fragments.

## Where it fits

`re-explain` is a reach-for-it-anytime standalone inside any conversation. [model-domain](../reference/model-domain.md) prevents vocabulary drift by maintaining the shared language; this skill repairs an explanation after it failed. [illustrate](./illustrate.md) is another option when a visual would make the relationship clearer. [guide](./guide.md) helps you choose the next move.
