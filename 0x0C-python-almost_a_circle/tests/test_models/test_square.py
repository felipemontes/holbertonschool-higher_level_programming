#!/usr/bin/python3
""" testing for square """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    def countdown(self):
        """ reset object count"""
        Base._Base__nb_objects = 0

    def test_errors_square(self):
        """ check if the errors are working """
        with self.assertRaises(TypeError):
            ins1 = Square()

        with self.assertRaises(TypeError):
            ins2 = Square(1, 2, 3, 4, 5, 6)

        with self.assertRaises(ValueError):
            ins3 = Square(-1)

        with self.assertRaises(ValueError):
            ins4 = Square(0)

        with self.assertRaises(TypeError):
            ins5 = Square(1.2)

        with self.assertRaises(TypeError):
            ins5 = Square(-1.2)

        with self.assertRaises(TypeError):
            in6 = Square(None)

        with self.assertRaises(TypeError):
            in7 = Square('string')

        with self.assertRaises(TypeError):
            in8 = Square([1, 2, 3])

        with self.assertRaises(TypeError):
            in9 = Square((1, 2))

        with self.assertRaises(TypeError):
            in10 = Square({'holb': 'erton'})

        with self.assertRaises(TypeError):
            in11 = Square(float('inf'))

    def test_size_creation(self):
        """ test size"""
        ins6 = Square(5, 5)
        self.assertEqual(ins6.size, 5)

        ins7 = Square(8)
        self.assertEqual(ins7.size, 8)

    def test_position(self):
        """ test position """
        ins8 = Square(2, 3, 4, 5)
        self.assertEqual(ins8.x, 3)

        ins9 = Square(2, 3, 4, 5)
        self.assertEqual(ins9.y, 4)

    def test_id(self):
        """ test id """
        ins = Square(2, 3, 4, 5)
        self.assertEqual(ins.id, 5)

    def test_str(self):
        """ test of str"""
        Base._Base__nb_objects = 0

        ins1 = Square(3)
        self.assertEqual(ins1.__str__(), '[Square] (1) 0/0 - 3')

        ins2 = Square(3, 7)
        self.assertEqual(ins2.__str__(), '[Square] (2) 7/0 - 3')

        ins3 = Square(3, 7, 9, 22)
        self.assertEqual(ins3.__str__(), '[Square] (22) 7/9 - 3')

    def test_area(self):
        """ test to check the area """
        ins = Square(3)
        self.assertEqual(ins.area(), 9)

        ins1 = Square(5, 2, 1)
        self.assertEqual(ins1.area(), 25)

    def test_update(self):
        """ test to check update method"""
        ins1 = Square(1)
        ins1.update(3, 2)
        self.assertEqual(ins1.__str__(), '[Square] (3) 0/0 - 2')

        ins2 = Square(5, 2, 6)
        ins2.update(3, 3, 3, 3)
        self.assertEqual(ins2.__str__(), '[Square] (3) 3/3 - 3')

    def test_to_dictionary(self):
        """ testing to dictionary method """
        Base._Base__nb_objects = 0

        ins = Square(3)
        dic1 = {'id': 1, 'size': 3, 'x': 0, 'y': 0}
        self.assertDictEqual(ins.to_dictionary(), dic1)

        ins2 = Square(3, 9)
        dic2 = {'id': 2, 'size': 3, 'x': 9, 'y': 0}
        self.assertDictEqual(ins2.to_dictionary(), dic2)

        ins3 = Square(3, 9, 2, 5)
        dic3 = {'id': 5, 'size': 3, 'x': 9, 'y': 2}
        self.assertDictEqual(ins3.to_dictionary(), dic3)
