#!/usr/bin/python3
def uppercase(str):
    for i in (str):
        distance = ord(i) - ord('A')
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            distance = ord(i) - ord('a')
        print(chr(ord('A') + distance), end="")
    print('\n')
