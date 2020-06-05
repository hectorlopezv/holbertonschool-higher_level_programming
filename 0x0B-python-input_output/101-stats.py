#!/usr/bin/python3
""" stats: script to get stats from generated http requests """
import sys
import traceback
import time

codes = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total = 0
length = 0


def print_info():
    """ prints info about parsed made so far """
    print("File size: {:d}".format(length))
    for x in sorted(codes.keys()):
        if codes[x] != 0:
            print("{:s}: {:d}".format(x, codes[x]))

try:
    for line in sys.stdin:
        length += int(line.split()[8])
        codes[line.split()[7]] += 1
        total += 1
        if total % 10 == 0:
            print_info()
except KeyboardInterrupt as e:
    print_info()