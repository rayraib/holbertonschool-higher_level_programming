#!/usr/bin/python3
def best_score(my_dict):
    if my_dict:
        value_list = list(my_dict.values())
        return (max(value_list))
    return None
