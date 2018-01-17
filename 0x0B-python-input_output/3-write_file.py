#!/usr/bin/python3
'''write to file'''


def write_file(filename="", text=""):
    '''open file to write text and return the number of bytes weritten'''
    with open(filename, 'w', encoding='utf-8') as f:
        return(f.write(text))
