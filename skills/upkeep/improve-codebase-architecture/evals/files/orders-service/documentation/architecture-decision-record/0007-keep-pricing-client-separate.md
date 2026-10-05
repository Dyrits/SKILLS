# 0007: Keep the pricing client a separate module

Status: accepted, 2025-11-03

Context: Pricing is owned by another team and exposed over HTTP. Their rules change weekly.

Decision: The PricingClient stays its own module with its own interface, so a pricing change never touches order code. Do not fold it into order intake.
