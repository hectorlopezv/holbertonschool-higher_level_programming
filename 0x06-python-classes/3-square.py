#!/usr/bin/python3
""" class of square"""


class Square:
    """class Square
    """
    def __init__(self, size=0):
        """creates an Square object

        Keyword Arguments:
            size {int} -- size of the Square (default: {0})

        Raises:
            TypeError: if size is not int
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area function returns

        Returns:
            [type] -- [description]
        """
        return self.__size**2
