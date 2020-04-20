#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        end_2 = ""
        coma = "\n"
    else:
        end_2 = " "
        coma = ","
    print('{}{}{}'.format(i // 10, i % 10, coma), end=end_2)
