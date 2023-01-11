#!/usr/bin/python3
'''Defines a function lookup'''


def lookup(obj):
    '''Returns the list of available attributes and methods of an object
    Args:
        obj: the object to look up
    '''

    return dir(obj)
