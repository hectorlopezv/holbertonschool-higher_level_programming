#!/usr/bin/python3
"""python request module"""


import urllib.request
import sys
url = sys.argv[1]

request =  urllib.request.Request(url)
try:
    with urllib.request.urlopen(request) as response:
        html = response.read()
        print(html.decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
