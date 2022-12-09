#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    target = []
    for key, val in a_dictionary.items():
        if val is value:
            target.append(key)

    for i in target:
        del a_dictionary[i]
    return a_dictionary
