#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_check_max(self):
        self.assertEqual(max_integer([1, 3]), 3)
        self.assertEqual(max_integer([6, 3, 65, 77]), 77)
        self.assertEqual(max_integer(), None)

    def test_check_eq(self):
        self.assertEqual(max_integer([1, 1, 1]), 1)

    def test_negative_max(self):
        self.assertEqual(max_integer([-5, -3, -2, -1]), -1)
        self.assertEqual(max_integer([5, -88, -5, 6]), 6)

    def test_float_max(self):
        self.assertEqual(max_integer([3.2, 3.1, 3.0, 3.8]), 3.8)

    def test_check_str(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_error_out(self):
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
