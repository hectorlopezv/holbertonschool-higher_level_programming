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
            retu.append(text[start:end] + "\n\n")
            start = idx + 1
        elif el == ' ':
            if idx < len(text) - 1:
                if ord(text[idx + 1]) > 32 and ord(text[idx + 1]) < 127:
                    if ord(text[idx - 1]) > 32 and ord(text[idx - 1]) < 127:
                        retu.append(el)
        elif el != ' ':
            retu.append(el)
    print("".join(retu))
