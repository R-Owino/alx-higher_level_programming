#!/usr/bin/python3
'''Defines a function that
    divides all the elements of a matrix
'''


def matrix_divided(matrix, div):
    '''Divides all elements of a matrix

    Args:
        matrix(list of lists): contains the dividends, ints or floats
        div(int or float): the divisor

    Raises:
        TypeError if: - matrix is not a list of lists of ints or floats
                      - matrix rows are not of the same size
                      - div is not an int or float
        ZeroDivisionError if div is 0
    Returns:
        A new matrix representing the quotient
    '''

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
                        integers/floats.")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of \
                            integers/floats.")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of \
                    integers/floats.")
    return [[round(x / div, 2) for x in row] for row in matrix]
