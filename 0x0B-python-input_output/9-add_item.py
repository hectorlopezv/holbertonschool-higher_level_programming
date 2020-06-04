#!/usr/bin/python3
"""add item"""
if __name__ == '__main__':
    import sys
    import json

    with open("add_item.json", 'w') as f:
        json.dump(sys.argv[1:], f)
