#!/usr/bin/python3
""" base model"""
import json


class Base:
    """ base for new geometry forms"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns a json string"""
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves on a file a json string"""
        fname = "{}.json".format(cls.__name__)
        newdic = []

        if list_objs is not None:
            for i in range(len(list_objs)):
                newdic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(newdic)

        with open(fname, 'w') as f:
            f.write(lists)

    def from_json_string(json_string):
        """ returns a json string inside a list"""
        if not json_string or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ creates an instance with the attr"""
        if cls.__name__ == "Rectangle":
            newinsta = cls(1, 1)
        elif cls.__name__ == "Square":
            newinsta = cls(1)
        newinsta.update(**dictionary)
        return newinsta

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        fname = '{}.json'.format(cls.__name__)
        try:
            with open(fname, 'r') as f:
                newl = cls.from_json_string(f.read())
                return [cls.create(**i) for i in newl]
        except:
            return []
