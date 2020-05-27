#!/usr/bin/python3
"""numpy lazy matrix multiplication"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """lazy_matrix_mul"""
    
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(el, list) for el in m_a) and len(m_a) > 0:
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(el, list) for el in m_b) and len(m_b) > 0:
        raise TypeError("m_b must be a list of lists")

    if all(len(el) == 0 for el in m_a) or len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    
    if all(len(el) == 0 for el in m_b) or len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    
    if not all(isinstance(el, (int, float))  for row in m_a for el in row):
        raise TypeError("m_a should contain only integers or floats")
    
    if not all(isinstance(el, (int, float))  for row in m_b for el in row):
        raise TypeError("m_b should contain only integers or floats")


    m_a_matrix = np.array(m_a) 
    m_b_matrix = np.array(m_b)
    m_a_num_rows, m_a_num_cols = m_a_matrix.shape
    m_b_num_rows, m_b_num_cols = m_b_matrix.shape
    
    if m_a_num_rows != m_a_num_cols:
        raise TypeError("each row of m_a must be of the same size")
    
    if m_b_num_rows != m_b_num_cols:
        raise TypeError("each row of m_b must be of the same size")
    
    if m_a_num_cols != m_b_num_rows:
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a_matrix, m_b_matrix)