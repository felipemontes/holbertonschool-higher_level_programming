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
