#!/usr/bin/python3
import json
'''
    Base class for geomtric shapes
'''


class Base(object):
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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''convert list_dictionaries to json string and return'''
        if list_dictionaries is None:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_obs to file'''
        if list_objs is None:
            list_objs = []
        s_list = []
        for obj in list_objs:
            obj = obj.to_dictionary()
            s_list.append(obj)
        json_string = cls.to_json_string(s_list)
        filename = "Rectangle.json"
        with open(filename, 'w+', encoding="UTF-8") as f:
            f.write(json_string)
