#!/usr/bin/python3
"""101-stats"""


import sys
import signal
import shlex
"""
#signal.signal(signal.SIGINT, print_stats)


# <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
# <status code> <file size>
"""

file_size = 0
codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0}
i = 0


def print_sorted():
    """sorted"""

    print("File size: {:d}".format(file_size))
    for x in sorted(codes.keys()):
        if codes[x] != 0:
            print("{:s}: {:d}".format(x, codes[x]))


try:
    for line in sys.stdin:
        s = shlex.shlex(line, posix=True)
        s.whitespace_split = True
        s = list(s)
        if s[5] in codes:
            codes[s[5]] += 1
        file_size += int(s[6])
        i += 1
        if i % 10 == 0:
            print_sorted()
except KeyboardInterrupt as e: 
    print_sorted()
