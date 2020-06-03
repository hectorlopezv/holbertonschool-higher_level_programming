#!/usr/bin/python3
"""10-square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square"""
    def __init__(self, size):
        """size"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    
    def area(self):
        """area method overwritten"""
        return self.__size * self.__size