import { db } from "../db";

export async function saveOrder(order: PricedQuote): Promise<Order> {
  const row = await db.insert("orders", order);
  return { ...order, id: row.id };
}

export async function findOrder(id: string): Promise<Order | null> {
  return db.find("orders", id);
}

// Leaks pricing knowledge: recomputes the discount instead of trusting the stored price.
export async function totalWithDiscount(id: string): Promise<number> {
  const order = await findOrder(id);
  return order ? order.total * (1 - order.discountRate) : 0;
}
