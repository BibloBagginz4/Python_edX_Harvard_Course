"""
(Written by: Jeff Truesdell 12-26-2025)
This program prompts the user for their date of birth in YYYY-MM-DD
format and then sings prints how old they are in minutes, rounded to the
nearest integer, using English words instead of numerals, just like the
song from Rent, without any and between words.

Since a user might not know the time at which they were born, assume,
for simplicity, that the user was born at midnight (i.e., 00:00:00) on
that date.

And assume that the current time is also midnight.
In other words, even if the user runs the program at noon, assume that
it’s actually midnight, on the same date.

Use datetime.date.today to get today’s date, per:
docs.python.org/3/library/datetime.html#datetime.date.today.

The program will use not only a main function but also with one or more
other functions as well.

You’re welcome to import other (built-in) libraries, or any that are
specified in the below hints.

Exit via sys.exit if the user doesn't input a date in YYYY-MM-DD format.
Ensure that your program will not raise any exceptions.

Either before or after you implement seasons.py, additionally implement,
in a file called test_seasons.py, one or more functions that test your
implementation of any functions besides main in seasons.py thoroughly,
each of whose names should begin with test_ so that you can execute your
tests with:
"""

import sys
from datetime import date
import inflect

p = inflect.engine()


def main():
    birthday_str = input("Date of Birth: ").strip()

    # Enforce exact YYYY-MM-DD shape
    if (
        len(birthday_str) != 10
        or birthday_str[4] != "-"
        or birthday_str[7] != "-"
        or not (birthday_str[:4] + birthday_str[5:7] + birthday_str[8:]).isdigit()
    ):
        sys.exit("Invalid date")

    # Semantic validation
    try:
        birthdate = date.fromisoformat(birthday_str)
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    print(minutes_in_words(birthdate, today))


def minutes_in_words(birthdate: date, today: date) -> str:
    delta = today - birthdate
    minutes = delta.days * 24 * 60

    words = p.number_to_words(minutes, andword="")
    return f"{words} minutes".capitalize()


if __name__ == "__main__":
    main()
