"""
    (Written by: Jeff Truesdell 11/21/2025)
    This program prompts the user for a greeting.
        - If the greeting starts with “hello”, output $0.
        - If the greeting starts with an “h” (but not “hello”), output $20.
        - Otherwise, output $100.
    Any leading whitespace in the user’s greeting will be ignored.
    The user’s greeting will be treated with case-insensitively
"""

def main():
    response = input("Please input a greeting: ").lower().strip()
    payment = evaluate(response)
    print(payment)

def evaluate(greeting):
    if greeting[0:5] == "hello":   # This is a string splice to get the first 5 letters in the response
        return "$0"
    elif greeting[0:1] == "h":     # This is a string splice to get the first letter in the response
        return "$20"
    else:
        return "$100"

 
main()