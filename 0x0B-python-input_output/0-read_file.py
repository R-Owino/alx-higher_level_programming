#!/usr/bin/python3
'''Defines a function read_file'''


def read_file(filename=""):
    '''Reads a file and prints it to stdout'''

    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end='')
