#!/usr/bin/python3
'''Defines a function inherits_from'''


def inherits_from(obj, a_class):
    '''Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class, otherwise False

    Args:
        obj: a class instance
        a_class: the class
    '''

    return type(obj) != a_class and isinstance(obj, a_class)
