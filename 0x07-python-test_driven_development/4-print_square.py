#!/usr/bin/python3
'''Defines a square'''


def print_square(size):
    '''
    Prints a square

    Args:
        size(int): length of the square

    Raises:
        TypeError if: - size is not int
                      - size is float and less than 0
        ValueError if size < 0
    '''

    if type(size) is not int:
        raise TypeError('size must be an integer')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for i in range(size):
            print('#', end='')
        print()
