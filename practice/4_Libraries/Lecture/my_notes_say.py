# import cowsay
import sys

# if len(sys.argv) == 2:
#    cowsay.cow("hello, " + sys.argv[1]) 

# if len(sys.argv) == 2:
#    cowsay.trex("Hello, " + sys.argv[1] + "!") 

from my_notes_sayings import goodbye

if len(sys.argv) == 2:
   goodbye(sys.argv[1])