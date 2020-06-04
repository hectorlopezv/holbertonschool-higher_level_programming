#!/usr/bin/python3
"""add item"""
if __name__ == '__main__':
    import sys

    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '8-load_from_json_file').load_from_json_file

    try:
        info = load_from_json_file('add_item.json')
    except BaseException:
        info = []

    finally:
        save_to_json_file(info + sys.argv[1:], 'add_item.json')
