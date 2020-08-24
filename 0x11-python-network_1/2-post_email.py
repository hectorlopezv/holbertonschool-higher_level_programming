#!/usr/bin/python3
"""python request module"""
from urllib import request
import sys

if __name__ == '__main__':

    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes

    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        html = response.read()
        print(html.decode('utf-8'))
