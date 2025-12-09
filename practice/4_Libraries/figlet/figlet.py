"""
(Written by Jeff Truesdell 12-27-2025)
This program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
"""

import sys
import random
from pyfiglet import Figlet


def main():
    f = Figlet()
    fonts = f.getFonts()

    # Checking Input Conditions
    if len(sys.argv) == 1:
        selected_font = random.choice(fonts)
    elif len(sys.argv) == 3:
        if sys.argv[1] in ("-f", "--font") and sys.argv[2] in fonts:
            selected_font = sys.argv[2]
        else:
            sys.exit("Error: Argument input 'TYPE' not expected")
    else:
        sys.exit("Error: Argument input not expected")

    user_input = input(f"Input: ").strip()
    f = Figlet(font=selected_font)
    print(f.renderText(user_input))


if __name__ == "__main__":
    main()
