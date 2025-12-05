"""
    (Written by Jeff Truesdell 11-28-2025)
    This program prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
    Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
    Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""

def main():
    coin = 0
    amount_due = 50
    print("Amount Due: ", amount_due,)
    while 0 < amount_due:
        coin = int(input("Insert Coin: "))
        amount_due = insert_coin(coin, amount_due)
        if amount_due > 0:
            print("Amount Due:", amount_due)

    print("Change Owed:", abs(amount_due))



def insert_coin(coin, due):
        valid_coin = [25, 10, 5]
        if coin in valid_coin:
            due -= coin
            return due
        else:
            return due


main()