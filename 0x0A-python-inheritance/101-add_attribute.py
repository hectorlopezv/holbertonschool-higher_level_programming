#!/usr/bin/python3
"""101-add"""

def add_attribute(obj, name_attm, value):
    """add_attribute"""
    
    if not hasattr(obj, "__dict__"):
       raise TypeError("can't add new attribute")

    setattr(obj, name_attm, value)