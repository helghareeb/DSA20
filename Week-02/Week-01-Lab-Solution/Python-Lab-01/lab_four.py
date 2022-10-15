# بسم الله الرحمن الرحيم

from math import pi, pow

def calculate_area(char, *args):
    if char == 't':
        return 0.5 * args[0] * args[1]
    elif char == 'r':
        return args[0] * args[1]
    elif char == 's':
        return args[0] * args[0]
    elif char == 'c':
        return pi * args[0] * args[0]
    else:
        return -1

shape = input('Enter Shape Character: ')
number_1 = int(input('Number 1: '))
if shape in ['t', 'r']:
    number_2 = int(input('Number 2: '))
    print(calculate_area(shape, number_1, number_2))
else:
    print(calculate_area(shape, number_1))

