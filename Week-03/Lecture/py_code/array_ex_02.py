# بسم الله الرحمن الرحيم

# Count the number of occurences of each letter in a text file
from my_array import MyArray

# Create an array for the counters
the_counters = MyArray(127)
the_counters.clear(0)

# Open the text file for reading and extract each letter
the_file = open('abc.txt', 'r')
for line in the_file:
    for letter in line:
        # Return the unicode point for one character string
        code = ord(letter)
        the_counters[code] += 1
# Close the file
the_file.close()

# Print the results
for i in range(26):
    print( "%c - %4d          %c - %4d" % \
    (chr(65+i), the_counters[65+i], chr(97+i), the_counters[97+i]) )

