#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a and not tuple_b:
        return (0, 0)
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    len_a_b = len_a - len_b
    if len_a > len_b:
        tuple_new = tuple_b + tuple([0 for elem in range(len_a_b)])
        return tuple(map(lambda i, j: i + j, tuple_a[0:2], tuple_new[0:2]))
    elif len_b > len_a:
        tuple_new = tuple_a + tuple([0 for elem in range(-1 * len_a_b)])
        return tuple(map(lambda i, j: i + j, tuple_new[0:2], tuple_b[0:2]))
    elif len_a == len_b and len_b == 1:
        tuple_a_new = tuple_a + tuple([0 for elem in range(1)])
        tuple_b_new = tuple_b + tuple([0 for elem in range(1)])
        return tuple(map(lambda i, j: i + j, tuple_a_new, tuple_b_new))
    else:
        return tuple(map(lambda i, j: i + j, tuple_a[0:2], tuple_b[0:2]))
