#   EXAMPLE 1 (PRINT COLUMN 4 HASH TAGS HIGH)
# # def main():
#     print_column(3)

# def print_column(height):
#     for _ in range(height):
#         print("#")


# main()

#   EXAMPLE 2 (PRINT ROW 4 QUESTION MARKS WIDE)
# def main():
#     print_row(4)


# def print_row(width):
#     print("?" * width)


# main()


#   EXAMPLE 2 (PRINT A 3X3 GRID)
def main():
    print_square(3)

# def print_square(size):            # Method 2.1
#     for i in range(size):          # For each row in square
#         for j in range(size):      # For each brick in row
#             print("#", end="")     # Print brick
#         print()                    # Adds a carriage return after each row

# def print_square(size):            # Method 2.2
#     for i in range(size):          # For each row in square
#         print("#" * size)          # Print (qty = size) #'s followed by carriage return

def print_square(size):              # Method 2.3
    for i in range(size):            # For each row in square
        print_row(size)              # Call the print_row function

def print_row(width):                # print_row function called in Method 2.3
    print("#" * width)



main()