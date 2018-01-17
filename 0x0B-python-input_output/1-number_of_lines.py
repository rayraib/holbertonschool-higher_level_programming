#!/usr/bin/python3
'''open and read file'''


def number_of_lines(filename=""):
    '''calculate the number of lines in filename'''
    line_number = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line_number += 1
        return line_number
