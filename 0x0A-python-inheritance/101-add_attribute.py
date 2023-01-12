#!/usr/bin/python3
'''Defines a function that adds new attributes to objects if possible'''

def add_attribute(obj, attr, val):
    '''Adds a new attribute to an object
    Args:
        obj: object to add attribute to
        attr: attribute to be added
        val: value of the attribute
    Raises:
        TypeError if attribute cannot be added
    '''

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
