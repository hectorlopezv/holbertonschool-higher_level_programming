#!/usr/bin/python3
"""2-read_lines.py"""
number_of_lines = __import__('1-number_of_lines').number_of_lines


def read_lines(filename="", nb_lines=0):
    """Read_lines"""

    with open(filename, 'r') as f:
        if nb_lines == 0:
            print(f.read())
        elif nb_lines <= number_of_lines(filename) and nb_lines > 0:
            for counter, line in enumerate(f):
                if counter < nb_lines:
                    print(line, end="")
