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
        Class containing test cases for the class Rectangle's area method
        inherits from class Base
        T
    '''
    def test_area(self):
        '''
            test the area method of a rectangle
            Should return `width * height`
        '''
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)
        r = Rectangle(2, 10)
        self.assertEqual(r.area(), 20)
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)
