#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        for elem in mat:
            if elem != 0:
                print(" ", end="")
            print("{:d}".format(elem), end="")
        print()
