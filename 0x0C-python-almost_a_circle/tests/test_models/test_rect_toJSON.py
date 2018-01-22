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
            Test the to_json method of the Rectangle's superclass
        '''
        r1 = Rectangle(10, 7, 2, 8, 9)
        dictionary = r1.to_dictionary()
        json_dictionary = r1.to_json_string([dictionary])
        self.assertEqual(type(dictionary), dict)
        d = r1.from_json_string(json_dictionary)
        self.assertEqual(d, [dictionary])
        self.assertEqual(type(json_dictionary), str)

    def test_savetofile_method(self):
        '''
            test the class method save_to_file:
            write JSON string to a file
        '''
        r1 = Rectangle(10, 7, 2, 8, 9)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            result = file.read()
            result = Rectangle.from_json_string(result)
            self.assertEqual(result, [{"y": 8, "x": 2, "id": 9, "width": 10, "height": 7}])
        r2 = Rectangle(2, 4)
        r2.update(id=99)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as file:
            result = file.read()
            result = Rectangle.from_json_string(result)
            self.assertEqual(result, [{"y": 0, "x": 0, "id": 99, "width": 2, "height": 4}])

    def test_from_json_to_string(self):
        '''
            test the class method that returns a list of json string representation
        '''
        pass
