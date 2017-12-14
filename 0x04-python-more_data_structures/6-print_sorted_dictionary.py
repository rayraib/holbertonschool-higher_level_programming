#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for k, v in sorted(my_dict.items()):
        print("{}: {}".format(k, v))
