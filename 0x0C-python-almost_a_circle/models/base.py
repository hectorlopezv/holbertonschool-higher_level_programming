#!/usr/bin/python3
"""Base interface for Classes"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """json_string"""

        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file class method"""

        file_name = str(cls.__name__) + ".json"

        with open(file_name, 'w') as f:
            if not list_objs:
                f.write([])
            else:
                resu = [el.to_dictionary() for el in list_objs]
                f.write(cls.to_json_string(resu))

    @staticmethod
    def from_json_string(json_string):
        """from json_String"""
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create a factory for the childs """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """load from file"""
        file_name = str(cls.__name__) + ".json"
        with open(file_name, 'r') as f:
            resu = cls.from_json_string(f.read())

        resu = [cls.create(**el) for el in resu]
        return resu
