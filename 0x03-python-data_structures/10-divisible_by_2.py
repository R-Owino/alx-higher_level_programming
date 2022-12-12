#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            new_list[count] = True
        else:
            new_list[count] = False
    return new_list
