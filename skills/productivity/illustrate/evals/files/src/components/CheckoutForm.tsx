import { useState } from "react";
import { createOrder } from "../api/orders";

export function CheckoutForm({ cartId }: { cartId: string }) {
  const [status, setStatus] = useState<"idle" | "pending" | "failed" | "done">("idle");

  async function onSubmit() {
    setStatus("pending");
    const result = await createOrder(cartId);
    setStatus(result.ok ? "done" : "failed");
  }

  return <button onClick={onSubmit} disabled={status === "pending"}>Pay</button>;
}
