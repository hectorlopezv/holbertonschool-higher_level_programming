#!/usr/bin/python3
"""python first pick """
def find_peak(list_of_integers):
    """find peak"""
    if len(list_of_integers) == 0:
        return "None"
    
    if len(list_of_integers) == 1:
        return list_of_integers[0]
        
    lower = 0
    upper = len(list_of_integers) - 1

    while lower < upper:
        """until they meet break"""
        mid = lower + (upper - lower)//2

        if list_of_integers[mid] < list_of_integers[mid+1]: #proof index is not a peak
            lower = mid + 1 #condition because we know mid+1 is greater.....
        else:
            upper = mid
    return lower