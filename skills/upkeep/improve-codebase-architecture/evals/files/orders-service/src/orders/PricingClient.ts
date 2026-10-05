export async function priceQuote(quote: Quote): Promise<PricedQuote> {
  const response = await fetch("https://pricing.example.test/v2/price", {
    method: "POST",
    body: JSON.stringify(quote),
  });
  return response.json();
}
