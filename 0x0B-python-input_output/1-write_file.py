#!/usr/bin/python3
'''Defines a function write_file'''


def write_file(filename="", text=""):
    '''Writes a string to a text file
    Args:
        filename: file to write to
        text: text to write

    Returns: Number of characters written
    '''

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
