#!/usr/bin/python3
'''Inheriting a class BaseGeometry'''

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''Defines a Rectangle, a derived class of BaseGeometry'''

    def __init__(self, width, height):
        '''Creates a rectangle
        Args:
            width(int): the width of the rectangle
            height(int): the height of the rectangle
        Raises:
            TypeError: if width or height is not int
            ValueError: if width or height is less or equal to 0
        '''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
