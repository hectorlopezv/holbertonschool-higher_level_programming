#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        len_ = len(row) - 1
        for counter, element in enumerate(row):
            print('{:d}'.format(element), end=" " if counter != len_ else "")
        print("\n", end="")
