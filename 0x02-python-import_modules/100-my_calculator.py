#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
from sys import argv
if __name__ == '__main__':
    len_arg = len(argv) - 1
    operations = {'+': add, '-': sub, '*': mul, '/': div}
    if len_arg != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    if argv[2] in operations:
        a = int(argv[1])
        b = int(argv[3])
        result = operations[argv[2]](a, b)
        print('{:d} {} {:d} = {:d}'.format(a, argv[2], b, result))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
