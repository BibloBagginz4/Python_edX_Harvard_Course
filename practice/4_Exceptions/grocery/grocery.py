"""
(Written by Jeff Truesdell 12/2/2025)
This program that prompts the user for items, one per line, until the user inputs control-d (or control + z on windows)
(which is a common way of ending one’s input to a program).
Then output the user’s grocery list in all uppercase,
sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item.
No need to pluralize the items.
Treat the user’s input case-insensitively.
"""

def main():
    stop_flag = False
    shopping_list = {}
    while stop_flag == False:
        try:
            item = input("Item: ").strip().upper()
            x = shopping_list.get(item, 0)
            shopping_list[item] = x+1
   
        except EOFError:
            stop_flag = True

    print(sorted_list(shopping_list))


def sorted_list(list):
    for key in sorted(list):
        print(list[key], key)


if __name__ == "__main__":
    main()    