#!/usr/bin/python3
for i in range(0, 100):
    second_digit = i // 10
    first_digit = i % 10

    if second_digit > first_digit or second_digit == first_digit:
        continue
    if i == 89:
        end_2 = ""
        coma = "\n"
    else:
        end_2 = " "
        coma = ","
    print('{}{}{}'.format(second_digit, first_digit, coma), end=end_2)
