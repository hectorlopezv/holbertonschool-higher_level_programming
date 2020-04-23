#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    f = [my_list[0]]
    temp = f[0]
    for element in my_list:
        if element > temp:
            f.pop()
            f.append(element)
            temp = element
    return f[0]
