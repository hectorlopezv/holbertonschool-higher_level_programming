#!/usr/bin/python3
"""#13"""


class Student:
    """student"""

    def __init__(self, first_name, last_name, age):
        """student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json"""
        dic = vars(self)
        if attrs is not None:
            return dict(filter(lambda k: k[0] in attrs, dic.items()))
        return dic

    def reload_from_json(self, json):
        """reload from json"""
        for k, v in json.items():
            self.__dict__[k] = v
