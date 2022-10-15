# بسم الله الرحمن الرحيم

from my_math import do_math

# Take input from user
# input: 2 Numbers + Operation


a = input('Enter First Value: ')
b = input('Enter Second Value: ')
op = input("Enter the Required Operation - 'add' or 'mul': ")

try:
    print(do_math(int(a), int(b), operation = op))
except NameError:
    print('Please enter a vaile operation!')
except:
    print('Unknown Exception')