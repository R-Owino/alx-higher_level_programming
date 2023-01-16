#!/usr/bin/python3
'''Module that defines a class Base'''


class Base:
    '''A class Base

    Private class attribute:
        __nb_objects(int): counts number of instances created
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Class constructor, initalizes a new Base instance
        Args:
            id(int): a public instance attribute
        '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
