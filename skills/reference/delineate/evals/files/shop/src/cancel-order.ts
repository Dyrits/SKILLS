// Invented example. Cancels an entire order; there is no per-item path.
export async function cancelOrder(orderId: string): Promise<void> {
  const order = await orders.get(orderId);
  if (order.status === "shipped") throw new Error("too late to cancel");
  order.status = "cancelled";
  await orders.save(order);
}
