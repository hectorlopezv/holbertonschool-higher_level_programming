#!/usr/bin/python3
"""14-pascal"""

def f(n):
    """pascal_triangle"""
    fact = 0
    for i in range(1,n + 1): 
        fact = fact * i 
    return fact
    
def pascal_triangle(n):
    """pascal_triangle"""
    out = []
    if n <= 0:
        return out

    for row in range(n + 1):
        resu = []
        for pos in range(row):
            x1 = f(row)
            x2 = f(pos) * f(row - pos)
            resu.append(x1 // x2)
        out.append(resu + [1])
    return out
