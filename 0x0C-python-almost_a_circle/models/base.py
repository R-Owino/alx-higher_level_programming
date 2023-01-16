#!/usr/bin/python3
'''Module that defines a class Base'''
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the JSON string rep'n of list_dictionaries

        Args:
            list_dictionaries(list): list of dicts
        '''
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)
