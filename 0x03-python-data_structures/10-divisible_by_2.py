#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    return [True if element % 2 == 0 else False for element in my_list]
