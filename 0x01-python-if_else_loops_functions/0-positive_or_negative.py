#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    print("0 is zero")
    exit(0)

print('{} {}'.format(number, "is positive" if number > 0 else "is negative"))
# YOUR CODE HERE
