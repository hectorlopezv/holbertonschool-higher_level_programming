#!/usr/bin/python3
def uppercase(strr):
    string = list(map(lambda x: ord(x) - 32 if ord(x) >= 97
                      and ord(x) < 123 else ord(x), strr))
    for i in string:
        print('{}'.format(chr(i)), end="")
