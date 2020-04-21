#!/usr/bin/python3
import sys
if __name__ == '__main__':
    number = 0 if len(sys.argv) - 1 == 0 else len(sys.argv) - 1
    dot_colon = '.' if len(sys.argv) - 1 == 0 else ':' if len(sys.argv) - 1 == 1 else 's:'
    print('{} argument{}'.format(number, dot_colon))
    if len(sys.argv) - 1 == 0:
        exit()
    for i, argument in enumerate(sys.argv[1:], 1):
        print('{}: {}'.format(i, argument))
