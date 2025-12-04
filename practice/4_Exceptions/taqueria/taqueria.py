"""
(Written by Jeff Truesdell 12/1/2025)
This  program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d
(which is a common way of ending one’s input to a program).
After each inputted item, display the total cost of all items inputted thus far,
prefixed with a dollar sign ($) and formatted to two decimal places.
Treat the user’s input case insensitively.
Ignore any input that isn’t an item.
Assume that every item on the menu will be titlecased.
"""

def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    stop_flag = False
    order = []
    total_cost = 0

    while stop_flag == False:
        try:
            item = input("Item: ").strip().title()
            item_cost = menu[item]
            order.append(item)
            total_cost += item_cost
            print(f"Total ${total_cost:.2f}")
        except EOFError:
            stop_flag = True
            print()
        except KeyError:
            stop_flag = False
        

if __name__ == "__main__":
    main()