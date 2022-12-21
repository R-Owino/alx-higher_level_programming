#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A square"""
    def __init__(self, size=0):
        """Creates a square
        Args:
            size (int): size of the current square
        """
        self.size = size

    @property
    def size(self):
        """Sets/gets the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the created square with # character"""
        for i in range(0, self.__size):
            [print('#', end='') for j in range(self.__size)]
            print('')
        if self.__size == 0:
            print('')
