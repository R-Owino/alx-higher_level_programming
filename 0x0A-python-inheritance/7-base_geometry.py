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
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
