#!/usr/bin/python3
""" test for rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ test cases for rectangle"""

    def countdown(self):
        """ reset object count"""
        Base._Base__nb_objects = 0

    def test_errors(self):
        """ check if the errors are working """
        with self.assertRaises(TypeError):
            ins1 = Rectangle()

        with self.assertRaises(TypeError):
            ins2 = Rectangle(10)

        with self.assertRaises(TypeError):
            ins2 = Rectangle(10, 20, 30, 40, 50, 60)

    def test_none(self):
        """ none input """
        with self.assertRaises(TypeError):
            ins = Rectangle(None, 10)

    def test_width_height(self):
        """ testing width and height"""
        ins3 = Rectangle(10, 10)
        self.assertEqual(ins3.width, 10)
        self.assertEqual(ins3.height, 10)

    def test_negative_width_height(self):
        """ test negative values"""
        with self.assertRaises(ValueError):
            ins6 = Rectangle(-10, 20)

        with self.assertRaises(ValueError):
            ins6 = Rectangle(10, -20)

    def test_xy(self):
        """ test for position x and y"""
        ins4 = Rectangle(10, 10, 2, 3)
        self.assertEqual(ins4.x, 2)
        self.assertEqual(ins4.y, 3)

    def test_xy_neg(self):
        """ test for negative x and y """
        with self.assertRaises(ValueError):
            inst = Rectangle(1, 1, -1)

        with self.assertRaises(TypeError):
            inst0 = Rectangle(1, 1, 1.2)

    def test_id(self):
        """ test id """
        ins5 = Rectangle(10, 10, 2, 3, 8)
        self.assertEqual(ins5.id, 8)

    def test_string(self):
        """ testing string input"""
        with self.assertRaises(TypeError):
            ins = Rectangle("s", 2)

    def test_float(self):
        """ test float input"""
        with self.assertRaises(TypeError):
            insta = Rectangle(22.1, 10)

        with self.assertRaises(TypeError):
            inst = Rectangle(-22.1, 10.5)

    def test_zero_value(self):
        """ test zero input"""
        with self.assertRaises(ValueError):
            inst7 = Rectangle(1, 0)

    def test_others(self):
        """ testing other data types"""
        with self.assertRaises(TypeError):
            ins = Rectangle(12, [12])
        with self.assertRaises(TypeError):
            ins2 = Rectangle((1, 2), 3)
        with self.assertRaises(TypeError):
            ins3 = Rectangle({'hello': 1}, 2)

    def test_area(self):
        """ testing result of area"""
        ar1 = Rectangle(3, 5)
        self.assertEqual(ar1.area(), 15)

        ar2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(ar2.area(), 2)
