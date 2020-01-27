#!/usr/bin/python3
""" rectagle class inhereited from base"""
from models.base import Base


class Rectangle(Base):
    """ class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """ returns the string representation"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    @property
    def width(self):
        """ width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

    @property
    def height(self):
        """ heigh getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ heigh setter """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

    @property
    def x(self):
        """ x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be > 0')
        else:
            self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be > 0')
        else:
            self.__y = y

    def area(self):
        """ calculation of the area"""
        return self.__width * self.__height

    def display(self):
        """ prints the rectangle"""
        if self.__y is 0:
            pass
        else:
            print('\n' * self.__y, end='')
        for i in range(self.__height):
            print("{}{}".format(' ' * self.__x, '#' * self.__width))

    def update(self, *args, **kwargs):
        """ updates the information """
        l = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) is not 0:
            for i in range(len(args)):
                setattr(self, l[i], args[i])
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns a dictionary representation"""
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
