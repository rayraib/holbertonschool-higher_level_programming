#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) > 0 and my_list is not None:
        for i in range(len(my_list) + 1):
            if i == 0:
                continue
            print("{:d}".format(my_list[-i]))
