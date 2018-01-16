#!/usr/bin/python3
'''check if the object is an instance of a specified class'''


def is_kind_of_class(obj, a_class):
    '''check if obj is an instance of a_class'''
    if isinstance(obj, a_class):
        return True
    else:
        return False
