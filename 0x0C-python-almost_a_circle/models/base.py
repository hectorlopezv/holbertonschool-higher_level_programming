#!/usr/bin/python3
"""Base interface for Classes"""


class Base(object):
    """Base interface
    Args:
        object (Baseclass): baseclass in python

    Returns:
        Base object: return a base class for children you set an id
    """

    __nb_object = 0

    def __init__(self, id=None):
        """constructor for base class

        Args:
            id (int, optional): id for base object or children.
            Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_object += 1
            self.id = type(self).__nb_object
