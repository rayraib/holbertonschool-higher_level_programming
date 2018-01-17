#!/usr/bin/python3
import json
'''create object form JSON file'''


def load_from_json_file(filename):
    '''creates an object from "JSON file"'''
    with open(filename) as f:
        data = json.load(f)
        return data
