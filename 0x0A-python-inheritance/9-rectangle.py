#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
'''
    subclass of BaseGeometry class
'''


class Rectangle(BaseGeometry):
    ''' representation of a rectangle'''
    def __init__(self, width, height):
        '''initialize the object attributes'''
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width

    def area(self):
        ''' calculate area of the rectangle'''
        return (self.__height * self.__width)

    def __str__(self):
        '''return informal string represention of the object itself'''
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
