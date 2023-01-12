#!/usr/bin/python3
'''Defines a class BaseGeometry'''


class BaseGeometry:
    '''Defines BaseGeometry'''

    def area(self):
        '''Public instance method that raises an exception'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validates value
        Args:
            name(str): name of the value
            value(int): what to be validated
        Raises:
            TypeError: if value is not int
            ValueError: if value <= 0
        '''
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


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
