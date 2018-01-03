#!/usr/bin/python3
class Square():
    '''Represent a square'''
    def __init__(self, size=0):
        '''Initialize data for each instances'''
        if (isinstance(size, int) is False):
            print("size must be an integer")
            raise TypeError
        elif size < 0:
            print("size must be >= 0")
            raise ValueError
        else:
            self.__size = size

    def area(self):
        '''Calculate area of the square object'''
        return (self.__size * self.__size)
