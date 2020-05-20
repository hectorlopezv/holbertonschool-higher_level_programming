#!/usr/bin/python3
#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation
        Keyword Arguments:
            size {int} -- size of the square (default: {0})
            position {tuple} -- position of the square (default: {(0,0)})
        Raises:
            TypeError: Raises error if variable size is not an integer
            ValueError: Raises error if size is out of rang or a negative
            TypeError: Raises error if position is not a positive value
            TypeError: Raises error if position is not a positive value
            TypeError: Raises error if position is not a positive value
            TypeError: Raises error if position is not a positive value
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) is not int or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[1]) is not int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrieves the size of the square
        Returns:
            int -- size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets new value to the size of the square
        Arguments:
            value {int} -- new value of size to be set
        Raises:
            TypeError: Raises error if variable size is not an integer
            ValueError: Raises error if size is out of rang or a negative value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ retrive positional value
        Returns:
            tuple -- tuple containing coordinates of position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets new position
        Arguments:
            value {tuple} -- values to be set in tuple
        Raises:
            TypeError: Raises error if position is not a positive value
            TypeError: Raises error if position is not a positive value
            TypeError: Raises error if position is not a positive value
            TypeError: Raises error if position is not a positive value
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """squares the size to compute the area of the square
        Returns:
            int -- area of square
        """
        return self.__size ** 2

    def my_print(self):
        """prints the sqaure according to the size
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print("{}{}".format(" "*self.__position[0], "#"*self.__size))