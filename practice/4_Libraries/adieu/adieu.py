"""
(Written by Jeff Truesdell 12/8/2025)
This program prompts the user for names, one per line, until the user inputs control-d (control-z in Windows).
Assume that the user will input at least one name.
Then bid adieu to those names, separating:
    * Two names with one "and".
    * Three names with two commas and one "and".
    * 𝑛 names with 𝑛 −1 commas and one "and".

===== EXAMPLES =====
Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
"""


def main():
    names = []
    while True:
        try:
            names.append(input("Name: "))
        # While Loop Break when user enters (CTRL+D) or (CTRL+Z in Windows)
        except EOFError:
            print()  # Moves cursor to new line
            break

    print(f"Adieu, adieu, to {conc_string(names)}")


def conc_string(names):
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return " and ".join(names)
    else:
        return ", ".join(names[0:-1]) + ", and " + names[-1]


if __name__ == "__main__":
    main()
