#!/usr/bin/python3
"""
    This file contains external tests for class `Rectangle`
    from the module `rectangle`.
    To use, impor the class `rectangle` and `unittest`
"""
from models.rectangle import Rectangle
from models.base import Base
import unittest
import sys
from unittest.mock import MagicMock 
from unittest.mock import patch
from io import StringIO

class TestRectangleclass(unittest.TestCase):
    '''
        Class containing test cases for the class Rectangle that
        inherits from class Base
    '''
    def test_instantiation(self):
        ''' 
            Test that objects are instantiated from Rectangle class
            Test that the objects are also subclass of Base 
        '''
        r1 = Rectangle(10, 2)
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r1, Base)

    def test_attr_inst(self):
        ''' 
            Test if each attribute has been instantiated correctly
        '''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(10, 2, 3, )
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(10, 2, 3, 4)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)

        r4 = Rectangle(10, 2, 3, 4, 19)
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 4)
        self.assertEqual(r4.id, 19)

    def test_attr_type(self):
        '''
            Test that TypeError is raised when:
            -`width`, height, x and y are not int
        '''
        with self.assertRaisesRegexp(TypeError, "width must be an integer"):
            r = Rectangle("s", 1)
            r = Rectangle(1.4, 2)
            r = Rectangle({2: 4}, 2)
            r = Rectangle([1, 2], 2)
            r = Rectangle((4, ), 2)
            r = Rectangle(True, 2)
            r = Rectangle(float('nan'), 2)
            r = Rectangle(float('inf'), 2)

        with self.assertRaisesRegexp(TypeError, "height must be an integer"):
            r = Rectangle(2, "s")
            r = Rectangle(2, 1.4)
            r = Rectangle(2, {2: 4})
            r = Rectangle(2, [1, 2])
            r = Rectangle(2, (4, ))
            r = Rectangle(2, True)
            r = Rectangle(3, float('nan'))
            r = Rectangle(3, float('inf'), 2)

        with self.assertRaisesRegexp(TypeError, "x must be an integer"):
            r = Rectangle(2, 3,  "s")
            r = Rectangle(2, 3,  1.4)
            r = Rectangle(2, 3, {2: 4})
            r = Rectangle(2, 3, [1, 2])
            r = Rectangle(2, 3, (4, ))
            r = Rectangle(2, 3, True)
            r = Rectangle(2, 3, float('nan'))
            r = Rectangle(2, 3, float('inf'))

        with self.assertRaisesRegexp(TypeError, "y must be an integer"):
            r = Rectangle(2, 3, 4, "s")
            r = Rectangle(2, 3, 4, 1.4)
            r = Rectangle(2, 3, 4, {2: 4})
            r = Rectangle(2, 3, 4, [1, 2])
            r = Rectangle(2, 3, 4, (4, ))
            r = Rectangle(2, 3, 4, True)

        with self.assertRaises(TypeError):
            '''
                Instantiate with no required parameter: width and height
                Instantiate with only one parameter
                Instantiate with too many parameters
            '''
            r = Rectangle()
            r = Rectangle(1)
            r = Rectangle(2, 3, 4, 5, 6, 7, 7, 8)

    def test_attr_value(self):
        '''
            test that ValueError is raised when:
            `width` and `height` are <= 0,
            `x` and `y` are < 0
        '''
        with self.assertRaisesRegexp(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)
            r = Rectangle(-1, 2)
            r = Rectangle(-3, -3, 3, 3, 3)

        with self.assertRaisesRegexp(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)
            r = Rectangle(2, -4)
            r = Rectangle(3, -3, -3, 3, 3)

        with self.assertRaisesRegexp(ValueError, "x must be >= 0"):
            r = Rectangle(2, 3, -1, 2)
            r = Rectangle(2, 3, -51, -3)

        with self.assertRaisesRegexp(ValueError, "y must be >= 0"):
            r = Rectangle(2, 3, 1, -2)

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

    def test_to_dict(self):
        '''
            test the to_dict method of a rectangle
            should return the object as a dictionary 
        '''
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
        self.asserEqual(type(r1_dictionary), "<class 'dict'>")
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertFalse(r1 == r2)
