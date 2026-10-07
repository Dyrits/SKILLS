---
name: improve-skills
description: "Hold a retrospective on a session, then report how the skills behaved as an issue on the skills repository. Use when the user asks to review skill use in a session or to report a skill problem."
metadata:
  forks: "mattpocock/skills/skills/engineering/retro"
argument-hint: "Optional: the session to review, and what you expected from it"
---

The user has asked for a **retrospective** on a session. Together you establish what went right, what went wrong, whether the skills were used correctly or used at all, and whether the outcome is the one expected. The findings about skills become an issue on the skills repository, [Dyrits/SKILLS](https://github.com/Dyrits/SKILLS), where they are fixed in a separate session.

## Steps

### 1. Reconstruct the session

Read the session the user names: a path, a session identifier, or a date in the local agent logs. Default to the current session. Build a timeline of:

- The user's goal and the outcome actually delivered.
- Every skill that ran, how it was reached (typed by the user, fired by the agent, called by another skill), and the steps it followed or skipped.
- Every point where a skill should plausibly have run and did not. Compare the work done with the descriptions of the installed skills.
- Corrections from the user, retries, detours, and expensive or repeated tool calls.

Completion: each skill that ran or should have run appears on the timeline with a pointer to the moment in the session.

### 2. Discuss it with the user

Hold the retrospective as a conversation, one question at a time, each opened with your own reading of the evidence for the user to confirm or correct. Cover:

- **Outcome**: what the user expected, and how the delivered result differs.
- **What went right**: behavior worth keeping, so a fix elsewhere does not break it.
- **What went wrong**: each difficulty, with the moment it happened.
- **Skill use**: for each skill on the timeline, whether it fired when it should, followed its own steps, and produced what it promises. Name the skill that was missing or misrouted, and the case no skill covers.

Quote the user faithfully. Keep what the evidence confirms apart from what is suspected, and label each suspected cause as a hypothesis.

Completion: the user has confirmed or corrected every finding, and the outcome question has an answer.

### 3. Sort the findings

Give each finding one home:

- **A skill finding**: a trigger that fired wrongly or never fired, an ambiguous or missing step, conflicting skills, a stale route in `guide`, a missing skill. These go into the issue.
- **A project lesson**: a convention, command, or rule of the project the session ran in. File it in the project following [LESSONS.md](LESSONS.md).
- **An environment finding**: friction a check, guardrail, navigation pointer, steering-file cut, tool, or access change would have prevented, including a mechanical violation a lint rule could catch. Once the issue is settled, list these findings for the user, each with its moment in the session and the environment change that would have prevented it.
- **Agent behavior neither a skill nor the environment could have steered**: report it to the user and leave it out of the issue.

Completion: every confirmed finding has exactly one home, and the user agrees with the sorting.

### 4. Draft the issue

Check open issues on the repository for the same problem first. When one exists, draft a comment on it instead of a new issue.

Write one issue for the retrospective in English, in GitHub Markdown:

- **Title**: the main skill problem, in a few words.
- **Context**: the harness, the model, the skills version (the plugin version, or the commit of the skills checkout when it can be found), and the kind of project.
- **Expected and actual outcome**.
- **Skills involved**: a table with each skill, how it was reached, and whether it behaved as intended, with evidence.
- **What went right**.
- **What went wrong**: one subsection per skill finding, with the evidence, the confirmed observation, the hypothesis, and a proposed correction when the evidence supports one.

The repository is public. Leave out private paths, code, client and colleague names, secrets, and anything else the user's project would not publish; describe it generically instead. Then remove AI language patterns from the draft following [UNSLOP.md](UNSLOP.md).

Completion: every skill finding from step 3 appears in the draft, and nothing in it identifies the private project.

### 5. Approve and open it

Show the repository, the title, the labels if any, and the exact body. Wait for explicit approval; after any revision, show the changed draft and ask again.

Open the issue through any route that can write issues on `Dyrits/SKILLS`, trying every available one before giving up; credentials already configured include the one git's credential helper stores for `https://github.com`, used without printing it. Read the issue back and report its URL.

When no option reaches GitHub, save the approved issue as a feedback record in `.agents/feedbacks/YYYY-MM-DD-<slug>.md`: the title as its heading, then the body. Put it in the skills checkout this skill was loaded from when it is one, otherwise in the current workspace. Tell the user where it is and which options failed.

On every run where GitHub is reachable, also check both locations for pending feedback records, offer to open each as an issue under the same approval, and delete each record once its issue is live.

Completion: the issue is live with the approved text and its URL is reported, or the approved text is saved as a feedback record and the user knows where.
