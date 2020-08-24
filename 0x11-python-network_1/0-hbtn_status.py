#!/usr/bin/python3
"""python request module"""


from urllib import request
req = request.Request('https://intranet.hbtn.io/status')
with request.urlopen(req) as response:
    html = response.read()
    print(
        """Body response:
        - type: {}
    - content: {}
    - utf8 content: {})""".format(type(html), html, html.decode('utf-8'))
    )
