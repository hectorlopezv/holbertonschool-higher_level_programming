"""7 bject to json-file"""
import json


def save_to_json_file(my_obj, filename):
    """object to json"""
    with open(filename, 'w') as f:

        return json.dump(my_obj, f)
