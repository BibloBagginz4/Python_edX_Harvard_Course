"""
(Written by Jeff Truesdell 12/14/2025)
    This program expects exactly one command-line argument, the name
    (or path) of a Python file, and outputs the number of lines of code in
    that file, excluding comments and blank lines.
    1) If the user does not specify exactly one command-line argument,
       or if the specified file’s name does not end in .py, or if the
       specified file does not exist, the program should instead exit
       via sys.exit.
    2) Assume that any line that starts with #, optionally preceded by
    whitespace, is a comment.
    3) A docstring should not be considered a comment.
    4) Assume that any line that only contains whitespace is blank.
"""

import sys


def main():
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        sys.exit("Error: One file name expected in command-line")

    if file_name[-3:] != ".py":
        sys.exit("Error: Not a (.py) file")

    try:
        with open(file_name, "r", encoding="utf-8", newline="") as file:
            contents = file.readlines()

    except FileNotFoundError:
        sys.exit("Error: File was not found.")

    filtered = []
    for line in contents:
        # Checking and skipping comments
        if line.strip().lstrip("#") == line.strip():
            pass
        else:
            continue
        # checking and skipping Blank Lines
        if line.strip():
            pass
        else:
            continue
        filtered.append(line)

    print(len(filtered))


if __name__ == "__main__":
    main()
