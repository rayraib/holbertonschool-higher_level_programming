#!/usr/bin/python3
"""
    This file contains external tests for class Rectangle
    from the module rectangle.
    This tests pertains to the to_dict method of Rectangle class
    To use, import the class Rectangle and unittest
"""
from models.rectangle import Rectangle
from models.base import Base
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from io import StringIO


class test_to_dict(unittest.TestCase):
    '''
        Class containing test cases for the Rectangle class
        Test to_dict method of the Rectangle class
    '''
    r1 = Rectangle(10, 2, 1, 9)

