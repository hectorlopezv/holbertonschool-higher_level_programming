#!/usr/bin/python3
"""text indentation"""


def text_indentation(text):
    """text indentation: text"""
    if not isinstance(text, str) or text is None:
        raise TypeError("text must be a string")
    start = 0
    end = 0
    retu = []
    for idx, el in enumerate(text):
        if el == '.' or el == '?' or el == ':':
            end = idx + 1
            retu.append (text[start:end] + "\n")
            start = idx + 1
        elif el != ' ':
            retu.append(el)
    print("".join(retu))
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("Holberton School")   
