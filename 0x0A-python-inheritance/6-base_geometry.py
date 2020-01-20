#!/usr/bin/python3
class BaseGeometry:
    """ base for geometry"""
    def area(self):
        raise Exception('area() is not implemented')
