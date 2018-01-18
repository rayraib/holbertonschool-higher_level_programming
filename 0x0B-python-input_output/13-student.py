#!/usr/bin/python3
'''Student to disk and reload'''


class Student:
    ''' represents a student'''
    def __init__(self, first_name, last_name, age):
        '''initialize the instance variables'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves dicitonary representation of a Student'''
        att_dict = self.__dict__
        new_dict = {}
        if attrs is not None:
            for item in attrs:
                for key, value in att_dict.items():
                    if item == key:
                        new_dict[key] = value
            return new_dict
        else:
            return att_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
