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
            self.assertEqual(result,
                     [{"y": 8, "x": 2, "id": 9, "width": 10, "height": 7}])
        r2 = Rectangle(2, 4)
        r2.update(id=99)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as file:
            result = file.read()
            result = Rectangle.from_json_string(result)
            self.assertEqual(result, [{"y": 0, "x": 0, "id": 99, "width": 2, "height": 4}])

    def test_from_json_to(self):
        '''
            test the class method that returns a list of json string representation
        '''
        list_input = [
                    {'id': 89, 'width': 10, 'height': 4},
                    {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}])
        self.assertEqual(type(list_output), list)

    def test_create(self):
        '''
            test the create class method
            return an instance with set attributes
        '''
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        r1 = Rectangle(3, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        r1 = Rectangle(3, 5, 3, 4, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)

    def test_load_from_file(self):
        '''
            test method for the Class method load_from_file
        '''
        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        for rect in list_rectangles_output:
            self.assertEqual(str(rect), str(r1)) 
