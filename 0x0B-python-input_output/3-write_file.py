#!/usr/bin/python3
"""write file"""


def write_file(filename="", text=""):
    """write_file"""
    with open(filename, 'w', enconde='utf8') as f:
        f.write(text)
