#!/usr/bin/python3
import unittest
from models.square import Square
from models.base import Base
'''
    This file contains external tests for the class Square from module
    square.py
'''


class test_class_method(unittest.TestCase):
    '''
        Class containing test cases for the class method of the
        Square class
    '''
    def test_tojson_method(self):
        '''
            Test the to_json method of the Square's superclass
        '''
        r1 = Square(10, 7, 2, 8)
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
        r1 = Square(10, 7, 8, 9)
        Square.save_to_file([r1])
        with open("Square.json", "r") as file:
            result = file.read()
            result = Square.from_json_string(result)
            self.assertEqual(result, [{"y": 8, "x": 7, "id": 9, "size": 10}])
        r2 = Square(2, 4)
        r2.update(id=99)
        Square.save_to_file([r2])
        with open("Square.json", "r") as file:
            result = file.read()
            result = Square.from_json_string(result)
            self.assertEqual(result, [{"y": 0, "x": 4, "id": 99, "size": 2}])

    def test_from_json_to(self):
        '''
            test the class method that returns
            a list of json string representation
        '''
        list_input = [
            {'id': 89, "size": 4},
            {'id': 7, "size": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'size': 4, 'id': 89},
                         {'size': 7, 'id': 7}])
        self.assertEqual(type(list_output), list)

    def test_create(self):
        '''
            test the create class method
            return an instance with set attributes
        '''
        r1 = Square(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        r1 = Square(3, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        r1 = Square(3, 5, 3, 4)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)

    def test_load_from_file(self):
        '''
            test method for the Class method load_from_file
        '''
        r1 = Square(10, 7, 2, 8)
        list_squares_input = [r1]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        for rect in list_squares_output:
            self.assertEqual(str(rect), str(r1))
