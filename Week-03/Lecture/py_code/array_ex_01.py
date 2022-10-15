# بسم الله الرحمن الرحيم

# Fill a 1-D array with random values, 
# then print the values

from my_array import MyArray
import random

# The constructor is called to create the array
value_list = MyArray(100)

# Fill the array with random floating-point values
for i in range(len(value_list)):
    value_list[i] = random.random()

# Print the values, one per line
for value in value_list:
    print(value)