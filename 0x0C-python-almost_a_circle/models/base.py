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

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes JSON string rep'n of list_objs to a file

        Args:
            list_objs(list): list of instances inheriting from Base
        '''
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write('[]')
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        '''Returns the list of the JSON string rep'n of json_string

        Args:
            json_string(list): string rep'ing list of dictionaries
        '''
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set

        Args:
            **dictionary(dict): key/value pairs of attributes to initialize
        '''
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances'''
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as f:
                list_dict = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []
