#!/usr/bin/python3
"""status python network"""


import requests
import sys

url = sys.argv[1]
r = requests.get(url)

try:
    r.raise_for_status()
    print(r.text)
except requests.exceptions.RequestException as e:
    print("Error code: {}".format(e.response.status_code))
