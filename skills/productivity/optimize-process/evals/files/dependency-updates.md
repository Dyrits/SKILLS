# Dependency updates at Marlow Works (current)

- An automated tool opens one pull request per week, grouping all minor and patch updates. It runs on Monday at 06:00.
- The test suite and a vulnerability scan run on that pull request automatically (11 minutes).
- A developer on rotation reviews the pull request on Monday morning: reads the changelog summary the tool attaches and checks that the checks are green (about 10 minutes).
- Passing pull requests are merged the same day. Major updates are never grouped; they are opened separately and scheduled by the team lead.
- Last quarter: 13 weekly pull requests, 12 merged on Monday, 1 merged Tuesday because a flaky test needed a rerun. No production incident was traced to a dependency update.
