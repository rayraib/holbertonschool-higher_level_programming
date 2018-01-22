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
        print(r)
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
