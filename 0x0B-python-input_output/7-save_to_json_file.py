"""7 bject to json-file"""
import json


def save_to_json_file(my_obj, filename):
    """object to json"""

    return json.dump(my_obj, filename)
