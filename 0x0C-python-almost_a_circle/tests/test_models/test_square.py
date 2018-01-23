#!/usr/bin/python3
"""
    This file contains external tests for class `Square`
    from the module `square`.
    To use, impor the class `square` and `unittest`
"""
from models.square import Square
from models.base import Base
import unittest


class TestSquareclass(unittest.TestCase):
    '''
        Class containing test cases for the class Square that
        inherits from class Base
    '''
    def test_instantiation(self):
        '''
            Test that objects are instantiated from Square class
            Test that the objects are also subclass of Base
        '''
        r1 = Square(10)
        self.assertIsInstance(r1, Square)
        self.assertIsInstance(r1, Base)

    def test_attr_width_height(self):
        '''
            Test if each attribute has been instantiated correctly
        '''
        r1 = Square(10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_attr_x_instan(self):
        '''
            Test if y attribute has been instantiated correctly
        '''
        r2 = Square(10, 2)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 0)

    def test_attr_y_instan(self):
        '''
            Test if y attribute has been instantiated correctly
        '''
        r3 = Square(10, 3, 4)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 10)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)

    def test_attr_id_instan(self):
        '''
            Test if id attribute has been instantiated correctly
        '''
        r4 = Square(10, 3, 4, 7)
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 10)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 4)
        self.assertEqual(r4.id, 7)

    def test_attr_width_type(self):
        '''
            Test that TypeError is raised when:
            -`width`is not int
        '''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square("s", 1)
            r = Square(1.4, 2)
            r = Square({2: 4}, 2)
            r = Square([1, 2], 2)
            r = Square((4, ), 2)
            r = Square(True, 2)
            r = Square(float('nan'), 2)
            r = Square(float('inf'), 2)

    def test_attr_x_type(self):
        '''
            Test that TypeError is raised when:
            -x is not int
        '''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(2, "s")
            r = Square(2, 1.4)
            r = Square(2, {2: 4})
            r = Square(2, [1, 2])
            r = Square(2, (4, ))
            r = Square(2, True)
            r = Square(2, float('nan'))
            r = Square(2, float('inf'))

    def test_attr_y_type(self):
        '''
            Test that TypeError is raised when:
            -y is not int
        '''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(2, 3, "s")
            r = Square(2, 3, 1.4)
            r = Square(2, 3, {2: 4})
            r = Square(2, 3, [1, 2])
            r = Square(2, 3, (4, ))
            r = Square(2, 3, True)

    def test_attr_type(self):
        '''
            Test that TypeError is raised when:
            Instantiate with no required parameter: size
            Instantiate with too many parameters
        '''
        with self.assertRaises(TypeError):
            r = Square()
            r = Square(2, 3, 4, 5, 6, 7, 7, 8)

    def test_attr_width_value(self):
        '''
            test that ValueError is raised when:
            `width` is <= 0,
        '''
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Square(0, 1)
            r = Square(-1, 2)
            r = Square(-3, -3, 3, 3, 3)
            r = Square(1, 0)
            r = Square(2, -4)
            r = Square(3, -3, -3, 3, 3)

    def test_attr_x_value(self):
        '''
            test that ValueError is raised when:
            `x` is < 0,
        '''
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Square(2, -1, 2)
            r = Square(2, -51, -32)

    def test_attr_y_value(self):
        '''
            test that ValueError is raised when:
            `y` is < 0,
        '''
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Square(2, 3, -2)
