#!/usr/bin/python3
'''Defines a class Student'''


class Student:
    '''Defines a student'''

    def __init__(self, first_name, last_name, age):
        '''Initializes a student
        Args:
            first_name(str): first name
            last_name(str): last name
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Retrieves a dict rep'n of a student instance'''
        return self.__dict__
