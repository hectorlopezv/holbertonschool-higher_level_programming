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