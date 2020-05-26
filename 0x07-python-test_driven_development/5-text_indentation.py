#!/usr/bin/python3
"""
This class prints a text with 2 new lines after each of these characters: .?:
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: .?:
    Arguments:
        text {str} -- text of testing
    Raises:
        TypeError: text must be a string
    """
    if text is None or not isinstance(text, str) or len(text) < 0:
        raise TypeError("text must be a string")
    new_line = []
    for line in text:
        if line not in "?.:":
            new_line.append(line)
        else:
            line += "\n\n"
            new_line.append(line)
    new_line = "".join(new_line)
    new_line_aux = []
    for line in new_line.split("\n"):
        line = line.strip()
        new_line_aux.append(line)
    print("\n".join(new_line_aux), end=""))