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

    def test_attr_width_height(self):
        '''
            Test if each attribute has been instantiated correctly
        '''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_attr_x_instan(self):
        '''
            Test if x and y attribute has been instantiated correctly
        '''
        r2 = Rectangle(10, 2, 3)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 0)

    def test_attr_y_instan(self):
        '''
            Test if y attribute has been instantiated correctly
        '''
        r3 = Rectangle(10, 2, 3, 4)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)

    def test_attr_id_instan(self):
        '''
            Test if id attribute has been instantiated correctly
        '''
        r3 = Rectangle(10, 2, 3, 4)
        r4 = Rectangle(10, 2, 3, 4, 19)
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 4)
        self.assertEqual(r4.id, 19)

    def test_attr_width_type(self):
        '''
            Test that TypeError is raised when:
            -`width`, height, x and y are not int
        '''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("s", 1)
            r = Rectangle(1.4, 2)
            r = Rectangle({2: 4}, 2)
            r = Rectangle([1, 2], 2)
            r = Rectangle((4, ), 2)
            r = Rectangle(True, 2)
            r = Rectangle(float('nan'), 2)
            r = Rectangle(float('inf'), 2)

    def test_attr_height_type(self):
        '''
            Test that TypeError is raised when:
            -height is not int
        '''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(2, "s")
            r = Rectangle(2, 1.4)
            r = Rectangle(2, {2: 4})
            r = Rectangle(2, [1, 2])
            r = Rectangle(2, (4, ))
            r = Rectangle(2, True)
            r = Rectangle(3, float('nan'))
            r = Rectangle(3, float('inf'), 2)

    def test_attr_x_type(self):
        '''
            Test that TypeError is raised when:
            -x is not int
        '''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(2, 3,  "s")
            r = Rectangle(2, 3,  1.4)
            r = Rectangle(2, 3, {2: 4})
            r = Rectangle(2, 3, [1, 2])
            r = Rectangle(2, 3, (4, ))
            r = Rectangle(2, 3, True)
            r = Rectangle(2, 3, float('nan'))
            r = Rectangle(2, 3, float('inf'))

    def test_attr_y_type(self):
        '''
            Test that TypeError is raised when:
            -y is not int
        '''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(2, 3, 4, "s")
            r = Rectangle(2, 3, 4, 1.4)
            r = Rectangle(2, 3, 4, {2: 4})
            r = Rectangle(2, 3, 4, [1, 2])
            r = Rectangle(2, 3, 4, (4, ))
            r = Rectangle(2, 3, 4, True)

    def test_attr_type(self):
        '''
            Test that TypeError is raised when:
            Instantiate with no required parameter: width and height
            Instantiate with only one parameter
            Instantiate with too many parameters
        '''
        with self.assertRaises(TypeError):
            r = Rectangle()
            r = Rectangle(1)
            r = Rectangle(2, 3, 4, 5, 6, 7, 7, 8)

    def test_attr_width_value(self):
        '''
            test that ValueError is raised when:
            `width` is <= 0,
        '''
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)
            r = Rectangle(-1, 2)
            r = Rectangle(-3, -3, 3, 3, 3)

    def test_attr_height_value(self):
        '''
            test that ValueError is raised when:
            `height` is <= 0,
        '''
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)
            r = Rectangle(2, -4)
            r = Rectangle(3, -3, -3, 3, 3)

    def test_attr_x_value(self):
        '''
            test that ValueError is raised when:
            `x` is < 0,
        '''
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(2, 3, -1, 2)
            r = Rectangle(2, 3, -51, -3)

    def test_attr_y_value(self):
        '''
            test that ValueError is raised when:
            `y` is < 0,
        '''
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
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

    def test_to_dict(self):
        '''
            test the to_dict method of a rectangle
            should return the object as a dictionary
        '''
        r1 = Rectangle(10, 2, 1, 9, 8)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9,
                         'id': 8, 'height': 2, 'width': 10})
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertFalse(r1 == r2)

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
