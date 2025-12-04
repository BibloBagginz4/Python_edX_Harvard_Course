"""
(Written by Jeff Truesdell 11-27-2025)
This program prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
Assume that the user’s input will indeed be in camel case. Note that in camelCase, the first letter is not capitalized.
"""

def main():
    camel_case = input("Enter a string in camelCase format: ")
    print(make_snake(camel_case))

def make_snake(camel):
    snake_string = ""
    for char in camel:
        if char.isupper():
           snake_string += "_" + char.lower()
        else:
           snake_string += char
    return snake_string

main()