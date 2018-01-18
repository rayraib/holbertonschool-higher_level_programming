#!/usr/bin/python3
'''Student to JSON'''


class Student:
    ''' represents a student'''
    def __init__(self, first_name, last_name, age):
        '''initialize the instance variables'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''retrieves dicitonary representation of a Student'''
        att_dict = self.__dict__
        return att_dict
