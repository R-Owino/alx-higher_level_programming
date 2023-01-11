#!/usr/bin/python3
'''Defines a function from_json_string'''

import json


def from_json_string(my_str):
    '''Returns a data structure rep'n of JSON string
    Args:
        my_str(str): JSON string
    '''

    return json.loads(my_str)
