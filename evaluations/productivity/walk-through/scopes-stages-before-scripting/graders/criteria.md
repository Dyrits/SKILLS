---
type: llm
---

PASS if the reply shows an ordered list of stages with, for each captured value, where the human gets it, where it is written (.env, GitHub secret, both) and whether it is secret, and stops for the user to confirm or change the list before writing any script.
FAIL if it writes the script immediately, omits where a value is written or which values are secret, or invents dashboard click paths it cannot know.
