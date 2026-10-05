# How the Orchard job queue retries failed jobs

Question: what retry policy does the Orchard queue apply by default?
Version checked: Orchard 4.2, as of 2026-09-12.

- Failed jobs are retried up to 5 times with exponential backoff ([official configuration reference](https://orchard.example.test/docs/4.2/retries)).
- The backoff base is 2 seconds and is configurable ([same page](https://orchard.example.test/docs/4.2/retries#backoff)).

Unresolved: whether dead jobs are kept after the final failure; the reference is silent.
