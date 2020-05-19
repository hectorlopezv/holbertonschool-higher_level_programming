#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
    except (ValueError, TypeError) as e:
        print(e, file=stderr)
        return False
    return True
