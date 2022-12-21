#!/usr/bin/python3
"""Defines a class MagicClass"""

import math

class MagicClass:
    """Reps a circle"""

    def __init__(self, radius):
        """Creates a circle

        Args:
            radius (int or float): radius of the current circle
        """

        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Returns the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference of the circle"""
        return 2 * math.pi * self.__radius
