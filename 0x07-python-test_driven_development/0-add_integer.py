#!/usr/bin/python3
def add_integer(a, b):
    '''
        Add two integers, if floats, cast into int then add
    '''
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    else:
        return (a + b)
