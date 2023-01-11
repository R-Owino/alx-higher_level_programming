#!/usr/bin/python3
'''Defines a function is_kind_of_class'''


def is_kind_of_class(obj, a_class):
    '''returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class
    otherwise False

    Args:
        obj: instance of a class
        a_class: the class
    '''
    if isinstance(obj, a_class):
        return True
    return False
