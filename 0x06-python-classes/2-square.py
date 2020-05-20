#!/usr/bin/python3
"""class Square"""


class Square:
    """class Square
    """
    def __init__(self, size=0):
        """method

        Keywords Arguments:
            size {int} -- size of the square

        Raises:
            TypeError: if size is not a int
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
