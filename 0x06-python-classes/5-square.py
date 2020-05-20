#!/usr/bin/python3
""" class of square"""
class Square:
    """class Square
    """
    def __init__(self, size=0):
        """class square object creation

        Keyword Arguments:
            size {int} -- size int of a variable (default: {0})
        """
        
        self.size = size
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
        palabra = "" if self.size < 0 else "#" * self.size
        print(((palabra + "\n") * self.size)[:-1])

my_square = Square(3)
print(my_square.area())
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")
