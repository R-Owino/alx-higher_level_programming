#!/usr/bin/python3

'''Adds 2 integers
'''


def add_integer(a, b=98):
    '''Adds 2 integers

    Args:
        a(int, float): first integer
        b(int, float): second integer
    Raises:
        TypeError if a and be are not integers
    '''

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a + b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
