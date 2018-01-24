#!/usr/bin/python3
'''
    Moduel containing class Square that inherits from class Rectangle
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Represent a square with size that inherits from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''initialize the instance attributes'''
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        '''return the size value of square'''
        return self.width

    @size.setter
    def size(self, size):
        '''set the value of size'''
        self.width = size
        self.height = size

    def __str__(self):
        '''override the Rectangle class's __str__method with new string'''
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        '''update the values of the square class's attributes'''
        if len(args) != 0:
            att_list = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, att_list[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''return the object as a dictionary'''
        new_dict = {}
        att_list = ["id", "size", "x", "y"]
        for key in att_list:
            value = getattr(self, key)
            new_dict[key] = value
        return new_dict
