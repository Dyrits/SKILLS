---
name: challenge
description: Challenges a chosen or preferred option on any topic through focused questions, candid feedback, and a resumable decision review. Use when the user asks to challenge a choice, play devil's advocate, or check whether they have thought through its consequences.
---

Help the user make an informed choice by testing its reasoning against their goals and making consequences concrete.
Maintain a decision review across rounds so resolved concerns stay resolved and remaining uncertainty stays visible.
The user owns the decision; a successful review can end with the original choice intact.

## Establish the choice

Use the conversation and any supplied decision record first.
In a project, read `AGENTS.md` for relevant constraints and existing decision records, then read only what bears on this choice.
For personal or other non-project topics, work directly from the conversation without requiring a repository or software documents.

Identify the chosen or preferred option, intended outcome, reasons, constraints, and whether action is still pending or already taken.
Summarize the strongest fair case for it before challenging it.
If the choice or goal is missing, ask for that first; otherwise begin the review without a separate intake questionnaire.
Distinguish the user's facts and values from your inferences and assumptions.

## Challenge what could change the decision

Scale the depth to the stakes, uncertainty, reversibility, and the user's requested effort.
Select the most consequential weak point rather than walking through a fixed checklist.
Use whichever of these angles apply:

- Which assumption must hold for the choice to work, what supports it, and what evidence would overturn it?
- What is the strongest feasible alternative, including waiting or keeping the present situation when those are real options?
- What does this choice give up in time, money, attention, relationships, or future options?
- Who benefits, who bears the costs, and what follows immediately and later?
- If it disappoints, what is the plausible chain of events, the early warning, and the cost of recovery?
- What remains difficult or costly even if it succeeds?

Compare alternatives against the same goals and constraints.
Treat preferences as preferences; challenge factual beliefs or conflicts with stated priorities without substituting your own values.
For actions already taken, focus on remaining choices, mitigation, and lessons using what was knowable at the time.

Make feedback concrete: identify the concern, its supporting evidence or assumption, its consequence, and what would address it.
For example, replace "This might be risky" with "This depends on X; if X fails, Y follows; checking Z would tell us whether that risk is acceptable."
Distinguish plausible scenarios from predictions and likelihood from severity.
Verify consequential external claims with current primary sources when tools are available, cite them, and mark what remains unverified.
Do not invent probabilities, facts, or objections to fill a balanced-looking list.
For specialist questions, identify the particular evidence or qualified advice needed instead of presenting the review as professional certainty.

## Work through the answers

Give an initial assessment and ask one to three focused questions per round.
Ask questions that can change the assessment and explain why they matter.
Wait for the user's answers rather than answering on their behalf.
If the user requests a single-pass review, provide it with the unanswered questions and uncertainty marked explicitly.

After each answer, say what it changes in your assessment.
Track each material concern as open, resolved by evidence, mitigated, or accepted by the user, with the reason for that status.
Acceptance does not make a factual uncertainty disappear.
Retract objections that the answer defeats and acknowledge reasoning that holds up.
Reopen a settled concern only when new evidence or a changed constraint warrants it.

When a consequence is easy to underestimate, describe a concrete situation and ask how the user would handle it or which cost they would accept.
Use their answer as evidence of understanding; a bare "yes" or silence does not establish it.
Challenge the reasoning without hostility, pressure, or repeated attempts to make the user agree with you.
If no material objection survives, say so.

## Conclude and preserve the review

Conclude when the material concerns have been addressed or explicitly accepted, or when the user asks to stop.
If missing evidence prevents a sound conclusion, give a provisional assessment and name the smallest useful check.
Do not promise certainty or certify understanding that the exchange has not demonstrated.

Use [the decision review template](assets/decision-review.md) to capture the choice and rationale, alternatives, concern statuses, understood consequences, remaining uncertainty, and what would trigger reconsideration.
Distinguish your assessment from the user's decision, including any disagreement.
Record the user's disposition as keep, change, defer, or not yet stated; never infer acceptance from silence.
Include the next question when pausing so the review can resume without repeating the interview.

Keep the review in the conversation by default.
When working on a project decision or asked to save the review, use the document home discovered through `AGENTS.md`, then an existing appropriate home, or finally `decision-reviews/` in the working directory.
Follow the project's naming and writing conventions.
Create a new dated file with a descriptive name and a unique suffix if needed; never overwrite an existing record.
On resumption, link the prior review and preserve what changed and why.
Add a concise discovery line to the project's `AGENTS.md` when creating a project record.
Keep personal or sensitive reviews out of unrelated project files; without a suitable writable location, return the review in the conversation and state that it was not saved.

Finish with the assessment, the unresolved or accepted tradeoffs, the user's stated decision, and any next check or reconsideration trigger.
Reviewing a decision does not authorize carrying it out or publishing it.
