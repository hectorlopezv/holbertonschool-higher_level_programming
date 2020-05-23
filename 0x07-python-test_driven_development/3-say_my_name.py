#!/usr/bin/python3
"""
This module prints My name is <first name> <last name>.
"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>

    Arguments:
        first_name {str} -- First name

    Keyword Arguments:
        last_name {str} -- Last name (default: {""})

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
