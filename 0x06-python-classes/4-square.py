#!/usr/bin/python3
class Square():
    '''Represent a square'''
    def __init__(self, size=0):
        '''Initialize the data'''
        self.size = size

    @property
    def size(self):
        '''Getter method - Get the __size field'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter method- Set the __size field'''
        if (isinstance(value, int) is False):
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise TypeError
        else:
            self.__size = value

    def area(self):
        '''Calculate area of square object'''
        return (self.__size * self.__size)
