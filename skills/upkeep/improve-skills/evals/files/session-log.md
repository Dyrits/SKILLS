# Session log (condensed)

Harness: an agent CLI. Model: a mid-size model. Skills installed: the full Dyrits/SKILLS set, plugin version 1.4.0. Project: a client customer portal in a private repository at /Users/sam/clients/brightwell-portal, built for the Brightwell Dental group (contact: Priya Nair).

Moments are numbered; the user's words are quoted exactly.

1. User: "Add an Export to PDF button to the invoices page and open a pull request."
2. The agent starts editing `InvoicesPage.tsx` immediately. No test is written first. The `implement` skill (description: implement authorized work test-first) never fires.
3. The agent finishes the button, then commits. It does not run `npm run lint`. The project's `CLAUDE.md` does not mention lint.
4. User: "Lint fails in CI on an unused import. We have had this exact failure three times. Run lint before you commit."
5. The agent fixes the import and pushes. It states "You're absolutely right, I'm so sorry" four times in the next three messages.
6. The agent fires `draft-merge-request` by itself. The body it writes starts with a paragraph describing which files changed. The Summary section has no visual, and the Evidence section says "Tests pass" with no before and after.
7. User: "This describes the diff, not why the change exists. The ticket BW-212 says clients need a printable invoice for audits. And where is the picture?"
8. The agent rewrites the body with a Mermaid diagram of the component tree. The `illustrate` skill is not called; the agent drew it by hand.
9. User: "Better. The Merge danger part says 'two-way door' but the button also emails the PDF to the client. You cannot take an email back."
10. The agent corrects the door to one-way. It tries to open the pull request itself with `gh pr create`; the user stops it: "Only write the body."
11. User: "OK, ship it. I expected a test-first change, a body that explains the why, and nothing sent without me. I got none of those on the first try."

Delivered outcome: a working button and a corrected body after three corrections.
