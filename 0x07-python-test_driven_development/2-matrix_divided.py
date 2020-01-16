#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ function to divide elements of a matrix """
    size = 0
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    for rows in matrix:
        if not isinstance(rows, list):
            raise TypeError('matrix must be a matrix (list of lists) '
                            'of integers/floats')
        for elem in rows:
            size += 1
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    'matrix must be a matrix (list of lists) '
                    'of integers/floats')
    if size % 2 != 0 and size is not 1:
        raise TypeError(
            'Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    new_matrix = [[round(nums / div, 2) for nums in rows] for rows in matrix]
    return new_matrix
