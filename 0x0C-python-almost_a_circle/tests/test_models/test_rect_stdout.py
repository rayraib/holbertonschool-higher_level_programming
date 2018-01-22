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
        Class containing test cases for the Rectangle class
    '''
    def test_str(self):
        '''
            test the __str__ method of the Rectangle class
        '''
        result = str(Rectangle(4, 6, 2, 1, 12))
        self.assertEqual(result, "[Rectangle] (12) 2/1 - 4/6")
        result = str(Rectangle(5, 5, 1, 2, 3))
        self.assertEqual(result, "[Rectangle] (3) 1/2 - 5/5")

    def test_display_method(self):
        '''
            test the display method of Rectangle class
            - Should display the rectangle with #
            - x if horizontal spaces
            - y is for vertical spaces
        '''
        with patch('sys.stdout', new=StringIO()) as fakeOutPut:
            r = Rectangle(2, 3, 2, 2)
            r.display()
            self.assertEqual(fakeOutPut.getvalue(), "\n\n  ##\n  ##\n  ##\n")

        with patch('sys.stdout', new=StringIO()) as fakeOutPut:
            r = Rectangle(3, 2, 1, 0)
            r.display()
            self.assertEqual(fakeOutPut.getvalue(), " ###\n ###\n")

        with patch('sys.stdout', new=StringIO()) as fakeOutPut:
            r = Rectangle(1, 1)
            r.display()
            self.assertEqual(fakeOutPut.getvalue(), "#\n")

        with patch('sys.stdout', new=StringIO()) as fakeOutPut:
            r = Rectangle(2, 2, 3)
            r.display()
            self.assertEqual(fakeOutPut.getvalue(), "   ##\n   ##\n")
