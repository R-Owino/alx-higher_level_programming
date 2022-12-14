#!/usr/bin/python3
'''Defines a function is_same_class'''


def is_same_class(obj, a_class):
    '''Returns True if the object is exactly an instance of the specified class
    otherwise False

    Args:
        obj: instance of a class
        a_class: the class
    '''

    if type(obj) == a_class:
        return True
    else:
        return False
