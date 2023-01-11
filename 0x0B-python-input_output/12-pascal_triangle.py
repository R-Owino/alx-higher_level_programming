#!/usr/bin/python3
'''Defines a function pascal_triangle'''


def pascal_triangle(n):
    '''Returns a list of list of ints representing a Pascal's triangle of n

    Args:
        n(int): number of rows of the triangle
    '''
    # return empty list if n <= 0
    if n <= 0:
        return []

    pascal_tri = [[1]]
    while len(pascal_tri) != n:
        tri = pascal_tri[-1]
        tmp = [1]

        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        pascal_tri.append(tmp)
    return pascal_tri
