#!/usr/bin/python3
'''open file to append'''


def append_write(filename="", text=""):
    '''append text to filename and return number of bytes appended'''
    with open(filename, 'a', encoding='utf-8') as f:
        return(f.write(text))
