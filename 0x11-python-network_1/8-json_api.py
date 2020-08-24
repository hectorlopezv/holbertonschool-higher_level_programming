#!/usr/bin/python3
"""status python network"""
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) >= 2 else ""
    r = requests.post(url, data = {'q':q})
    r.raise_for_status()
    result = r.json()
    if not result:
        print("No result")
    else:
        print("[{}] {}".format(result.get("id"), result.get("name")))
