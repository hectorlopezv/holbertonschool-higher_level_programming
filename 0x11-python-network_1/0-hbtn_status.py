#!/usr/bin/python3
"""python request module"""


import urllib.request
req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    html = response.read()
    print(
        """Body response:
    - type: {}
    - content: {}
    - utf8 content: {})""".format(type(html), html, html.decode('utf-8'))
    )
