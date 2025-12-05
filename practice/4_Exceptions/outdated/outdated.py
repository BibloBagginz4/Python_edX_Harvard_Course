"""
This program prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636
wherein the month in the latter might be any of the values in the list below:
["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again.
The program assumes that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""

def main():
    stop_flag = False
    while stop_flag == False:
        user_date = input("Date: ").strip().upper()
        try:
            iso_year, iso_month, iso_day, stop_flag = date_convert_iso8601(user_date)
        except IndexError:
            stop_flag = False    
    print(f"{iso_year:04}-{iso_month:02}-{iso_day:02}")


def date_convert_iso8601(us_date):
    if us_date[0:1].isalpha():
        month = []
        split_date = us_date.split(" ",2)
        month = split_date[0].capitalize()
        iso_month = convert_string_month(month)
        iso_day = int(split_date[1][:-1] if "," in split_date[1] else 0)
        iso_year = int(split_date[2]) 
    elif  us_date[0:1].isdigit():
        try:
            month, day, year = us_date.split("/")
            iso_month = int(month)
            iso_day = int(day)
            iso_year = int(year)
        except ValueError:
            iso_month = 0
            iso_day = 0
            iso_year = 0
    else:
        iso_month = 0
        iso_day = 0
        iso_year = 0
    check_flag = validate_iso_date(iso_year, iso_month, iso_day)
    return (iso_year, iso_month, iso_day, check_flag)


def convert_string_month(m):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    try:
        iso_month = int(months.index(m) + 1)
        return (iso_month)
    except ValueError:
        return (0)


def validate_iso_date(y, m, d):
    validate_flag = False
    if (0 < m < 13) and (0 < d < 31) and (y > 0):
        return True
    else:
        return False
     

if __name__ == "__main__":
    main()