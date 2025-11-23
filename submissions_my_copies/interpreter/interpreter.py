"""
(Written by: Jeff Truesdell 11/22/2025)
This Program prompts the user for an arithmetic expression and then calculates and outputs the result
as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted
as x y z, with one space between x and y and one space between y and z, wherein:
    x is an integer
    y is +, -, *, or /
    z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.
"""

def main():
    expression = input("Enter arithmetic expression: ").strip()
    x, y, z = string_split(expression)
    answer = evaluate_expression(x, z, y)
    print(answer)


def string_split(expression_string):
    x, y, z = expression_string.split()
    x = float(x)                             # Convert from string to floating number.
    z = float(z)                             # Convert from string to floating number.
    return x, y, z


def evaluate_expression(a, b, operand):
    if operand == "+":
        return round(a + b, 1)
    elif operand == "-":
        return round(a - b, 1)
    elif operand == "*":
        return round(a * b, 1)
    elif operand == "/" and b == 0:
        return "Error: You cannot divide by zero"
    elif operand == "/":
        return round(a / b, 1)
    else:
        return "Error: Try again"


main()