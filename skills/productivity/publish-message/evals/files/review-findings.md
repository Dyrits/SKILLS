# Review of pull request 57, "Retry payment ledger writes" (harbor/harbor-api, scratch setup, no real remote)

Head revision reviewed: 9b7d0e2. The review is finished and the dispositions below are agreed with the author, Noor.

1. Typo in the log message at `src/webhooks/handle-payment.ts` line 13: "recieved" should be "received". Open. Fix is one word.
2. The retry list at line 14 includes status 400. Agreed with Noor in the thread that a 400 is never retried, so the entry is removed. Open. Fix is one line.
3. Open question: should status 429 be retried? Noor says yes, the ledger team has not answered. Decision needed from the ledger team before merge.
4. The type `PaymentEvt` should be renamed `PaymentEvent` in three files (`handle-payment.ts`, `refund.ts`, `types.ts`). Open, spans files.
5. A test for the retry behaviour exists as a local commit on Noor's machine (`a41c9d0`), not yet pushed to the pull request. Verified locally: all tests pass.
