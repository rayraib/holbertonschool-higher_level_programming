#!/usr/bin/python3
def print_square(size):
    '''
        Prnt square of ``size`` size
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(size):
            print("#" * size)
