# Harbor web (invented project)

Copy `.env.example` to `.env`, fill in the values, and run `npm run dev`. Deploys run from `.github/workflows/deploy.yml` on every push to main.

The payments account is on Stripe, transactional email goes through Resend, and the deploy host issues a personal deploy token.
