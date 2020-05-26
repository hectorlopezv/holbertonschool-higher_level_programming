#!/usr/bin/python3
""" function that prints a statement
    """


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    padd = "" if len(last_name) == 0 else " "
    return "My name is " + first_name + padd + last_name
