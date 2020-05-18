#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    try:
        for counter, ele in enumerate(my_list[:x], 1):
            print('{}'.format(ele), end="")
    except IndexError:
        print()
        return counter
    else:
        print()
        return counter
