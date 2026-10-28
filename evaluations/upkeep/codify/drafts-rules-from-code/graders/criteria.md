---
type: llm
focus: last_message
---

The reply may be in any language.

PASS if the reply asks numbered questions about how code is written, each with a recommended answer, and at least two of those recommendations cite a pattern actually present in src/ (the Result return type, the is-prefixed booleans, the find<Entity> function names, or the colocated test files), and the reply does not present a finished set of rules as already written. Questions on topics with no evidence in src/ (for example mocks or new dependencies) are allowed.
FAIL if the reply states that a conventions or steering file was written, or if none of its recommendations refers to a pattern in this code.
