#!/usr/bin/python3
"""
    This is a file containing external tests associated with `base.py`
    First, import the class `Base`
    from `base` as `Base` and `unittest`
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    '''
        Class containing test methods for Base class
    '''
    def test_instantiation(self):
        '''tests instantiation of Baseclass'''
        b0 = Base(0)
        self.assertEqual(b0.id, 0)
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_inheritence(self):
        ''' check that the instance is an instance of Base class
        '''
        b1 = Base(1)
        self.assertIsInstance(b1, Base)

    def test_nb_increment(self):
        ''' test incrementation of the __nb_objects attribute
            when no arg is sent
        '''
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base()
        self.assertEqual(b4.id, 4)
        b5 = Base(9)
        self.assertEqual(b5.id, 9)
