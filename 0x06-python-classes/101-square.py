#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class
    """
    
    def __init__(self, size=0, position=(0,0)):
        """constructor for Square class

        Keyword Arguments:
            size {int} -- size of a square (default: {0})
            position {tuple} -- position in a x,y plane (default: {(0,0)})
        """
        self.size = size
        self.position = position
   
    @property    
    def size(self):
        """size getter

        Returns:
            int -- return size 
        """
        return self.__size
    @size.setter
    def size(self, value):
        """setter

        Arguments:
            value {int} -- set size with integer

        Raises:
            TypeError: if size is not a integer
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    @property
    def position(self):
        """position getter

        Returns:
            tuple -- return tuple of 2 elemetns
        """
        return self.__position
    @position.setter
    def position(self, value):
        """position setter

        Arguments:
            value {tuple} -- tuple of 2 positions

        Raises:
            TypeError: if not a tuple or not a integer(elements) 
        """
        if isinstance(value, tuple) and len(value) == 2:
            a,b = value
            if isinstance(a, int ) and isinstance(b, int):
                self.__position = value
        else:
            raise TypeError("position must be a tupe of 2 positive integer")

    def area(self):
        """are method

        Returns:
            int -- area of a circle
        """
        return self.__size**2

    def my_print(self):
        """my print method
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print("{}{}".format(" "*self.__position[0], "#"*self.__size))
    
    def __str__(self):
        """str

        Returns:
            str -- string representation for the Square class
        """
        resu = ""
        if self.__size == 0:
            return resu
        for _ in range(self.__position[1]):
            resu += "\n"
        for _ in range(self.__size):
            resu += " "*self.__position[0]+"#"*self.__size+"\n"
        return resu[:-1]

        


