import { money } from "../money";

export function summaryLine(label: string, cents: number): string {
  return `${label};${money(cents)}`;
}
