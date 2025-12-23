"""
(Written by: Jeff Truesdell 12-23-2025)
This program...
"""

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um_pattern = r"\bum\b"

    find_um = re.findall(um_pattern, s, re.IGNORECASE)
    return len(find_um)


if __name__ == "__main__":
    main()
