#!/usr/bin/python3
class Rectangle:
    """ defining class rectangle """

    number_of_instances = 0

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        strr = ''
        if self.__height is 0 or self.__width is 0:
            return strr
        for i in range(self.__height):
            strr += str(self.print_symbol) * self.__width + '\n'
        strr = strr[:-1]
        return strr

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__height is 0 or self.__width is 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
