"""
(Written by Jeff Truesdell 12-27-2025)
This program from the early 1990s for making large letters out of
ordinary text, a form of ASCII art:In a file called figlet.py, implement
a program that:

1) Expects zero or two command-line arguments:
  * Zero if the user would like to output text in a random font.
  * Two if the user would like to output text in a specific font, in
  which case the first of the two should be -f or --font, and the second
  of the two should be the name of the font.
2) Prompts the user for a str of text.
3) Outputs that text in the desired font.
4) Exit via sys.exit with an error message, if the user provides two
command-line arguments and the first is not "-f" or "--font" or the
second is not the name of a font
"""

import sys
import random
from pyfiglet import Figlet


def validate_input_args(args, fonts):
    # Checking if zero input arguments (Random Font)
    if len(args) == 1:
        return random.choice(fonts)

    # Checking if two input arguments. (User Font)
    if len(args) == 3:
        flag, font_name = args[1], args[2]

        if flag in ("-f", "--font") and font_name in fonts:
            return font_name

        sys.exit("Error: Invalid Argument Type")

    # Anything else automatically invalid
    sys.exit("Error: Invalid Number of Arguments")


def main():
    f = Figlet()
    fonts = f.getFonts()

    selected_font = validate_input_args(sys.argv, fonts)

    # Prompt User for String
    user_input = input(f"Input: ").strip()

    f = Figlet(font=selected_font)
    print(f.renderText(user_input))


if __name__ == "__main__":
    main()
