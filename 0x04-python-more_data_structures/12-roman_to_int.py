#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    number_value = 0
    case = {'MMM': 3000, 'MM': 2000, 'M': 1000, 'CM': 900,
            'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
            'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
            'VIII': 8, 'VII': 7, 'VI': 6, 'V': 5, 'I': 1}
    number_value += case[roman_string[0]]
    for counter, element in enumerate(roman_string[1:], 1):
        if case[element] > case[roman_string[counter - 1]]:
            number_value += case[element] - case[roman_string[counter - 1]]
            number_value -= case[roman_string[counter - 1]]
        else:
            number_value += case[element]
    return number_value
