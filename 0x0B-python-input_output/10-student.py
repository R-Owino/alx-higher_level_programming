#!/usr/bin/python3
'''Defines a class Student'''


class Student:
    '''Defines a student'''

    def __init__(self, first_name, last_name, age):
        '''Initializes a student
        Args:
            first_name(str): first name
            last_name(str): last name
            age(int): age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves a dict rep'n of a student instance
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved, otherwise retrieve all attrs.

        Args:
            attrs(list): attributes to retrieve
        '''

        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
