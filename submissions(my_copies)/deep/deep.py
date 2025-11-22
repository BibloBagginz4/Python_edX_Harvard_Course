"""
    (Written by Jeff Truesdell 11/20/2025)
    This program will prompt the user for the answer to the Great Question
    of Life, the Universe and Everything.
    If the user inputs 42 or (case-insensitively) forty-two or forty two, then the program will output YES.
    Otherwise the program will output No.
"""

def main():
    user_answer = input("Please provide the answer The Answer to the Great Question of Life, the Universe and Everything: ")
    check_answer = evaluate(user_answer)
    print(check_answer)


def evaluate(answer):
    a = answer.lower().strip()
    if a == "42" or a == "forty-two" or a == "forty two":
        return "YES"
    else:
        return "NO"


main()
