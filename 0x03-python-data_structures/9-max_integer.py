#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    f = [0]
    temp = 0
    for element in my_list:
        if element > temp:
            f.pop()
            f.append(element)
            temp = element
    return f[0]
