#!/usr/bin/python3
'''
    search and update
'''


def append_after(filename="", search_string="", new_string=""):
    '''insert a line of text to a file, after each line containing
        a specific string.
    '''
    with open(filename, 'r', encoding='UTF-8') as f:
        upd_str = ""
        for line in f:
            if line.find(search_string) != -1:
                upd_str += line + new_string
            else:
                upd_str += line
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(upd_str)
