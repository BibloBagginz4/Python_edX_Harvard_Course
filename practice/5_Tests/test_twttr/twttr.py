def main():
    tweet = input("Input: ").strip()
    twt = shorten(tweet)
    print("Output:", twt)


def shorten(word):
    remove_list = {"a", "e", "i", "o", "u"}
    revised_word = ""
    for c in word:
        if c.lower() in remove_list:
            revised_word += ""
        else:
            revised_word += c
    return revised_word


if __name__ == "__main__":
    main()
