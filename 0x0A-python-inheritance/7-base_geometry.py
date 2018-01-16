#!/usr/bin/python3
'''Base class for geometry shapes'''


class BaseGeometry:
    '''base class geometry'''
    def area(self):
        ''' area of  geometric shape'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validate if the value is an int'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
