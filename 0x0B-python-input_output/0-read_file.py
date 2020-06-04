#!/usr/bin/python3
"""Read-File"""


def read_file(filename=""):
    """read_file"""

    with open(filename) as f:
        print(f.read())
