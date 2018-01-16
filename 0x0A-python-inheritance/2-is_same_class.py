#!/usr/bin/python3
'''Check the the class of an object'''


def is_same_class(obj, a_class):
    '''check if the obj is an instance of the given class'''
    if type(obj) is a_class:
        return True
    else:
        return False
