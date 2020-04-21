#!/usr/bin/python3
from sys import argv
from functools import reduce
if __name__ == '__main__':
    len_ag = len(argv) - 1
    def add(x, y): return int(x) + int(y)
    result = 0 if len_ag == 0 else reduce(add, argv[1:])
    print('{}'.format(result))
