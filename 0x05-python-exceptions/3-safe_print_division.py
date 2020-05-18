#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        resu = a/b
    except ZeroDivisionError:
        resu = None
    finally:
        print('inside result: {}'.format(resu))
