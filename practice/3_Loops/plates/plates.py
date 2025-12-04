"""
     (Written by Jeff Truesdell 11/28/2025)
     In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car,
     with your choice of letters and numbers instead of random ones. Among the requirements, though, are:
          1) All vanity plates must start with at least two letters.
          2) All vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
          3) Numbers cannot be used in the middle of a plate; they must come at the end.
               3a) For example, AAA222 would be an acceptable vanity plate;
               3b) AAA22A would not be acceptable.
          4) The first number used cannot be a ‘0’.
          5) No periods, spaces, or punctuation marks are allowed.

     This program prompts the user for a vanity plate and then outputs "Valid" if it meets all of the requirements
     or "Invalid" if it does not.
     Assume that any letters in the user’s input will be uppercase.
     Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
     Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    a = start_two_letters(s)               # Check that first 2 characters are letters, not numbers
    b = char_length(s)                     # Check that length is 2 to 6 letters long
    c = no_mid_num(s)                      # Check that there are no letters after numbers
    d = first_number_non_zero(s)           # Check that the first number (if any) is not a zero
    e = alpha_num_only(s)                  # Check that only letters and numbers are used
    return a == b == c == d == e == True
    

def start_two_letters(s):
    first_two = s[0:2]
    return first_two.isalpha() 


def char_length(s):
    if 2 <= len(s) <=6:
        return True
    else:
        return False


def no_mid_num(s):
    for c in range(len(s)):
        if s[c].isdigit():
            return s[c:].isdigit()     # This will return True if all characters after the first digit are digits.
    return True                        # This will return True if no digits exist (i.e. all characters are alpha)


def first_number_non_zero(s):
    for c in range(len(s)):
        if s[c].isdigit():
            return s[c]!= "0"         # This will return True if the first digit does not equal zero.
    return True                        # This will return True if no digits exist (i.e. all characters are alpha)


def alpha_num_only(s):
    return s.isalnum()


main()