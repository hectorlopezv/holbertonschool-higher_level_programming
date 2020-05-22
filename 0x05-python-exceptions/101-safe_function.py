#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    resu = None
    try:
        resu = fct(*args)
    except BaseException as e:
        print('Exception: {}'.format(e), file=stderr)
        return resu
    return resu
