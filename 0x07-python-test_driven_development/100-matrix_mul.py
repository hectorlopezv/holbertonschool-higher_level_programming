#!/usr/bin/python3
"""matrix mul"""


def matrix_mul(m_a, m_b):
    """matrix_mul"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(el, list) for el in m_a) and len(m_a) > 0:
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(el, list) for el in m_b) and len(m_b) > 0:
        raise TypeError("m_b must be a list of lists")

    if any(len(el) == 0 for el in m_a) or len(m_a) == 0:
        raise ValueError("m_a can't be empty")

    if any(len(el) == 0 for el in m_b) or len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(el, (int, float)) for row in m_a for el in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(el, (int, float)) for row in m_b for el in row):
        raise TypeError("m_b should contain only integers or floats")

    m_a_num_rows = len(m_a)
    m_a_num_cols = len(m_a[0])
    m_b_num_rows = len(m_b)
    m_b_num_cols = len(m_b[0])

    if not all(len(in_list) == m_a_num_cols for in_list in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(in_list) == m_b_num_cols for in_list in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if m_a_num_cols != m_b_num_rows:
        raise ValueError("m_a and m_b can't be multiplied")

    resu = []
    for i in range(m_a_num_rows):
        temp_list = []
        for z in range(m_b_num_cols):
            temp = 0
            for j in range(m_a_num_cols):
                temp += m_a[i][j] * m_b[j][z]
            temp_list.append(temp)
        resu.append(temp_list)
    return resu
