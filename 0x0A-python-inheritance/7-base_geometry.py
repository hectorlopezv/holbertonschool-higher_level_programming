#!/usr/bin/python3
"""base geomerty"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """area method"""
        raise Exception("is not implemented")
    
    def integer_validator(self, name, value):
        """integer_validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))