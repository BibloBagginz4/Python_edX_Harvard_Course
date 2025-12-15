"""
(Written by: Jeff Truesdell 12-15-2025)
"""

import sys
import csv
from tabulate import tabulate


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Error: expected exactly one CSV file argument")

    file_name = sys.argv[1]

    if not file_name.lower().endswith(".csv"):
        sys.exit("Error: file must have a .csv extension")

    try:
        with open(file_name, encoding="utf-8", newline="") as file:
            menu = list(csv.DictReader(file))
    except FileNotFoundError:
        sys.exit("Error: file not found")

    print(tabulate(menu, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
