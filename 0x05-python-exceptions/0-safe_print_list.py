#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    index = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            index += 1
    except IndexError:
        None
    print()
    return index
