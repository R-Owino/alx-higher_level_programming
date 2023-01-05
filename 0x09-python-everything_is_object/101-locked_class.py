#!/usr/bin/python3
'''Defines a class LockedClass'''


class LockedClass:
    '''
    Has no class or object attributes
    Prevents a user from dynamically creating new instance attributes,
    except if the new instance is called first_name
    '''

    __slots__ = ['first_name']
