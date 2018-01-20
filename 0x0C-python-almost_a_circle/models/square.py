#!/usr/bin/pytho3
'''Moduel containing class Square that inherits from class Rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Represent a square with size that inherits from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''initialize the instance attributes'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''override the Rectangle class's __str__method with new string'''
        return ("[Square] {} {}/{} - {}".format(self.id,
                self.x, self.y, self.width))
