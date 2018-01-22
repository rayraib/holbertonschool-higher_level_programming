#!/usr/bin/python3
"""
    This file contains external tests for class `Rectangle`
    from the module `rectangle`.
    To use, impor the class `rectangle` and `unittest`
"""
from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangleclass(unittest.TestCase):
    '''
        Class containing test cases for the class Rectangle's to_dict method
        inherits from class Base
    '''
    def test_to_dict(self):
        '''
            test the to_dict method of a rectangle
            should return the object as a dictionary 
        '''
        r1 = Rectangle(10, 2, 1, 9, 8)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 8, 'height': 2, 'width': 10})
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertFalse(r1 == r2)
