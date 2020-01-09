#!/usr/bin/python3
class Square:
    """ creating a class square
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Constructor method that ask for the size
        and the position
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if position is tuple:
            raise TypeError(
                    "position must be a tuple of 2 positive integers")
        for num in position:
            if not isinstance(num, int) or num < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            self.__position = position

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
        if self.__size == 0:
            print("")
        else:
            for b in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)

    @property
    def position(self):
        return self.__position

    @size.setter
    def position(self, value):
        for num in value:
            if not isinstance(num, int) or num < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            self.__position = value
