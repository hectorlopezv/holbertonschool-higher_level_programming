#!/usr/bin/python3
"""Read-File"""


def number_of_lines(filename=""):
    """read_file"""

    with open(filename, encoding='utf8', errors='ignore') as f:
        counter = 0
        for counter, _ in enumerate(f, 1):
            _
        return counter
