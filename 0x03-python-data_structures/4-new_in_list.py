#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    my_new_list = my_list[:]
    if 0 <= idx < len(my_list):
        my_new_list[idx] = element
        return my_new_list
    return my_list


if __name__ == "__main__":
    new_in_list()