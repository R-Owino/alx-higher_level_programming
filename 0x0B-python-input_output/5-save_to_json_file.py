#!/usr/bin/python3
'''Defines a function save_to_json_file'''

import json


def save_to_json_file(my_obj, filename):
    '''
    Writes an object to a textfile using JSON rep'n

    Args:
        my_obj: object to write
        filename: file to write to
    '''

    with open(filename, 'w', encoding='utf=8') as f:
        return json.dump(my_obj, f)
