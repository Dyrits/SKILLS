// Prorates a plan change mid-cycle. Today it only handles upgrades.
export interface Subscription {
  planPriceCents: number;
  cycleDays: number;
  daysUsed: number;
}

export function upgradeCharge(current: Subscription, newPlanPriceCents: number): number {
  const remainingDays = current.cycleDays - current.daysUsed;
  const difference = newPlanPriceCents - current.planPriceCents;
  return Math.round((difference * remainingDays) / current.cycleDays);
}
