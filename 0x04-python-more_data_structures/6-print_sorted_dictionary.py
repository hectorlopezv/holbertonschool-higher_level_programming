#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for keys_ in sorted(a_dictionary):
        print('{}: {}'.format(keys_, a_dictionary.get(keys_)))
