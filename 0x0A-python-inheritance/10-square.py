#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
'''Subclass of Rectangle'''


class Square(Rectangle):
    '''represents a square'''
    def __init__(self, size):
        '''initialize instance attributes'''
        Rectangle.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        ''' calculate area of the square instance'''
        return (self.__size * self.__size)

    def __str__(self):
        '''create informal string representation of the object itself'''
        return ("[Square] {}/{}".format(self.__size, self.__size))
