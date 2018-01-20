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
        Class containing test cases for the class Rectangle that
        inherits from class Base
    '''
    def test_instantiation(self):
        ''' Test that objects are instantiated of Rectangle class'''
        r1 = Rectangle(10, 2)
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r1, Base)

    def test_attr_inst(self):
        ''' test if each attribute has been instantiated correctly'''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(10, 2, 3, )
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 3, 4)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)
        self.assertEqual(r3.id, 3)

        r4 = Rectangle(10, 2, 3, 4, 19)
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 4)
        self.assertEqual(r4.id, 19)

        with self.assertRaises(TypeError):
            r = Rectangle()
