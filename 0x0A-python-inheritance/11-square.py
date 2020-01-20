#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ new class that inhereits from rectangle"""
    def __init__(self, size):
        super().integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return ('[Square] {}/{}').format(self.__size, self.__size)

    def area(self):
        return self.__size ** 2
