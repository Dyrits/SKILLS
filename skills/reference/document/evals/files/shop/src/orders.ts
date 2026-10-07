// Invented example showing how this codebase is written.
export type Result<T> = { ok: true; value: T } | { ok: false; error: AppError };

export function parseQuantity(input: string): Result<number> {
  const n = Number(input);
  if (!Number.isInteger(n) || n < 1) return { ok: false, error: { code: "bad_quantity" } };
  return { ok: true, value: n };
}

export function findOrder(id: string): Result<Order> {
  const order = store.get(id);
  return order ? { ok: true, value: order } : { ok: false, error: { code: "not_found" } };
}
