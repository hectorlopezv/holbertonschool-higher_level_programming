#!/usr/bin/python3
"""python first pick """
def find_peak(list_of_integers):
    """find peak"""
    if len(list_of_integers) == 0:
        return "None"
    
    if len(list_of_integers) == 1:
        return list_of_integers[0]
        
    for idx in range(len(list_of_integers)):
       # print(list_of_integers[idx])
        if idx > 1 and idx < len(list_of_integers)-1:
            if list_of_integers[idx] > list_of_integers[idx - 1] and list_of_integers[idx] > list_of_integers[idx + 1]:
                return list_of_integers[idx]
        if idx == 0 and list_of_integers[idx] > list_of_integers[idx + 1]:
            return list_of_integers[idx]
        if idx == len(list_of_integers)-1 and list_of_integers[idx] > list_of_integers[idx - 1]:
            return list_of_integers[idx]
