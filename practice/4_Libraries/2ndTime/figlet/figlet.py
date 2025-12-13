"""
(Written by Jeff Truesdell 12-10-2025)
This program:
    1) Expects zero or two command-line arguments:
        1a) If the user would like to output text in a random font,
            there be Zero command line inputs.
        1b) If the user would like to output text in a specific font,
            there would be TWO command line inputs, in which case the
            first of the two should be -f or --font, and the second of
            the two should be the name of the font.
    2) Prompts the user for a str of text.
    3) Outputs that text in the desired font.
    4) If the user provides two command-line arguments and the first is
       not -f or --font or the second is not the name of a font, the
       program should exit via sys.exit with an error message.
"""

import sys
import random
from pyfiglet import Figlet


def main():
    f = Figlet()
    fonts = f.getFonts()

    if len(sys.argv) == 1:
        selected_font = random.choice(fonts)
    elif len(sys.argv) == 3:
        if check_argv1(sys.argv[1]) == check_argv2(sys.argv[2], fonts) == True:
            selected_font = sys.argv[2]
        else:
            sys.exit("Error: hahahahaha")
    elif len(sys.argv) == 2:
        sys.exit("Error: Expected 0 or 2 arguments")
    else:
        sys.exit("Error: Too many arguments")

    user_input = input("Input: ")
    f = Figlet(font=selected_font)
    print(f.renderText(user_input))


def check_argv1(a):
    if a in ("-f", "--font"):
        return True
    return False


def check_argv2(a, fonts):
    if a in fonts:
        return True
    return False


if __name__ == "__main__":
    main()
