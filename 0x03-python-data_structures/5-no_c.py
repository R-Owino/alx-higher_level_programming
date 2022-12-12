#!/usr/bin/python3

def no_c(my_string):
    str_new = ''
    for character in my_string:
        if character not in 'Cc':
            str_new += character
    return str_new
