MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]


def main():
    while True:
        raw = input("Date: ").strip()

        parsed = parse_date(raw)
        if parsed:
            year, month, day = parsed
            print(f"{year:04}-{month:02}-{day:02}")
            break


def parse_date(s):
    """Return (year, month, day) if valid, otherwise None."""

    # Case 1: Numeric MM/DD/YYYY
    if "/" in s:
        try:
            month, day, year = map(int, s.split("/"))
        except ValueError:
            return None
        return (year, month, day) if is_valid(year, month, day) else None

    # Case 2: Written Month Day, Year
    try:
        month_str, rest = s.split(" ", 1)
        day_str, year_str = rest.split(",", 1)
        month = MONTHS.index(month_str.capitalize()) + 1
        day = int(day_str.strip())
        year = int(year_str.strip())
    except Exception:
        return None

    return (year, month, day) if is_valid(year, month, day) else None


def is_valid(y, m, d):
    return y > 0 and 1 <= m <= 12 and 1 <= d <= 31


if __name__ == "__main__":
    main()
