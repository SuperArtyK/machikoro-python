import os
from typing import List
w = os.get_terminal_size()
#print("Hello world!")
#print("\033[%d;%dH" % (0, 0))
#print("Bye")
#print(w)

a = False
b = False
print(a)
print(b)
print( 1 if a else 2 if b else 3 )