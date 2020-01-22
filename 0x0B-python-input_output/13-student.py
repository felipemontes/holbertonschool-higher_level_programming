#!/usr/bin/python3
class Student:
    """ class that defines a studen"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not isinstance(attrs, list):
            return self.__dict__
        for elem in attrs:
            if not isinstance(elem, str):
                return self.__dict__
        newdic = {}
        for string in attrs:
            if string in self.__dict__.keys():
                newdic[string] = self.__dict__[string]
        return newdic

    def reload_from_json(self, json):
        for attr in json:
            self.__dict__[attr] = json[attr]
