#!/usr/bin/python3
'''Defines a class Square, inheriting from Rectangle'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Defines a square'''

    def __init__(self, size):
        '''Creates a square
        Args:
            size(int): size of the square
        '''
        self.__size = size
        super().__init__(self.__size, self.__size)
