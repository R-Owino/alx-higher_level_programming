#!/usr/bin/python3
'''Defines a matrix multiplication using Numpy'''

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    '''Multiplies 2 matrices

    Args:
        m_a (list of lists of ints or float): first matrix
        m_b (list of lists of ints or float): second matrix

    Returns:
        A product of m_a and m_b in a new matrix
    '''

    return np.matmul(m_a, m_b)
