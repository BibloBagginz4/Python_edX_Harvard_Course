"""
(Written by Jeff Truesdsell 12-8-2025)
This is a program that:
    01) Prompts the user for a level, 𝑛.
    02) If the user does not input 1, 2, or 3, the program should prompt
        again.
    03) Randomly generates ten (10) math problems formatted as X + Y =
        wherein each of X and Y is a non-negative integer with 𝑛 digits.
        No need to support operations other than addition (+).
    04) The order in which x and y is generated matters.
    05) The program generates random numbers in x, y pairs to simulate
        generating one math question at a time
        (e.g., x0 with y0, x1 with y1, and so on).
    06) It prompts the user to solve each of those problems.
    07) If an answer is not correct (or not even a number), the program
        will output "EEE" and prompt the user again
    08) Allow the user up to three tries in total for that problem.
    09) If the user has still not answered correctly after three tries,
        the program outputs the correct answer.
    10) The program will ultimately output the user’s score: the number
        of correct answers out of 10.
    11) The program is structured as follows:
            - The "get_level: function prompts (and, if need be,
              re-prompts) the user for a level and returns 1, 2, or 3.
            - The "generate_integer" function returns a single randomly
              generated non-negative integer with level digits or raises
               a ValueError if level is not 1, 2, or 3.
"""

import random


def main():
    results = 0

    level = get_level()
    for i in range(10):
        x, y = generate_integer(level), generate_integer(level)
        a = x + y
        results += check_answer(x, y, a)
    print(f"Score:", results)


def get_level():
    while True:
        try:
            num = int(input("Level: ").strip())
            if 0 < num < 4:
                return num
        except ValueError:
            pass  # Prompt user again


def generate_integer(digits):
    if digits == 1:
        return random.randint(0, 9)
    if digits == 2:
        return random.randint(10, 99)
    if digits == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Allowed values are 1, 2 or 3")


def check_answer(x, y, a):
    for i in range(3):
        try:
            user_answer = int(input(f"{x} + {y} = ").strip())
            if user_answer == a:
                return 1
            else:
                print("EEE")
        except ValueError:
            print("EEE")
            pass  # Prompt user again
    print(f"{x} + {y} = {a}")
    return 0


if __name__ == "__main__":
    main()
