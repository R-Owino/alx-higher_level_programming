#!/usr/bin/python3
'''Defines a function class_to_json'''


def class_to_json(obj):
    '''
    Returns the dict desc with a simple data structure
    for JSON serialization of an object

    Args:
        obj: an instance of a class
    '''

    return obj.__dict__
