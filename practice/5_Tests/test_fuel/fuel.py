"""
(Written by Jeff Truesdell 12-01-2025)
1) This program that prompts the user for a fraction, with expected
format of X/Y.
2) It tests that both X and Y are a positive integers
3) It outputs, as a percentage rounded to the nearest integer, how much
fuel is in the tank.
4) If 1% or less remains, output E instead to indicate that the tank is
essentially empty.
5) If 99% or more remains, output F instead to indicate that the tank is
essentially full.
6) If X or Y is not an integer, prompt the user again.
7) If X is greater than Y, prompt the user again.
8) If Y is 0, prompt the user again.
9) Exceptions like ValueError or ZeroDivisionError are caught and raised
to main().
"""


def main():
    while True:
        user_input = input("Fraction: ").strip()
        try:
            percent = convert(user_input)
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

    level = gauge(percent)
    print(level)


def convert(fraction):
    fraction_split = fraction.split("/", maxsplit=1)
    x = int(fraction_split[0])
    y = int(fraction_split[1])
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    if x < 0 or y < 0:
        raise ValueError
    else:
        return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
