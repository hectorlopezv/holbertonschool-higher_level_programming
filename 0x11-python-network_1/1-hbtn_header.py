#!/usr/bin/python3
"""python request module"""


import urllib.request
import sys
url = sys.argv[1]

request = urllib.request.Request(url)

with urllib.request.urlopen(request) as request:
    header = request.info()
    print(header['X-Request-Id'])
