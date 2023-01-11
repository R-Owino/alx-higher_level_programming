#!/usr/bin/python3
'''Defines a function append_write'''


def append_write(filename="", text=""):
    '''Appends a string at the end of a textfile

    Args:
        filename: the file to append string to
        text: the text to append

    Returns: number of characters added
    '''

    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
