"""
    (Written br Jeff Truesfell (11-18-2025)
    This program will calculate a customary tip in USD, for your server after dining in a restaurant.
    The user will input the cost of the meal and the percentage that they would like to tip.
    The calculator will then calculate what the tip amount should be.
"""

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    float_cost = float(d.replace("$", "+"))
    return(float_cost)


def percent_to_float(p):
    float_percent = float(p.replace("%", ""))
    float_percent = float_percent / 100
    return(float_percent)


main()