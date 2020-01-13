#!/usr/bin/python3
def matrix_divided(matrix, div):
    size = 0
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for rows in matrix:
        for elem in rows:
            size += 1
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    'matrix must be a matrix (list of lists) of integers/floats')
    if size % 2 != 0:
        raise TypeError(
            'Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    new_matrix = [[round(nums / div, 2) for nums in rows] for rows in matrix]
    return new_matrix
