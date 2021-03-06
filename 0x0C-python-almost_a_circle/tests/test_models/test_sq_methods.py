#!/usr/bin/python3
"""
    This file contains external tests for class Square
    from the module square.
    This tests test the stdout outputs
    To use, import the class Square and unittest
"""
from models.square import Square
from models.base import Base
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from io import StringIO


class test_rect_stdout(unittest.TestCase):
    '''
        Class containing test cases for the Square class's
        methods
    '''
    def test_update_arg(self):
        '''
            Test the update method of Square.
            Each attribute in the *arg is in order of
            ID, Width, Height, X and Y
        '''
        r = Square(10, 10, 10, 10)
        self.assertEqual(str(r), "[Square] (10) 10/10 - 10")
        r.update(89)
        self.assertEqual(str(r), "[Square] (89) 10/10 - 10")
        r.update(8, 9)
        self.assertEqual(str(r), "[Square] (8) 10/10 - 9")
        r.update(8, 9, 11)
        self.assertEqual(str(r), "[Square] (8) 11/10 - 9")
        r.update(9, 10, 13, 12)
        self.assertEqual(str(r), "[Square] (9) 13/12 - 10")
        r.update(9, 13, 12, 14)
        self.assertEqual(str(r), "[Square] (9) 12/14 - 13")
        ls = [2, 3, 4]
        r.update(*ls)
        self.assertEqual(str(r), "[Square] (2) 4/14 - 3")

    def test_update_kwargs(self):
        '''
            Test update method of Rectanglw with
            **kwargs input, **kwargs is a double pointer to
            a dictionary
        '''

        r = Square(10, 10, 10, 10)
        self.assertEqual(str(r), "[Square] (10) 10/10 - 10")
        r.update(height=1)
        self.assertEqual(str(r), "[Square] (10) 10/10 - 10")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Square] (10) 2/10 - 1")
        r.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(r), "[Square] (89) 3/1 - 2")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Square] (89) 1/3 - 4")
        r.update(size=3)
        self.assertEqual(str(r), "[Square] (89) 1/3 - 3")

    def test_update_arg_kwargs(self):
        '''
            Test the update method with both *arg
            and **kwargs input
            if *arg exists and not empty, skip **kwarg
        '''
        r = Square(10, 10, 10, 10)
        self.assertEqual(str(r), "[Square] (10) 10/10 - 10")
        r.update(1, 2, x=9)
        self.assertEqual(str(r), "[Square] (1) 10/10 - 2")
        r.update(9, x=9)
        self.assertEqual(str(r), "[Square] (9) 10/10 - 2")

    def test_update_wdth_typeError(self):
        '''
            Test for conditions that raise TypeError with update method
        '''
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update('s')
            r.update(1.5)
            r.update([1, 2], 2, 4)
            r.update((1, 2), 4, 5)
            r.update({'s': 3}, 6)
            r.update(float('nan'))
            r.update(width="hi")
            r.update(size="hi")
            r.update(width=[1, 2, 3], x=2)
            r.update(width=(1, ))
            r.update(width={"s": 3})
            r.update(id=3, width=float('nan'))
            r.update(y=4, width=float('inf'))

    def test_update_hei_typeError(self):
        '''
            Test for conditions that raise TypeError with update method
            test with height is not an int
        '''
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(6, 1.5)
            r.update(6, 's')
            r.update(5, [1, 2], 2, 4)
            r.update(4, (1, 2), 4, 5)
            r.update(2, {'s': 3}, 6)
            r.update(2, float('nan'))
            r.update(width=2, height="34")
            r.update(width=2, height=[2, 3])
            r.update(width=2, height=(1, 2))
            r.update(width=2, height={"s": 3})
            r.update(width=2, height=float('nan'))
            r.update(width=2, height=float('inf'))

    def test_update_x_typeError(self):
        '''
            Test for conditions that raise TypeError with update method
            test with x is not an int
        '''
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(6, 4, 's')
            r.update(6, 4, 1.5)
            r.update(5, 4, [1, 2])
            r.update(4, 4, (1, 2))
            r.update(2, 4, {'s': 3}, 6)
            r.update(2, 4, float('nan'))
            r.update(width=2, y=7, x="34")
            r.update(width=2, x=[2, 3])
            r.update(width=2, x=(1, 2))
            r.update(width=2, x={"s": 3})
            r.update(width=2, x=float('nan'))
            r.update(width=2, x=float('inf'))

    #def test_update_y_typeError(self):
        '''
            Test for conditions that raise TypeError with update method
            test with y is not an int
        '''
        '''
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(6, 5, 's')
            r.update(5, 5, [1, 2], 2, 4)
            r.update(4, 5, (1, 2), 4, 5)
            r.update(2, 5, {'s': 3}, 6 )
            r.update(2, 5, float('nan'))
            r.update(width=2, y="34")
            r.update(height=4, y=[2, 3])
            r.update(height=4, y=(1, 2))
            r.update(width=2, y={"s": 3})
            r.update(width=2, y=float('nan'))
            r.update(y=float('inf'))

        '''
    def test_to_dict(self):
        '''
            test the to_dict method of a rectangle
            should return the object as a dictionary
        '''
        r1 = Square(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 2, 'y': 1, 'id': 9, 'size': 10})
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Square(1, 1)
        r2.update(**r1_dictionary)
        self.assertFalse(r1 == r2)

    def test_str(self):
        '''
            test the __str__ method of the Square class
        '''
        result = str(Square(4, 6, 2, 1))
        self.assertEqual(result, "[Square] (1) 6/2 - 4")
        result = str(Square(5, 5, 1, 2))
        self.assertEqual(result, "[Square] (2) 5/1 - 5")

    def test_display_method(self):
        '''
            test the display method of Square class
            - Should display the rectangle with #
            - x if horizontal spaces
            - y is for vertical spaces
        '''
        with patch('sys.stdout', new=StringIO()) as fakeOutPut:
            r = Square(2, 3, 2)
            r.display()
            self.assertEqual(fakeOutPut.getvalue(), "\n\n   ##\n   ##\n")

        with patch('sys.stdout', new=StringIO()) as fakeOutPut:
            r = Square(3, 2, 1)
            r.display()
            self.assertEqual(fakeOutPut.getvalue(), "\n  ###\n  ###\n  ###\n")

        with patch('sys.stdout', new=StringIO()) as fakeOutPut:
            r = Square(1)
            r.display()
            self.assertEqual(fakeOutPut.getvalue(), "#\n")

        with patch('sys.stdout', new=StringIO()) as fakeOutPut:
            r = Square(2, 2, 3, 3)
            r.display()
            self.assertEqual(fakeOutPut.getvalue(), "\n\n\n  ##\n  ##\n")

    def test_area(self):
        '''
            test the area method of a rectangle
            Should return size * size`
        '''
        r = Square(3, 2)
        self.assertEqual(r.area(), 9)
        r = Square(2, 10)
        self.assertEqual(r.area(), 4)
        r = Square(8, 7, 0, 0)
        self.assertEqual(r.area(), 64)
        r = Square(1)
        self.assertEqual(r.area(), 1)
