#!/usr/bin/python3
import json
'''JSON string to object'''


def from_json_string(my_str):
    '''return an object(Python data structure) represented by a JSON string'''
    data = json.loads(my_str)
    return (data)
