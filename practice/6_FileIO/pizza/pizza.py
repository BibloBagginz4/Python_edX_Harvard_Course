"""
(Written by: Jeff Truesdell 12-15-2025)
"""

import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) != 2:
        sys.exit("Error: One file name expected in command-line")

    file_name = sys.argv[1]

    if file_name[-4:] != ".csv":
        sys.exit("Error: not a (.csv) file")

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            menu = []
            reader = csv.DictReader(file)
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        sys.exit("Error: File not found")

    print(tabulate(menu, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
