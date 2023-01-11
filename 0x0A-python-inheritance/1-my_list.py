#!/usr/bin/python3
'''Defines a class MyList'''


class MyList(list):
    '''Inherits from a class list'''

    def print_sorted(self):
        '''prints the list, but sorted'''

        print(sorted(self))
