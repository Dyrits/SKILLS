import json
import sys

from totals import display_total, export_total


def export_invoice(path):
    with open(path) as handle:
        order = json.load(handle)
    total = export_total(order["lines"])
    print(f"order,{order['order_id']}")
    print(f"total,{total / 100:.2f}")


if __name__ == "__main__":
    export_invoice(sys.argv[1])
