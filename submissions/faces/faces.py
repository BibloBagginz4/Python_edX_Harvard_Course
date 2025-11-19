"""
     This prograam implements a function called convert that accepts a str as input and returns that same input
     with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁
     (otherwise known as a slightly frowning face). All other text should be returned unchanged.

     Then, a function called main() is implemenented, that prompts the user for input,
     calls the convert() function on that input, and prints the result. 
"""
def convert(user_string):
    new_string = user_string.replace(":)", "🙂")
    new_string = new_string.replace(":(", "🙁")
    return(new_string)

def main():
    print("Please type a sentence that has a happyface  :)  and/or a frowning face  :(  in it.")
    user_input = str(input())
    print(convert(user_input))



main()
 