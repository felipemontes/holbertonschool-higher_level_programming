#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        for elem in mat:
            print("{:d}".format(elem), end=" " if mat[-1] != elem else "")
        print()
