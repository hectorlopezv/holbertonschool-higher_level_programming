#!/usr/bin/python3
"""100-append"""


def append_after(filename="", search_string="", new_string=""):
    """append_after"""

    with open(filename, 'r') as f:
        file_tmp = f.readlines()
    with open(filename, 'w') as f:
        for line in file_tmp:
            if search_string in line:
                f.write(line)
                f.write(new_string)
            else:
                f.write(line)
