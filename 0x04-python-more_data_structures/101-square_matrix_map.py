#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    return list(map(lambda result: list(map(lambda x: x ** 2, result)), matrix))
