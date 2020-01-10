#!/usr/bin/python3
class Square:
    """ creating a class square
    """

    def __eq__(self, other):
        return self.size == other.size

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size

    def __ne__(self, other):
        return self.size != other.size

    def __gt__(self, other):
        return self.size > other.size

    def __ge__(self, other):
        return self.size >= other.size

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
