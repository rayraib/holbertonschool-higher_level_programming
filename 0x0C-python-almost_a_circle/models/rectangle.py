#!/usr/bin/python3
''' Module that describes a rectangle'''
from models.base import Base


class Rectangle(Base):
    ''' Represents a rectangle that inherits from `Base` class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''initialize the private attributes of Rectangle class instances'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' return the value of private attribute __width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set the value of the private attribute __width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        ''' return the value of private attribute __height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set the value of the private attribute __height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        ''' return the value of private attribute __x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''set the value of the private attribute __x'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        ''' return the value of private attribute __y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''set the value of the private attribute __y'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
