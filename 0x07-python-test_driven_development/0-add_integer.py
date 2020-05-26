#!/usr/bin/python3
"""
add integer module
this module does the addition
of two numbers only
"""


def add_integer(a, b=98):
    """
    add_integer: add two integers
    """
    if not isinstance(a, (int, float)) or a != a or a == float("inf") or a == float("-inf"):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b != b or b == float("inf") or b == float("-inf"):
        raise TypeError("b must be an integer")
    return int(a) + int(b)