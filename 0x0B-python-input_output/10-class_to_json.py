#!/usr/bin/python3
'''class to JSON'''


def class_to_json(obj):
    '''
        return the dictionary description with simple data structure
        for JSOn serialization of an object
    '''
    new_dict = obj.__dict__
    return new_dict
