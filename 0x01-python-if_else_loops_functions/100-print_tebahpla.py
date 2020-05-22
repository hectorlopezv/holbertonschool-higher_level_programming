#!/usr/bin/python3
for i in range(122, 96, -1):
    character = chr(i) if i % 2 == 0 else chr(i - 32)
    print('{}'.format(character), end="")
