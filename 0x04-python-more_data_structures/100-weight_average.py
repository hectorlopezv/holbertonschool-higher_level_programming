#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    y_gen_f = sum(((x * y) for x, y in my_list))
    div_gen_f = sum((y for x, y in my_list))
    return y_gen_f/div_gen_f
