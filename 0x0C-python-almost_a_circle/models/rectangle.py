#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle classs children of Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """[summary]

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int, optional): x position in a 2d plane. Defaults to 0.
            y (int, optional): y position in a 2d plane. Defaults to 0.
            id (int, optional): "id" of the object itself. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """heigth getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getterr"""
        return self.__y

    @y.setter
    def y(self, value):
        """y settter"""
        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area method for rectangle"""
        return self.width * self.height
    """
    def display(self):
        ""graphical representation of object with #""
        print(((("#" * self.width)+ "\n")* self.height)[:-1] )
    """

    def __str__(self):
        """string representation of object"""
        return "{} ({}) {}/{} - {}/{}".format("[Rectangle]",
                                              self.id, self.x, self.y,
                                              self.width, self.height)

    def display(self):
        """display overload"""
        print("\n" * self.y, end="")
        print(
            (((" " * self.x) + ("#" * self.width) + "\n") * self.height)[:-1])

    def update_(self, id=None, width=None, height=None, x=None, y=None):
        """update aux method"""
        if id is not None:
            self.id = id

        if width is not None:
            self.width = width

        if height is not None:
            self.height = height

        if x is not None:
            self.x = x

        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update args of instance"""
        if args and len(args) != 0:
            self.update_(*args)
        else:
            self.update_(**kwargs)
