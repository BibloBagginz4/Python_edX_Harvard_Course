"""
    (Created by Jeff Truesdell 11-18-2025)
    This Python program prompts the user for mass as an integer (in kilograms)
    and then outputs the equivalent number of Joules as an integer.
    Assume that the user will input an integer.
"""

c = 300000000     # speed of light constant = (3.0 x 10^8 m/sec)
c_squared = c * c
mass = input("Enter a mass (as an interger) in kilograms: ")
energy = int(mass) * c_squared

print("Energy (Joules): ", energy)