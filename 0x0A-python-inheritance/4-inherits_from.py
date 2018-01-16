#!/usr/bin/python3
'''check if the class of the object is directly or indirectly inherited
    from a specified class
'''


def inherits_from(obj, a_class):
    '''check if class of obj is inherited from a_class'''
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
