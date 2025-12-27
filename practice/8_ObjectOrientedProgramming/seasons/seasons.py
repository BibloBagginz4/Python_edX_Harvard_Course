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
import operator
import inflect


def main():
    birthday = input(f"Date of Birth: ")
    today = date.today()

    # Validating user input and converting str to date object
    try:
        b_day = date.fromisoformat(birthday)
    except:
        sys.exit("Invalid date")

    # Finishing input format, since only the valid format is length 10
    if len(birthday) != 10:
        sys.exit(f"Length is not 10")

    print(convert_minutes(today, b_day))


def convert_minutes(d1, d2):
    # Subtracting birthday from today
    delta = operator.__sub__(d1, d2)

    # Converting from days to minutes (1440 minutes per day)
    minutes = delta.days * 1440

    # Changing from numbers to words
    p = inflect.engine()

    return (f"{p.number_to_words(minutes, andword="")} minutes").capitalize()


if __name__ == "__main__":
    main()
