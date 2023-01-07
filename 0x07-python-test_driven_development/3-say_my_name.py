#!/usr/bin/python3
'''Defines a function say_my_name'''


def say_my_name(first_name, last_name=""):
    '''A function the prints 2 names

    Args:
        first_name(str): first name
        last_name(str): second name

    Raises:
        TypeError if first_name and last_name are not strings

    Returns:
        My name is <first name> <last name>
    '''

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print("My name is {} {}".format(first_name, last_name))
