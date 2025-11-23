"""
    (Written by Jeff Truesdell 11/23/2025)
    This program prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.
       - If it’s not time for a meal, there is no output.
       - The user’s input will be formatted in 24-hour time as #:## or ##:##.
       - Each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between,
         it’s time for breakfast.

    PROGRAM STRUCTURE: convert() is a function (that can be called by main) that converts time,
    a str in 24-hour format, to the corresponding number of hours as a float.
    For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
"""

def main():
    user_input = input("Enter a time (in 24-hr format #:## or ##:##) to check if it is a mealtime: ").strip()
    float_time = convert(user_input)
    meal = determine_meal(float_time)
    if meal != None:
        print(meal)


def convert(time):
    hours, minutes = time.split(":")
    float_time = float(hours) + float(minutes)/60
    return float_time

def determine_meal(time):
    if 7.00 <= time <= 8.00:
        return "breakfast time"
    elif 12.00 <= time <= 13.00:
        return "lunch time"
    elif 18.00 <= time <= 19.00:
        return "dinner time"
    else:
        return


if __name__ == "__main__":
    main()