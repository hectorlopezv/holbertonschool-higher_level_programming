#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    reduce(lambda i, j: i (if i > j) else j, my_list)