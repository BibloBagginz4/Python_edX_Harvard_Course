"""
(Written by Jeff Truesdell 12-8-2025)
This is a program that:
    1) Prompts the user for a level, 𝑛.
    2) If the user does not input a positive integer, the program
       should prompt again.
    3) Randomly generates an integer between 1 and 𝑛, inclusive,
       using the random module.
    4) Prompts the user to guess that integer.
    5) If the guess is not a positive integer, the program should
       prompt the user again.
    6) If the guess is smaller than that integer, the program should
       output "Too small!" and prompt the user again.
    7) If the guess is larger than that integer, the program should
       output "Too large!" and prompt the user again.
    8) If the guess is the same as that integer, the program should
       output "Just right!" and exit.
"""

from random import randint, randrange


def main():
    guess = 0
    status = 0
    num = randint(1, user_input_num("Level: "))
    print(user_guess(num))


def user_input_num(prompt):
    while True:
        try:
            num = int(input(prompt).strip())
            if num > 0:
                return num
        except ValueError:
            number = 0


def user_guess(number):
    while True:
        guess = user_input_num("Guess: ")
        if number > guess:
            print("Too small!")
        if number < guess:
            print("Too large")
        else:
            return "Just Right"


if __name__ == "__main__":
    main()
