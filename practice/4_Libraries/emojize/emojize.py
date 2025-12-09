"""
(Written by Jeff Truesdell 12/7/2024)
This program prompts the user for a str in English and then outputs the “emojized” version of that str,
converting any codes (or aliases) therein to their corresponding emoji.
See carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a list of codes with aliases.
"""

import emoji


def main():
    user_string = input("Input: ").strip()
    print(f"Output:", emoji.emojize(user_string, language="alias"))


if __name__ == "__main__":
    main()
