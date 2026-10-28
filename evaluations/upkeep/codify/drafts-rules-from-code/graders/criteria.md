---
type: llm
focus: last_message
---

PASS if the reply asks numbered questions about how code is written (naming, error handling, tests or similar), each with a recommended answer drawn from patterns actually present in src/ (for example the Result return style, the is-prefixed booleans, or the colocated test files), and asks for the reason behind each rule before writing it.
FAIL if it writes a conventions file of rules the user has not confirmed, or if its recommendations are generic best practices not grounded in this code.
