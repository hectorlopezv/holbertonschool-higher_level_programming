#!/usr/bin/python3
mod = __import__('2-replace_in_list').replace_in_list
def new_in_list(my_list, idx, element):
    len_ = len(my_list)
    my_list_ = my_list[:]
    if idx < 0 or idx > len_:
        return my_list
    return mod(my_list_, idx, element)
