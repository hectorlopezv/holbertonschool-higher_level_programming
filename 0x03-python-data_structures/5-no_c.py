#!/usr/bin/python3
def no_c(my_string):
    return "".join((filter(lambda x: ord(x) not in (67, 99), my_string)))
