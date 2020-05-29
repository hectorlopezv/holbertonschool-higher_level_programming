#!/usr/bin/python3
def magic_string():
    setattr(magic_string, 'idx', getattr(magic_string, 'idx', -1) + 1)
    return "Holberton" + ", Holberton" * getattr(magic_string, 'idx', 0)