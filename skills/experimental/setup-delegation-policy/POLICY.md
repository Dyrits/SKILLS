## Delegation and model routing

At the **top** of a fresh unit of engineering work, before reasoning about how to do it, decide how it gets done: here, by one subagent, split across independent subtasks, or here with a second agent reviewing the result. Reason first and the decision bends toward whatever you already started planning.

Keep it here when the turn builds on this window's context, when you are already inside a subagent, when the user named an agent or a skill, or when the turn is a question or a one-liner. A subagent inherits none of this conversation, only the briefing you write it, so a turn resting on a long window costs more to hand over than to finish here.

**If delegating, choose the least expensive model capable of completing the bounded task reliably.**

Match the work to a tier:

- **Light**: small, deterministic, well-scoped, verifiable. Renames, config tweaks, small fixes, test additions.
- **Balanced**: ordinary implementation, debugging, tests, specialized engineering work.
- **Heavy**: ambiguous requirements, architecture, cross-cutting changes, hard debugging, high-risk operations, final integration.
- **Frontier**: the hardest reasoning and the longest-horizon agentic runs, when the tier below has already fallen short or being wrong costs far more than the tokens do.

| Tier | Claude | Codex |
| --- | --- | --- |
| Light | Haiku | Luna |
| Balanced | Sonnet | Terra |
| Heavy | Opus | Sol |
| Frontier | Fable | Astra |

Read your delegation tool's parameter list this turn rather than assuming agent names or model controls: generations move and harnesses differ, so trust the choices it offers over the table. If a spawn tool offers a per-call model override, select the available model for the tier and pass its exact identifier. Otherwise pick the tier agent whose description matches. When no delegation tool is available, carry out the work here and name the tier the work would need if delegation becomes available.

Brief what you dispatch: the request verbatim, the working directory, whatever the request leans on without stating it (a path, a target file, a convention agreed earlier), and prior artifacts by path rather than pasted in full. A subagent left to guess any of these wastes the tier you just paid for.

State which agent and model handled dispatched work, before or alongside its result: name the tier, the resolved model or agent, and what it was asked to do. The user cannot see this otherwise, and cannot correct a wrong tier choice they never learned about.

Delegation earns its place when the subtask is bounded and its result is verifiable: weigh the briefing you have to write, the coordination and the verification you owe against what handing it over saves. Intent, task boundaries, tier choice, integration and final verification stay yours.
