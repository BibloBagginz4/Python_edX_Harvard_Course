"""
(Written by: Jeff Truesdell 12-19-2025)
This program implements a function called <validate> that expects an
IPv4 address as input in a ,str. format and returns True or False,
respectively if that input is a valid IPv4 address or not.
"""

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

    match = re.search(ip_pattern, ip)
    if match:
        for i in range(1, 5):
            octet = match.group(i)

            # Validating that octet had no leading zeros
            if len(octet) > 1 and octet[0] == "0":
                return False

            # Validating octet is in valid range
            if not 0 <= int(octet) <= 255:
                return False

        return True
    return False


if __name__ == "__main__":
    main()
