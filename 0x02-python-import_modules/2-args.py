#!/usr/bin/python3
import sys
if __name__ == '__main__':
    len_ag = len(sys.argv) - 1
    number = 0 if len_ag == 0 else len_ag
    s_or = 's' if len_ag > 1 or len_ag == 0 else ''
    dot_colon = ':' if len_ag >= 1 else '.'
    print('{} argument{}{}'.format(number, s_or, dot_colon))
    if len(sys.argv) - 1 == 0:
        exit()
    for i, argument in enumerate(sys.argv[1:], 1):
        print('{}: {}'.format(i, argument))
