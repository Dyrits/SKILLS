import { chargeCard } from "../services/payments";
import { loadCart, markCartPaid } from "../services/carts";

export async function createOrder(cartId: string) {
  const cart = await loadCart(cartId);
  const charge = await chargeCard(cart.total, cart.paymentToken);
  if (!charge.approved) return { ok: false as const };
  await markCartPaid(cartId, charge.reference);
  return { ok: true as const, reference: charge.reference };
}
