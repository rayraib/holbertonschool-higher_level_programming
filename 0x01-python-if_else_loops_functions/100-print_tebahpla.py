#!/usr/bin/python3
flag = 0
z = 122
for i in range(26):
    if flag == 0:
        print("{}".format(chr(z - i)), end="")
    else:
        print("{}".format(chr((z - i) - 32)), end="")
    if flag == 0:
        flag = 1
    else:
        flag = 0
