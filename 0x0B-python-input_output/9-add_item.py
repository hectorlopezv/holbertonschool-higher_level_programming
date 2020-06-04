#!/usr/bin/python3
"""Load, add, save"""


import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
arguements = sys.argv[1:]
try:
    ls = load_from_json_file(filename)
    list_ = ls + arguements
    save_to_json_file(list_, filename)
except Exception:
    save_to_json_file(arguements, filename)