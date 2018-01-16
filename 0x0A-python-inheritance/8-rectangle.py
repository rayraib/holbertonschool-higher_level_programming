#!/usr/bin/python3
''' subclass of BaseGeometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' representation of a rectangle'''
    def __init__(self, width, height):
        '''initialize the object attributes'''
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
