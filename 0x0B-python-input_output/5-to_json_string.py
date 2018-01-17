#!/usr/bin/python3
import json
'''JSON representation'''



def to_json_string(my_obj):
    ''' return JSON representation of the my_obj'''
    x = json.dumps(my_obj)
    return x
