#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle
"""


class Rectangle():
    """Rectangle that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation function

        Keyword Arguments:
            width {int} -- width of the rectangle (default: {0})
            height {int} -- height of the rectangle (default: {0})
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Return width if setter checks have passed

        Returns:
            int -- width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter validates if value is >= 0

        Arguments:
            value {int} -- Value to be setted

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return height if setter checks have passed

        Returns:
            int -- height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter validates if value is >= 0

        Arguments:
            value {int} -- Value to be setted

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of a rectangle

        Returns:
            int -- area
        """
        return (self.width * self.height)

    def perimeter(self):
        """Returns perimeter of a rectangle

        Returns:
            int -- perimeter
        """
        if self.height == 0 or self.width == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        """Returns string representation

        Returns:
            str -- representation
        """
        if self.width == 0 or self.height == 0:
            return ("")
        width = ("{}".format(self.print_symbol)) * self.width
        representation = width
        for x in range(self.height - 1):
            representation += "\n" + width
        return (representation)

    def __repr__(self):
        """Returns a string representation

        Returns:
            str -- concat
        """
        return 'Rectangle(' + str(self.width) + ',' + str(self.height) + ')'

    def __del__(self):
        """Print the message when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns rect_1 if both have the same area value
        the biggest rectangle based on the area

        Arguments:
            rect_1 {class} -- instances of class Rectangle
            rect_2 {class} -- instances of class Rectangle

        Raises:
            TypeError: rect_1 must be an instance of Rectangle
            TypeError: rect_2 must be an instance of Rectangle

        Returns:
            class -- higher or equal instance class Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Rectangle instance with width == height == size

        Keyword Arguments:
            size {int} -- size of the square (default: {0})

        Returns:
            class -- Rectangle instance with square size
        """
        return (cls(size, size))
