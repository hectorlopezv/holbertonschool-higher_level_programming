#!/usr/bin/python3
"""write file"""


def append_write(filename="", text=""):
    """write_file"""
    with open(filename, 'a') as f:
        return f.write(text)