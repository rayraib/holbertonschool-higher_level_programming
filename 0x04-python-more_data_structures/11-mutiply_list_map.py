#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    num_list = [number] * len(my_list)
    return (list(map(lambda val, num: val * num, my_list, num_list)))
