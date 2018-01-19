#!/usr/bin/python3
'''
    Base class for geomtric shapes
'''


class Base:
    '''
        Defines a base class that other geometric shapes can inherit from
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' initialize public instnace attribute `id` '''
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
