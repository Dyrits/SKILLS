export async function chargeCard(amount: number, token: string) {
  const response = await fetch("https://payments.example.test/charge", {
    method: "POST",
    body: JSON.stringify({ amount, token }),
  });
  const body = await response.json();
  return { approved: body.status === "approved", reference: body.reference as string };
}
