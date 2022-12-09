#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    avg = 0
    avg2 = 0

    for x, y in my_list:
        avg += x * y
        avg2 += y
    return avg / avg2
