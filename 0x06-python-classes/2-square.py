#!/usr/bin/python3
class Square:
    """Square class
    """
    def __init__(self, size=0):
        """__init__ method

        Keyword Arguments:
            size {int} -- size of the square

        Raises:
            TypeError: if size is not a int
            ValueError: if size is less than 0
        """
        if isinstance(int, size):
            raise TypeError
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size
        
        