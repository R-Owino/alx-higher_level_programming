#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    my_dict = a_dictionary.copy()
    for val in my_dict.keys():
        my_dict[val] *= 2
    return my_dict
