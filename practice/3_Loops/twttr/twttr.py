"""
(Written by Jeff Truesdell 11/28/2025)
This program that prompts the user for a str of text,
then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.
"""

def main():
    tweet = input("Input: ")
    twt = omit_vowels(tweet)
    print("Output:", twt)


def omit_vowels(tweet):
    remove_list = {"a", "e", "i", "o", "u"}
    revised_tweet = ""
    for c in tweet:
        if c.lower() in remove_list:
            revised_tweet += ""
        else:
            revised_tweet += c
    return revised_tweet



main()    