"""
(Written by Jeff Truesdell 12-10-2025)
    This program prompts the user for a str in English and then outputs
    the “emojized” version of that str, converting any codes (or
    aliases) therein to their corresponding emoji.
"""

import emoji


def main():
    user_input = input("Input: ").strip()
    converted = emoji.emojize(user_input, language="alias")
    print(converted)


if __name__ == "__main__":
    main()
