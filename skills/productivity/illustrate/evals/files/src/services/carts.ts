export async function loadCart(cartId: string) {
  return { id: cartId, total: 4200, paymentToken: "tok_demo" };
}

export async function markCartPaid(cartId: string, reference: string) {
  // writes the payment reference onto the cart record
}
