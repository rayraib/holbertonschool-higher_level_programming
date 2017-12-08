#!/usr/bin/python3
from add_0 import add
'''If the program is being directly executed and not imported as module,
then, import function add from module add_0 and call add on the two
variables a and b'''
if __name__ == "__main__":
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
