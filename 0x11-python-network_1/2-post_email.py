#!/usr/bin/python3
"""python request module"""


import urllib.request
import sys
url = sys.argv[1]
email = sys.argv[2]
values = {'email': str(email)}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')  # data should be bytes

request = urllib.request.Request(url, data)

with urllib.request.urlopen(request) as response:
    html = response.read()
    print(html.decode('utf-8'))
