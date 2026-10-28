#!/usr/bin/env bash
set -euo pipefail
export GIT_AUTHOR_NAME=Eval GIT_AUTHOR_EMAIL=eval@example.com GIT_COMMITTER_NAME=Eval GIT_COMMITTER_EMAIL=eval@example.com
git init -q -b main
git config user.name Eval
git config user.email eval@example.com
git config commit.gpgsign false
mkdir -p src
cat > src/users.ts <<'EOF'
export type Result<T> = { ok: true; value: T } | { ok: false; error: string };
export function findUser(id: string): Result<{ id: string; isActive: boolean }> {
  if (!id) return { ok: false, error: "missing id" };
  return { ok: true, value: { id, isActive: true } };
}
EOF
cat > src/orders.ts <<'EOF'
import type { Result } from "./users";
export function findOrder(orderId: string): Result<{ orderId: string; isPaid: boolean }> {
  if (!orderId) return { ok: false, error: "missing order id" };
  return { ok: true, value: { orderId, isPaid: false } };
}
EOF
cat > src/users.test.ts <<'EOF'
import { findUser } from "./users";
test("returns an error for a missing id", () => {
  expect(findUser("").ok).toBe(false);
});
EOF
git add -A && git commit -qm "Initial commit"
