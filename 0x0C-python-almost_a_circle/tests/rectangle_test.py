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

    def test_attr_type(self):
        '''
            Raises TypeError when:
            - `width`, height, x and y are not int
            - no arg value is given during instantiation
        '''
        with self.assertRaisesRegexp(TypeError, "width must be an integer"):
            r = Rectangle("s", 1)
            r = Rectangle(1.4, 2)
            r = Rectangle({2: 4}, 2)
            r = Rectangle([1, 2], 2)
            r = Rectangle((4, ), 2)
            r = Rectangle(True, 2)

        with self.assertRaisesRegexp(TypeError, "height must be an integer"):
            r = Rectangle(2, "s")
            r = Rectangle(2, 1.4)
            r = Rectangle(2, {2: 4})
            r = Rectangle(2, [1, 2])
            r = Rectangle(2, (4, ))
            r = Rectangle(2, True)

        with self.assertRaisesRegexp(TypeError, "x must be an integer"):
            r = Rectangle(2, 3,  "s")
            r = Rectangle(2, 3,  1.4)
            r = Rectangle(2, 3, {2: 4})
            r = Rectangle(2, 3, [1, 2])
            r = Rectangle(2, 3, (4, ))
            r = Rectangle(2, 3, True)

        with self.assertRaisesRegexp(TypeError, "y must be an integer"):
            r = Rectangle(2, 3, 4, "s")
            r = Rectangle(2, 3, 4, 1.4)
            r = Rectangle(2, 3, 4, {2: 4})
            r = Rectangle(2, 3, 4, [1, 2])
            r = Rectangle(2, 3, 4, (4, ))
            r = Rectangle(2, 3, 4, True)

        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_attr_value(self):
        '''Raise ValueError when:
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
