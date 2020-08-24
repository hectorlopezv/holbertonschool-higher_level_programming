#!/usr/bin/python3
"""status python network"""


import requests
url = 'https://intranet.hbtn.io/status'
r = requests.get(url)
print("""Body response:\n\t- type: {}\n\t- content: {}"""
      .format(type(r.text), r.text) )
