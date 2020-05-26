#!/usr/bin/python3
""" matrix division by integer"""


def matrix_divided(matrix, div):
    """matrix division function by integer"""

    len_matrix = None
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(in_list, list) for in_list in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    len_matrix_0 = len(matrix[0])
    if not all(len(in_list) == len_matrix_0 for in_list in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    len_matrix = len(matrix)
    for idx in range(len_matrix):
        if not all(isinstance(el, int) for el in matrix[idx]):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    for in_list in matrix:
        for el in in_list:
            matrix[matrix.index(in_list)][in_list.index(el)
                                          ] = round(el / div, 2)
    return matrix
