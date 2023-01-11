#!/usr/bin/python3
'''Defines a function to_json_string'''
import json


def to_json_string(my_obj):
    '''Returns the JSON rep'n of a string
    Args:
        my_obj(str): object to be converted to JSON
    '''
    return json.dumps(my_obj)
