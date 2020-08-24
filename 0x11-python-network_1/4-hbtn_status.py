#!/usr/bin/python3
"""status python network"""


import requests
url = 'https://intranet.hbtn.io/status'
r = requests.get(url)
print("""Body response:
    - type: {}
        - content: {}""".format(type(r.text), r.text) )
