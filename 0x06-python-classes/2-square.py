#!/usr/bin/python3
class Square():
    """Represent a square with size size"""
    def __init__(self, size=0):
        '''Initialize the data'''
        if (isinstance(size, int) is False):
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >=0", end="")
            raise ValueError
        else:
            self.__size = size
