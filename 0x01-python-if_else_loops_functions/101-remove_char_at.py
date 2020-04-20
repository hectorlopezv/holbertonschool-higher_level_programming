#!/usr/bin/python3
def remove_char_at(strr, n):
    temp = list(strr)
    if n >= 0 and n <= len(temp) - 1:
        del temp[n]
    return ''.join(map(str, temp))
