import os
w = os.get_terminal_size()
print("Hello world!")
print("\033[%d;%dH" % (0, 0))
print("Bye")
print(w)