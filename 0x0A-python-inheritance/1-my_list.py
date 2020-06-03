#!/usr/bin/python3
"""my list"""

class MyList(list):
    """My_list

    Arguments:
        list {list} -- list object
    """

    def print_sorted(self):
        """print_sorted"""

        print(sorted(self))
    