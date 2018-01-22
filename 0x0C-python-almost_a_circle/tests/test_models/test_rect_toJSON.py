#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
'''
    This file contains external tests for the class Rectangle from module
    rectangle.py
'''


class test_class_method(unittest.TestCase):
    '''
        Class containing test cases for the class method of the
        Rectangle class
    '''
    def test_tojson_method(self):
        '''
            Test the to_json metho of the Rectangle's superclass
        '''
        r1 = Rectangle(10, 7, 2, 8, 9)
        dictionary = r1.to_dictionary()
        json_dictionary = r1.to_json_string([dictionary])
        self.assertEqual(dictionary, {'x': 2, 'width': 10, 'id': 9, 'height': 7, 'y': 8})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(json_dictionary, '[{"x": 2, "width": 10, "id": 9, "height": 7, "y": 8}]')
        self.assertEqual(type(json_dictionary), str)

