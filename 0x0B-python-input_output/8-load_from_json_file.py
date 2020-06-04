#!/usr/bin/python3
"""8 bject to json-file"""
import json


def load_from_json_file(filename):
    """object to json"""
    with open(filename, 'r') as f:

        return json.load(f)
