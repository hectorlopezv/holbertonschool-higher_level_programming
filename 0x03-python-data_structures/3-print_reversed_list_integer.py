#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    try:
        my_list = my_list[::-1]
    except:
        return
    else:
        for element in my_list:
            print('{:d}'.format(element), end="\n")
