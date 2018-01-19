#!/usr/bin/python3
''' Module that describes a rectangle'''
from models.base import Base


class Rectangle(Base):
    ''' Represents a rectangle that inherits from `Base` class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''initialize the private attributes of Rectangle class instances'''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.id = id
        super().__init__(self.id)

    @property
    def width(self):
        ''' return the value of private attribute __width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set the value of the private attribute __width'''
        self.__width = value

    @property
    def height(self):
        ''' return the value of private attribute __height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set the value of the private attribute __height'''
        self.__height = value

    @property
    def x(self):
        ''' return the value of private attribute __x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''set the value of the private attribute __x'''
        self.__x = value

    @property
    def y(self):
        ''' return the value of private attribute __y'''
        return self.__y

    @height.setter
    def y(self, value):
        '''set the value of the private attribute __y'''
        self.__y = value
