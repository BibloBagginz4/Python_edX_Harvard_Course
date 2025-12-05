import sys


# ===== sys.argv[0] is reserved for the file name =====
# print("sys.argv[0]: ", sys.argv[0])


# =============== Way 1 (Using try/except)===============
# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")


# =============== Way 2 (Using if/elif/else conditionals)==============
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("Hello, My Name is", sys.argv[1])


# =============== Way 3 - (Using sys.exit) ==============
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# #Print name tags
# print("Hello, My Name is", sys.argv[1])


# =============== Way 4 - (Using for & slice of sys.argv) ==============
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, My Name is", arg)