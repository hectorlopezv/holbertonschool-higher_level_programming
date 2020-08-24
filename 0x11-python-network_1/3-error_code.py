#!/usr/bin/python3
"""python request module"""

from urllib import request
import sys
url = sys.argv[1]

request =  request.Request(url)
try:
    with request.urlopen(request) as response:
        html = response.read()
        print(html.decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
