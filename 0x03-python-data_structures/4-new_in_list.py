#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len_ = len(my_list)
    my_list_ = my_list[:]
    if idx < 0 or idx > len_:
        return my_list
    for counter, element_ in enumerate(my_list_):
        if counter == idx:
            my_list_[counter] = element
            return my_list_
