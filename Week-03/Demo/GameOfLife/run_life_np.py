# بسم الله الرحمن الرحيم


from life_np import Life
import matplotlib.pyplot as plt
import numpy as np

dim_row = 200
dim_col = 200

data = np.random.random_integers(0,1,(dim_row,dim_col))

# print(data)

life = Life(initial=data)

fig, ax = plt.subplots()
ax.imshow(life._initial)

for i in range(100):
    ax.cla()
    ax.imshow(life.next_generation())
    # ax.set_title("frame {}".format(i))
    # Note that using time.sleep does *not* work here!
    plt.pause(1)