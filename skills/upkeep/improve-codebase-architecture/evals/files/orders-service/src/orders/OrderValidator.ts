export function validateQuote(quote: Quote): Quote {
  if (quote.items.length === 0) throw new Error("empty quote");
  return quote;
}

export function validateQuantity(quantity: number): boolean {
  return quantity > 0;
}

export function validateSku(sku: string): boolean {
  return sku.length > 0;
}
