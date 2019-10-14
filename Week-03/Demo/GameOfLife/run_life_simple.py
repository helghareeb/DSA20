# بسم الله الرحمن الرحيم


from life import Life
import matplotlib.pyplot as plt
import numpy as np

dim_row = 100
dim_col = 100
data = [ [ 0 * dim_col for i in range(dim_col)] * dim_row for j in range(dim_row) ]
from random import randint
for i in range(dim_row):
    for j in range(dim_col):
        data[i][j] = randint(0,1)

# print(data)

life = Life(initial=data)

fig, ax = plt.subplots()
ax.imshow(life._initial)

for i in range(100):
    # ax.cla()
    
    ax.matshow(life.next_generation())
    # ax.set_title("frame {}".format(i))
    # Note that using time.sleep does *not* work here!
    plt.pause(1)