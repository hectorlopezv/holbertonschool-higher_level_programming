#!/usr/bin/python3
""" function that prints a statement
    """


def say_my_name(first_name, last_name=""):
    """say_my_name: function to print in this format"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    return "My name is " + first_name + " " + last_name
