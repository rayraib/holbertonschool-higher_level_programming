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
        if list_dictionaries is None or len(list_dictionaries) == 0:
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
        filename = type(list_objs[0]).__name__ + ".json"
        with open(filename, 'w+', encoding="UTF-8") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        '''convert from json string to JSON representation'''
        if json_string is None or len(json_string) == 0:
            return []
        return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        '''create and return an instance with all attribute set'''
        new_ins = cls(2, 3, 4)
        new_ins.update(**dictionary)
        return(new_ins)

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        obj_list = []
        try:
            with open('Rectangle.json', 'r', encoding='UTF-8') as f:
                content = f.read()
                obj_l = cls.from_json_string(content)
                for ins_dict in obj_l:
                    obj_list.append(cls.create(**ins_dict))
                return obj_list
        except FileNotFoundError:
            return obj_list
