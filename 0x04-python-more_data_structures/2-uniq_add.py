#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_ = []
    for interger_ in my_list:
        if interger_ not in list_:
            list_.append(interger_)
    return sum(list_)
