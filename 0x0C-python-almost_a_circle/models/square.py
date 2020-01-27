#!/usr/bin/python3
""" class square that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ creation of class square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns a str representation """
        strr = "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)
        return strr

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update argumes of the class"""
        l = ['id', 'size', 'x', 'y']
        if args is not None and len(args) is not 0:
            for i in range(len(args)):
                setattr(self, l[i], args[i])
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ return a dictionary representation"""
        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
