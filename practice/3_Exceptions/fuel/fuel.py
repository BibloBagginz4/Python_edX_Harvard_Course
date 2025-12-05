"""
(Written by Jeff Truesdell 12-01-2025)
This program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is a positive integer,
and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""
def main():
    valid_fraction = False
    while valid_fraction == False:
        user_input = input("Fraction: ")
        x, y, valid_fraction = parse_fraction(user_input)
    level = round((x / y) * 100)
    if level <= 1:
        print("E")
    elif level >= 99:
        print("F")
    else:
        print(f"{level}%")

def parse_fraction(fraction):
    try:
        fraction_split = fraction.split("/", maxsplit=1)
        x = int(fraction_split[0])
        y = int(fraction_split[1])
        valid_fraction = test_fraction(x, y)
        return x, y, valid_fraction
    except ValueError:
        return None, None, False
    except IndexError:
        return None, None, False

def test_fraction(x, y):
    if y <= 0:
        return False
    elif x < 0:
        return False
    elif x > y:
        return False
    else:
        return True


if __name__ == "__main__":
    main()