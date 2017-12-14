#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for c in my_list:
        if c != search:
            new_list.append(c)
        else:
            new_list.append(replace)
    return (new_list)
