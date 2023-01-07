#!/usr/bin/python3
'''Defines a function text_indentation'''


def text_indentation(text):
    '''prints a text with 2 new lines after each of these characters: .?:

    Args:
        text(str): text to be printed

    Raises:
        TypeError: if text is not str
    '''

    if type(text) is not str:
        raise TypeError('text must be a string')

    for character in '.?:':
        text = (character + "\n\n").join(
                [line.strip(" ") for line in text.split(character)])

    print(text, end='')
