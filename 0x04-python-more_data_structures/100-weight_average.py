#!/usr/bin/python3
def weight_average(my_list=[]):
    divisor = 0
    result = 0
    for tup in my_list:
        divisor += tup[1]
        result += tup[0] * tup[1]
    result /= divisor
    return result
