#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key_ in a_dictionary.keys():
        if value in key_:
            del key_
    return a_dictionary
