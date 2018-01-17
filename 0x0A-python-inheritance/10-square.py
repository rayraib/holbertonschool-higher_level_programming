#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
'''Subclass of Rectangle'''


class Square(Rectangle):
    '''represents a square'''
    def __init__(self, size):
        '''initialize instance attributes'''
        super().__init__(size, size)
        Rectangle.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        ''' calculate area of the square instance'''
        return (self.__size * self.__size)
