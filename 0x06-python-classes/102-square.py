#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A square"""

    def __init__(self, size=0):
        """Creates a square
        Args:
            size (int): size of the square
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

    def __eq__(self, other):
        """Define the == comparator"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparator"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparator"""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparator"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparator"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparator"""
        return self.area() >= other.area()
