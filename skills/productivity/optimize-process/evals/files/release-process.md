# Release sign-off, as it runs today (Harbor Lane team)

One real cycle, release 2026.14, week of 14 September.

| Step | Who | Active time | Waiting before the step |
| --- | --- | --- | --- |
| Developer finishes the last merge and tags a release candidate | Developer | 10 min | none |
| Developer writes release notes by hand from merged pull requests | Developer | 45 min | none |
| Tester reruns the full regression checklist in a spreadsheet (112 rows) | Tester | 3 h | 1 day (tester busy on another project) |
| Product owner reads the release notes and asks for rewording | Product owner | 20 min | 1 day |
| Developer rewords the notes | Developer | 15 min | 4 h |
| Security lead confirms no new dependencies with known vulnerabilities (required by the customer contract) | Security lead | 30 min | 2 days |
| Release manager gathers the three confirmations by email and posts "approved" in the team chat | Release manager | 15 min | 1 day |
| Developer deploys | Developer | 20 min | 4 h |

Notes from the team:
- The regression checklist has not found a failure in the last six cycles, but two earlier cycles it caught a real one.
- The same people are asked to confirm the release in three different places (spreadsheet, email, chat).
- Total elapsed: about 6 working days; total active effort: about 5 hours.
