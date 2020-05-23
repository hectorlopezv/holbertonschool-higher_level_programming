#!/usr/bin/python3
"""
This module prints My name is <first name> <last name>.
"""


def print_square(size):
    row = 0
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        while row < size:
            print("{}".format("#" * size))
            row += 1
