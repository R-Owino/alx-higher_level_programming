#!/usr/bin/python3
'''Defines a class BaseGeometry'''


class BaseGeometry:
    '''Defines BaseGeometry'''
    def area(self):
        '''Public instance method that raises an exception'''
        raise Exception('area() is not implemented')
