#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
define_strings = 'Last digit of'
number_temp = (int(str(number)[-1]) if number > 0 else -1
               * int(str(number)[-1]))
if number_temp == 0:
    condition = 'and is 0'
elif number_temp < 6 and number_temp != 0:
    condition = 'and is less than 6 and not 0'
else:
    condition = 'and is greater than 5'

print('{} {} {} {} {}'.format(define_strings, number, "is",
                              number_temp, condition))
