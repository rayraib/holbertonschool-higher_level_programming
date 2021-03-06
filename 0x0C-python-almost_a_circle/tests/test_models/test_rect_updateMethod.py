#!/usr/bin/python3
"""
    This file contains external tests for class Rectangle
    from the module rectangle.
    This tests test the stdout outputs
    To use, import the class Rectangle and unittest
"""
from models.rectangle import Rectangle
from models.base import Base
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from io import StringIO


class test_rect_stdout(unittest.TestCase):
    '''
        Class containing test cases for the Rectangle class's
        update method
    '''
    def test_update_arg(self):
        '''
            Test the update method of Rectangle.
            Each attribute in the *arg is in order of
            ID, Width, Height, X and Y
        '''
        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(8, 9)
        self.assertEqual(str(r), "[Rectangle] (8) 10/10 - 9/10")
        r.update(8, 9, 11)
        self.assertEqual(str(r), "[Rectangle] (8) 10/10 - 9/11")
        r.update(9, 10, 13, 12)
        self.assertEqual(str(r), "[Rectangle] (9) 12/10 - 10/13")
        r.update(9, 10, 13, 12, 14)
        self.assertEqual(str(r), "[Rectangle] (9) 12/14 - 10/13")
        ls = [2, 3, 4]
        r.update(*ls)
        self.assertEqual(str(r), "[Rectangle] (2) 12/14 - 3/4")

    def test_update_kwargs(self):
        '''
            Test update method of Rectanglw with
            **kwargs input, **kwargs is a double pointer to
            a dictionary
        '''

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (10) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_arg_kwargs(self):
        '''
            Test the update method with both *arg
            and **kwargs input
            if *arg exists and not empty, skip **kwarg
        '''
        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")
        r.update(1, 2, x=9)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 2/10")
        r.update(9, x=9)
        self.assertEqual(str(r), "[Rectangle] (9) 10/10 - 2/10")

    def test_update_typeError(self):
        '''
            Test for conditions that raise TypeError with update method
        '''
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(6, 's')
            r.update(5, [1, 2], 2, 4)
            r.update(4, (1, 2), 4, 5)
            r.update(2, {'s': 3}, 6)
            r.update(2, float('nan'))
            r.update(width="hi")
            r.update(width=[1, 2, 3], x=2)
            r.update(height=3, width=(1, ))
            r.update(height=3, width={"s": 3})
            r.update(id=3, width=float('nan'))
            r.update(y=4, width=float('inf'))

    def test_update_typeError(self):
        '''
            Test for conditions that raise TypeError with update method
            test with height is not an int
        '''
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(6, 3, 's')
            r.update(5, 3, [1, 2], 2, 4)
            r.update(4, 3, (1, 2), 4, 5)
            r.update(2, 3, {'s': 3}, 6)
            r.update(2, 3, float('nan'))
            r.update(width=2, height="34")
            r.update(width=2, height=[2, 3])
            r.update(width=2, height=(1, 2))
            r.update(width=2, height={"s": 3})
            r.update(width=2, height=float('nan'))
            r.update(width=2, height=float('inf'))

    def test_update_typeError(self):
        '''
            Test for conditions that raise TypeError with update method
            test with x is not an int
        '''
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(6, 3, 4, 's')
            r.update(5, 3, 4, [1, 2], 2, 4)
            r.update(4, 3, 4, (1, 2), 4, 5)
            r.update(2, 3, 4, {'s': 3}, 6)
            r.update(2, 3, 4, float('nan'))
            r.update(width=2, height=4, x="34")
            r.update(width=2, height=4, x=[2, 3])
            r.update(width=2, height=4, x=(1, 2))
            r.update(width=2, height=4, x={"s": 3})
            r.update(width=2, height=4, x=float('nan'))
            r.update(width=2, height=4, x=float('inf'))

    def test_update_typeError(self):
        '''
            Test for conditions that raise TypeError with update method
            test with y is not an int
        '''
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(6, 3, 4, 5, 's')
            r.update(5, 3, 4, 5, [1, 2], 2, 4)
            r.update(4, 3, 4, 5, (1, 2), 4, 5)
            r.update(2, 3, 4, 5, {'s': 3}, 6)
            r.update(2, 3, 4, 5, float('nan'))
            r.update(width=2, height=4, y="34")
            r.update(width=2, height=4, y=[2, 3])
            r.update(width=2, height=4, y=(1, 2))
            r.update(width=2, height=4, y={"s": 3})
            r.update(width=2, height=4, y=float('nan'))
            r.update(width=2, height=4, y=float('inf'))
