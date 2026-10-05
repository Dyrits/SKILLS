// Invented example: three tiny modules that are always called together.

import { StripeGateway } from "./stripe-gateway";
import { db } from "./db";

export function validateOrder(order: Order): void {
  if (order.items.length === 0) throw new Error("empty order");
}

export function totalOrder(order: Order): number {
  return order.items.reduce((sum, item) => sum + item.price * item.quantity, 0);
}

export async function saveOrder(order: Order, total: number): Promise<void> {
  await db.orders.insert({ ...order, total });
}

export async function processOrder(order: Order): Promise<void> {
  validateOrder(order);
  const total = totalOrder(order);
  const gateway = new StripeGateway();
  await gateway.charge(order.customerId, total);
  await saveOrder(order, total);
}
