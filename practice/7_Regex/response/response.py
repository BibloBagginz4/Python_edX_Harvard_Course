"""
(Written by: Jeff Truesdell 12-23-2025)

"""

import validators


def main():
    email = input("What's youe email address: ")

    if validate(email) is True:
        print("Valid")
    else:
        print("Invalid")


def validate(s):
    return validators.email(s)


if __name__ == "__main__":
    main()
