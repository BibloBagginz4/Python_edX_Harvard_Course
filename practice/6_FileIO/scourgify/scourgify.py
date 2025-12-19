"""
(Written by Jeff Truesdell 12-16-2025)
    This program:
        1) Expects the user to provide two command-line arguments:
            a) The name of an existing CSV file to read as input, whose
               columns are assumed to be, in order, name and house.
            b) The name of a new CSV to write as output, whose columns
               should be, in order, first, last, and house.
        2) Converts that input to that output, splitting each name into
           a first name and last name.
        3) Assume that each student will have both a first name and
           last name.
        4) If the user does not provide exactly two command-line
           arguments, or if the first cannot be read, the program should
           exit via sys.exit with an error message.
"""

import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Error: Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Error: Too many command-line arguments")
    else:
        read_file = sys.argv[1]
        write_file = sys.argv[2]

    if read_file[-4:] != ".csv" or write_file[-4:] != ".csv":
        sys.exit("Error: Filetype (.csv) expected")

    try:
        with open(read_file, "r", encoding="utf-8", newline="") as infile:
            reader = csv.DictReader(infile)

            transformed_list = []
            for row in reader:
                last, first = [names.strip() for names in row["name"].split(",")]
                transformed_list.append(
                    {"first": first, "last": last, "house": row["house"]}
                )
    except FileNotFoundError:
        sys.exit("Error: File Not Found")

    field_names = ["first", "last", "house"]
    with open(write_file, "w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(transformed_list)


if __name__ == "__main__":
    main()
