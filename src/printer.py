import json
from tabulate import tabulate


def print_as_table(items: list[dict]):
    headers = list(items[0].keys())
    rows = []
    for item in items:
        row = [item.get(key, "") for key in headers]
        rows.append(row)

    table = tabulate(rows, headers=headers, tablefmt="round")
    print(table)
