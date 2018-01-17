#!/usr/bin/python3
''' read a file'''


def read_lines(filename="", nb_lines=0):
    '''read n number of lines from file filename'''
    with open(filename, 'r', encoding='utf-8') as f:
        i = 1
        line = f.readline()
        while (i <= nb_lines or nb_lines <= 0 and line != ""):
            print (line, end="") 
            line = f.readline()
            i += 1
