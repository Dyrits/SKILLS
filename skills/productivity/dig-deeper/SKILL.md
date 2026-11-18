---
name: dig-deeper
description: "Ask why, layer by layer, until bedrock. Use when the user wants to understand how or why unfamiliar code, a system, or a concept works, or asks to dig deeper, not stop at the surface, or run the five whys."
metadata:
  forks: "Tarektouati/skills/keep-digging"
---

Explain how something works by asking why of each answer until the next why would only repeat a definition. This builds understanding of a mechanism. It does not diagnose a failure, so a broken behavior the user wants fixed is out of scope.

Answer a trivial or already-understood fact directly, without a chain. Write in the language the user has been writing in.

## Process

1. Answer the first why from a real source. Read the code, configuration, documentation, or specification that governs the subject, and cite the file and line or the document section. When an earlier answer in the conversation already explains the subject, treat it as layer 1 and check it against its source.
2. Ask why of the layer you just wrote, and answer from a source again. Each layer goes one level more fundamental than the last: what it does, why it is built that way, which constraint or decision forced that, which upstream assumption the decision rests on.
3. Stop at bedrock. Bedrock is a hardware limit, an external contract, a documented tradeoff, or a principle the project states as given. Five layers is a guide: stop earlier when bedrock arrives earlier, continue past five when a layer still has a source-backed why, and never add a layer to reach five.
4. Mark a layer you cannot source as an assumption, say what would confirm it, and end the chain there. A short chain with a flagged gap is better than a plausible invented why.

The work is complete when every layer carries a source or an assumption flag and the last layer is bedrock or a flagged gap.

## Output

Show every layer. Stepping through them is how the reader learns, so do not collapse the chain into a summary.

```
1. [Observed behavior or surface fact] (source)
   why?
2. [Mechanism or immediate cause] (source)
   why?
3. [Decision or constraint behind the mechanism] (source)
   why?
4. [What the decision optimizes, or the assumption it rests on] (source)
   why?
5. [Bedrock] (source)
```

End with one plain sentence naming the root, the part worth remembering.
