import re

locations = {"+1": "Unites States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}


def main():
    pattern = r"(?P<country_code>\+\d{1,3}) (?P<area_code>\d{3})-(?P<prefix_code>\d{3})-(?P<suffix_code>\d{4})"
    number = input("Number: ")

    match = re.search(pattern, number)
    if match:
        country_code = match.group("country_code")
        print(locations[country_code])
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
