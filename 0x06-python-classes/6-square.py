#!/usr/bin/python3
""" class of square"""


class Square:
    """class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """class square object creation

        Keyword Arguments:
            size {int} -- size int of a variable (default: {0})
        """
        self.size = size
        self.position = position

    def area(self):
        """area function returns

        Returns:
            area -- to be the area of the function
        """
        return self.__size**2

    @property
    def size(self):
        """size getter

        Returns:
            self -- return the size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """size setter

        Arguments:
            size {int} -- integer for size

        Raises:
            TypeError: if size is not a interger
            ValueError: if the number is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """my_print is going to print # accordin to size
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print("{}{}".format(" "*self.__position[0], "#"*self.__size))

    @property
    def position(self):
        """position

        Returns:
            position -- return position as a tuple
        """
        return self.__position

    @position.setter
    def position(self, value):
        """position

        Arguments:
            value {tuple} -- contains a tuple of len 2 of ints

        Raises:
            TypeError: value must be a tuple
            TypeError: value[0] must be an integer
            TypeError: value[1] must be an integer
        """
        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
