#!/usr/bin/python3
"""2-read_lines.py"""
number_of_lines = __import__('1-number_of_lines').number_of_lines


def read_lines(filename="", nb_lines=0):
    """Read_lines"""

    with open(filename, 'r') as f:

        for counter, line in enumerate(f):
            print(line, end="")
            if counter == nb_lines - 1:
                return
