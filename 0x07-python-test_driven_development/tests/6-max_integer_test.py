#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def check_max(self):
        self.assertEqual(max_integer([1, 3]), 3)
        self.assertEqual(max_integer([6, 3, 65, 77]), 77)
        self.assertEqual(max_integer(), None)

    def check_eq(self):
        self.assertEqual(max_integer([1, 1, 1]), 1)

    def negative_max(self):
        self.assertEqual(max_integer([-5, -3, -2, -1]), -1)
        self.assertEqual(max_integer([5, -88, -5, 6]), 6)

    def float_max(self):
        self.assertEqual(max_integer([3.2, 3.1, 3.0, 3.8]), 3.8)

    def check_str(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def error_out(self):
        with self.assertRaises(TypeError):
            max_integer(32)
        with self.assertRaises(TypeError):
            max_integer([1, (2, 3)])
        with self.assertRaises(KeyError):
            max_integer({'key': 1, 'key2': 2})
        with self.assertRaises(NameError):
            max_integer(i)


if __name__ == '__main__':
    unittest.main()
