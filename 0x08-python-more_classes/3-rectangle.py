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
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter method for width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''returns value of the height attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set value of the instance attribute height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''return the area of a Rectangle'''
        return (self.width * self.height)

    def perimeter(self):
        '''return the perimeter of a Rectangle'''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        '''print a rectangle of width and height with '#' character'''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return_value = ""
            for i in range(self.height):
                return_value += ("#" * self.width)
                if i != (self.height - 1):
                    return_value += '\n'
            return return_value
