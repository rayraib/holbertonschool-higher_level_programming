#!/usr/bin/python3
z = 122
case = 0
for i in range(26):
    print("{}".format(chr((z - i) - case)), end="")
    if case == 0:
        case = 32
    else:
        case = 0
