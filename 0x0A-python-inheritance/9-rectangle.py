#!/usr/bin/python3
"""rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, heigth):
        super().integer_validator("width", width)
        super().integer_validator("heigth", heigth)
        self.__width = width
        self.__height = heigth
    
    def area(self):
        """rectangle"""
        return self.__height * self.__width
    def __str__(self):
        """str"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
