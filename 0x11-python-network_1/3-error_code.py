#!/usr/bin/python3
"""python request module"""
from urllib import request, parse, error
import sys


url = sys.argv[1]
try:
    with request.urlopen(url) as response:
        html = response.read()
        print(html.decode('utf-8'))
except error.HTTPError as e:
    print("Error code: {}".format(e.code))
