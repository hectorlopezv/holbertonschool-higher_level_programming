#!/usr/bin/python3
"""text indentation"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    start = 0
    end = 0
    for idx, el in enumerate(text):
        if el == '.' or el == '?' or el == ':':
            end = idx + 1
            print(text[start:end] + "\n")
            start = idx + 1
