#!/usr/bin/python3
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    '''
        Class containing test methods for function  ``max_integer`` from
        module ``6-max_integer.py``
    '''
    def test_empty_list(self):
        '''Tests an empty list for it's max value'''
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_int_list(self):
        ''' Tests a list of integer, positives, negatives and zeros'''
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_not_int_list(self):
        ''' Tests a lists containing non integer type elements'''
        with self.assertRaises(TypeError):
            max_integer(['s', 'w', 's'])
            max_integer([1, [1, 2]])
            max_integer("hello")
