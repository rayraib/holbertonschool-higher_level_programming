#!/usr/bin/python3
class Rectangle:
    '''Define a rectangle of width and height'''
    def __init__(self, width=0, height=0):
        '''Initialize values for an instance of Rectangle'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''getter method for width'''
        return self.__width__

    @width.setter
    def width(self, value):
        '''Setter method for width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width__ = value

    @property
    def height(self):
        '''returns value of the height attribute'''
        return self.__height__

    @height.setter
    def height(self, value):
        '''set value of the instance attribute height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height__ = value
