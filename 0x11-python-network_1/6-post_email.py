#!/usr/bin/python3
"""status python network"""
import requests
import sys

if __name__ == '__main__':

    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)
