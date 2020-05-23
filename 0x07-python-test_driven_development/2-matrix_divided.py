#!/usr/bin/python3
"""
This module divides a matrix and returns a new matrix with the result.
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix

    Arguments:
        matrix {list of lists} -- A list of lists
        div {(int, float)} -- Number with whom matrix will be divided

    Raises:
        TypeError: div must be a number
        ZeroDivisionError: division by zero
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size

    Returns:
        list -- Returns a new matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = [[isinstance(item, (int, float)) for item in row]
                  for row in matrix]
    row_len = len(new_matrix[0])
    for row in new_matrix:
        if row_len != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        if not all(row) or len(matrix) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = [[float("{:.2f}".format(item / div)) for item in row]
                  for row in matrix]
    return new_matrix
