import { validateQuote } from "./OrderValidator";
import { saveOrder } from "./OrderRepo";
import { priceQuote } from "./PricingClient";

export async function handleIntake(quote: Quote): Promise<Order> {
  const checked = validateQuote(quote);
  const priced = await priceQuote(checked);
  return saveOrder(priced);
}
