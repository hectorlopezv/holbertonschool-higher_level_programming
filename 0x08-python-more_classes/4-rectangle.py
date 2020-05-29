#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """constructor

        Keyword Arguments:
            width {int} -- width of the rectangle (default: {0})
            height {int} -- height of the rectangle (default: {0})
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method of the width

        Returns:
            int -- return width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the rectangle

        Arguments:
            value {int} -- value of the rectangle

        Raises:
            TypeError: if its not a integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """height getter

        Returns:
            int -- heigth of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """heigth setter

        Arguments:
            value {int} -- set heigth of the rectangle

        Raises:
            TypeError: its not a integer
            ValueError: value is less tha 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def perimeter(self):
        """perimeter

        Returns:
             -- [description]
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def area(self):
        """area of a rectangle

        Returns:
            int -- area of a rectangle
        """
        return self.height * self.width

    def __str__(self):
        """string represention for information about
            area and perimeter of a rectangle

        Returns:
            str -- information about the rectangle object
        """
        if self.width == 0 or self.height == 0:
            return ""
        return (("#" * self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        """ string represtation for object for debugging purposes

        Returns:
            object rectangle -- return string represtation of object
        """
        return "Rectangle(" + str(self.width) + "," + str(self.height) + ")"
