#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for el in range(x):
            print('{}'.format(my_list[el]), end="")
            i += 1
    except:
        print()
        return i
    else:
        print()
        return i
