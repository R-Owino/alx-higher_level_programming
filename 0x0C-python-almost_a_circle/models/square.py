#!/usr/bin/python3
'''Defines a class Square that inherits from Rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class Rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''class constructor, initializes a new square

        Args:
            size(int): size of the rectangle
            x(int): a square attribute
            y(int): a square attribute
            id(int): public instance attribute
        '''

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''returns the size of the square'''
        return self.width

    @size.setter
    def size(self, value):
        '''sets the value of size'''

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''overrides the __str__ method and updates the rectangle
        Args:
            *args(int): id, size, x and y in that order
            **kwargs(dict): key/value pair of attributes, skipped if *args
                            exists and is not empty
        '''
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        '''Overloading str function'''

        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)
