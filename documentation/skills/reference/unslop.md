Source: Cursor's pstack `unslop` skill, adopted in commit `6585eba`. This fork extends the editing pass to the source language.

## What it does

`/unslop` edits writing in any language to remove patterns that make it sound AI-generated. It preserves the meaning and intended tone, then rereads the revision once for patterns that remain.

## When to reach for it

Type `/unslop`, or the agent reaches for it before it shows or publishes a draft that other people will read: a message, a post, a caption, interface text, an announcement, or documentation. It applies to drafts that already seem polished too. It does not run on the agent's ordinary replies to you.

## The editing pass

The skill checks content, wording, style, filler, and vague claims. It replaces a pattern only when the revision says the same thing more plainly. A concrete fact or instruction is better than a general phrase that could fit any document.

## Common questions

**Does it change the point I am making?**
It should preserve the point and the intended tone. Review any revision that changes a technical claim or removes a useful distinction.

**Does it override my project's style rules?**
No. Where your steering file or style guide sets a writing rule (for example, which punctuation replaces an em dash), the skill follows that rule over its own pattern.

**Does it work outside English?**
Yes. The examples in the skill are English, but the editing pass follows the source language and applies each pattern by meaning rather than translating the examples.

## It's working if

- The revised text makes the same claims in plainer words.
- Vague claims become specific or disappear.
- The draft reads naturally without stock phrases or decorative structure.

## Where it fits

This is a standalone editing pass for any draft. [Write for agents](write-for-agents.md) guides the structure of instructions agents read; `/unslop` edits the prose itself. [Guide](../productivity/guide.md) maps the full skill set.
