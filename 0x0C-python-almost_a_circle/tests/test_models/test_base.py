#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import os


class TestBase(unittest.TestCase):
    """Unittesting for class Base"""

    def countdown(self):
        """ reset counter"""
        Base._Base__nb_objects = 0

    def test_inst_num(self):
        """ test instance id"""
        ins = Base()
        ins2 = Base(2)
        ins3 = Base(-1)
        ins4 = Base(1.5)
        ins5 = Base(12345)
        self.assertEqual(ins.id, 1)
        self.assertEqual(ins2.id, 2)
        self.assertEqual(ins3.id, -1)
        self.assertEqual(ins4.id, 1.5)
        self.assertEqual(ins5.id, 12345)

    def test_inst_inf(self):
        """ test with inf number"""
        inst = Base(float('inf'))
        self.assertEqual(inst.id, float('inf'))

    def test_inst_str(self):
        """ test with a string"""
        inst = Base('str')
        self.assertEqual(inst.id, 'str')

    def test_inst_data_types(self):
        """ test with different data types"""
        inst = Base([1, 2, 3])
        inst1 = Base((1, 2))
        inst2 = Base({'key': 'value'})
        self.assertEqual(inst.id, [1, 2, 3])
        self.assertEqual(inst1.id, (1, 2))
        self.assertEqual(inst2.id, {'key': 'value'})

    def test_inst_multiple_input(self):
        """ test multiple input"""
        with self.assertRaises(TypeError):
            inst = Base(1, 2, 3)

    def test_to_json_string(self):
        """ test method to_json_string"""
        var1 = None
        ret1 = Base.to_json_string(var1)
        self.assertEqual(ret1, '[]')

        var2 = []
        ret2 = Base.to_json_string(var2)
        self.assertEqual(ret2, '[]')

        var3 = [{'holberton': 'school'}]
        ret3 = Base.to_json_string(var3)
        self.assertEqual(ret3, '[{"holberton": "school"}]')

        var4 = [{'hello': 'world'}, {'hello': 'world'}]
        ret4 = Base.to_json_string(var4)
        self.assertEqual(ret4, '[{"hello": "world"}, {"hello": "world"}]')

        var5 = [{}]
        ret5 = Base.to_json_string(var5)
        self.assertEqual(ret5, '[{}]')

    def test_from_json_string(self):
        """ test method to from_json_string"""
        var1 = None
        ret1 = Base.to_json_string(var1)
        self.assertEqual(Base.from_json_string(ret1), [])

        var2 = []
        ret2 = Base.to_json_string(var2)
        self.assertEqual(Base.from_json_string(ret2), [])

        var3 = [{}]
        ret3 = Base.to_json_string(var3)
        self.assertEqual(Base.from_json_string(ret3), [{}])

        var4 = [{'holberton': 'school'}]
        ret4 = Base.to_json_string(var4)
        self.assertEqual(Base.from_json_string(ret4), var4)

        var5 = "Hello world"
        ret5 = Base.to_json_string(var5)
        self.assertEqual(Base.from_json_string(ret5), var5)
