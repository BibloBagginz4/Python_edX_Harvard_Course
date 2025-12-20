"""
(Written by: Jeff Truesdell 12-19-2025)
This program extracts and converts embedded YouTube URLs from HTML.

1) It defines a function, parse, which takes a string of HTML as
input, searches for a YouTube embed URL contained in the value of an
iframe's src attribute, and returns the equivalent short youtu.be URL.

2) If the input contains no valid YouTube embed URL, the function returns None.

3) The input is assumed to contain at most one iframe src attribute.
"""

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url_pattern = (
        r'^<iframe.+src=\"https?://(www\.)?youtube\.com/embed/(.+?)".+iframe>$'
    )

    match = re.search(url_pattern, s)
    if not match:
        return None
    return f"https://youtu.be/{match.group(2)}"


if __name__ == "__main__":
    main()
