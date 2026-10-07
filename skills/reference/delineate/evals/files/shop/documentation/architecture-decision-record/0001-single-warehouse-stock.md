# Stock is tracked for one warehouse only

The shop ships from a single warehouse, so stock levels are a single number per product, not per location. Moving to several warehouses later would require reworking every stock query, which we accepted to keep checkout fast.
