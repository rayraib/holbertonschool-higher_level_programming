#!/usr/bin/python3
'''open file to read'''


def read_file(filename=""):
    ''' open and read file to stdou in UTF-8 encoding'''
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
