#!/usr/bin/python3
class Square:
    """ creating a class square
    """
    def __init__(self, size=0):
        """ Constructor method that ask for the size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ function that returns the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """ function to get the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ fuction to set a size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """function to print a square
        """
        i, b = 0, 0
        if self.__size == 0:
            print("")
        else:
            while i < self.__size:
                print("#" * self.__size)
                i += 1
