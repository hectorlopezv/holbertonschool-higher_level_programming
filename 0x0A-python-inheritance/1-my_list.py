#!/usr/bin/python3
"""my list"""

class MyList(list):
    """My_list

    Arguments:
        list {list} -- list object
    """

    def print_sorted(self):
        r = self[:]
        r.sort()
        print(r)
        del r
    