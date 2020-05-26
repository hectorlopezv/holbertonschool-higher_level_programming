#!/usr/bin/python3
"""numpy lazy matrix multiplication"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """lazy_matrix_mul"""
    
    if not isinstance(m_a, list):
        raise TypeError("m_a not a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b not a list")
    m_a_matrix = np.array(m_a) 
    m_b_matrix = np.array(m_b)
    if np.shape(m_a_matrix)[1] < np.shape(m_b_matrix)[0]:
        raise ValueError("mxn1 , n2xp -> n1 != n2")
    return np.dot(m_a_matrix, m_b_matrix)