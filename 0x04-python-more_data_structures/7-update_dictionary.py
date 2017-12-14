#!/usr/bin/python3
def update_dictionary(my_dict, key, value):
    for k in my_dict.items():
        if k == key:
            my_dict[k] = value
    my_dict[key] = value
    return my_dict
