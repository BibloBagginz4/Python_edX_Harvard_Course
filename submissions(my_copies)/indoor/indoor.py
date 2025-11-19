# This program will prompt a user for an input, then output that same imput in lowercase.
# Punctuation and whitespaces will be outputted unchanged. 

def main():
    user_input = input("Please type something here: ")
    user_whisper = user_input.lower()
    print(user_whisper)


main()
