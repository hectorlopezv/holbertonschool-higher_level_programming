#!/usr/bin/python3
"""add integer module"""


def add_integer(a, b=98):
    """ Function that add to numbers"""
    """
    Arguments:
        a {int, float} -- integer or float variable

    Keyword Arguments:
        b {int, float} -- integer or float variable (default: {98})

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int -- return the addition for a and b
    """
    if not isinstance(a, (int, float)) or a != a or
    a == float("inf") or a == float("-inf"):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b != b or
    b == float("inf") or b == float("-inf"):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
