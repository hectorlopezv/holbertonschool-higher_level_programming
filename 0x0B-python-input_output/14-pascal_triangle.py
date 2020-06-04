#!/usr/bin/python3
"""14-pascal"""
from math import factorial as f

def pascal_triangle(n):
    """pascal_triangle"""
    out = []
    for row in range(n + 1):
        resu = []
        for pos in range (row):
            x1 = f(row)
            x2 = f(pos)* f(row - pos)
            resu.append(x1 // x2)
        out.append(resu + [1])
    return out

            
            
