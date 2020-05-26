#!/usr/bin/python3
"""print square"""


def print_square(size):
    """ print_Squaree"""
    if isinstance(size, float) and size < 0:
        raise ValueError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if size == 0:
        print()
    else:
        print(((("#" * size) + "\n") * size)[:-1])
