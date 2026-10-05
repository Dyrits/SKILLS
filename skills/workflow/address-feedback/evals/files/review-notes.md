# Review notes on shipping.py

Pasted from a chat message. Mara is the reviewer for items 1 to 3 and 5, Tomas for item 4.

1. (Mara) `billable_weight_kg` rounds the weight down. A 1.1 kg parcel is billed as 1.0 kg, which undercharges. It should round up to the next 0.5 kg.
2. (Mara) The parameter name `w` is cryptic, please use something descriptive.
3. (Mara) Please reject anything over 30 kg by raising `ValueError`, so nobody quotes a parcel the courier cannot carry.
4. (Tomas) Do not raise on heavy parcels, callers cannot handle exceptions here. Return a quote of `None` and let the caller route it to freight.
5. (Mara) Nice work overall, thanks for the quick turnaround!
6. (Mara) While you are in there, could you move the whole pricing module from integer cents to `Decimal` and update every caller in the checkout service too?
