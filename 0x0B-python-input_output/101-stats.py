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
i = 1


def print_sorted(dic):
    """sorted"""
    print("File size: {}".format(file_size))
    for k, v in dic.items():
        if v > 0:
            print("{}: {}".format(k, v))


try:
    for line in sys.stdin:
        s = shlex.shlex(line, posix=True)
        s.whitespace_split = True
        s = list(s)

        if s[5] in codes:
            codes[s[5]] += 1
        file_size += int(s[6])

        if i % 10 == 0:
            print_sorted(codes)
        i += 1
except KeyboardInterrupt:
    print_sorted(codes)
