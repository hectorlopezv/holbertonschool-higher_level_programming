#!/usr/bin/python3
def element_at(my_list, idx):
    len_ = len(my_list)
    if (idx < 0) or (idx > len_):
        return None
    for counter, element in enumerate(my_list, 0):
        if counter == idx:
            return element
