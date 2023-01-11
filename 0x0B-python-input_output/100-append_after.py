#!/usr/bin/python3
'''Defines a function append_after'''


def append_after(filename="", search_string="", new_string=""):
    '''Inserts a line of text to a file, after each line
        containing specific string

    Args:
        filename: the file to append to
        search_string: specific string to insert after
        new_string: string to be inserted
    '''

    text = ''
    with open(filename) as f:
        for line in f:
            text += line

            if search_string in line:
                text += new_string

    with open(filename, 'w') as outfile:
        outfile.write(text)
