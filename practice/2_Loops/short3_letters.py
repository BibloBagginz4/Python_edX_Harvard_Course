def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    # for i in range(len(names)):                           # OK WAY TO WRITE THE FOR LOOP
    #     print(write_letter(names[i], "Princess Peach"))   # OK WAT TO WRITE THE FOR LOOP

    for name in names:                                      # BETTER WAY TO WRITE FOR LOOP
        print(write_letter(name, "Princess Peach"))         # BETTER WAY TO WRITE FOR LOOP
        
def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver},

        You are cordially invited to a ball at
        Peach's Castle this evening, 7:00 PM.set

        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """


main()