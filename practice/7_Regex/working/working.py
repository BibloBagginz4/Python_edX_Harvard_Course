"""
(Written by Jeff Truesdell 12-19-2025)
This program implements a function called `convert()` that expects a
`str` in 12-hour format and returns the corresponding `str` in 24-hour
format.
1) Expect that AM & PM will be capitalized with no periods and a space
before each.
2) A value will be raised if the input to convert is not not correct.
3) Do not assume that times will start in the AM and end in the PM.
4) The only allowed imports are `re` & `sys` but they do not have to be
utilized in the program.
"""

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_pattern = r"^(1[0-2]|[1-9]):?([0-5][0-9])?\s(AM|PM) to (1[0-2]|[1-9]):?([0-5][0-9])?\s(AM|PM)$"

    match = re.fullmatch(time_pattern, s)
    if match:
        time1 = hour_to_24(match.group(1), match.group(2), match.group(3))
        time2 = hour_to_24(match.group(4), match.group(5), match.group(6))
        return f"{time1} to {time2}"
    else:
        raise ValueError


def hour_to_24(hh, mm, period):
    hh = int(hh)
    if period == "AM" and hh == 12:
        hh = 0
    elif period == "PM" and hh == 12:
        hh = 12
    elif period == "PM" and hh < 12:
        hh = hh + 12
    else:
        hh = hh

    if mm == None:
        mm = int(0)
    else:
        mm = int(mm)

    return f"{hh:02}:{mm:02}"


if __name__ == "__main__":
    main()
