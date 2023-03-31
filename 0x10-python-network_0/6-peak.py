#!/usr/bin/python3
# Module that defines a function find_peak

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers
    There may be more than 1 peak in the list

    Arguments:
        list_of_integers (list): the unsorted list
    """

    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
