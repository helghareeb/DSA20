# بسم الله الرحمن الرحيم

from life import Life
import matplotlib.pyplot as plt
import numpy as np

life = Life()

from matplotlib.animation import FuncAnimation

n_frames = 49

fig = plt.figure()
plot = plt.matshow(life._initial, fignum=0)

def init():
    plot.set_data(life._initial)
    return [plot]

def update():
    plot.set_data(life.next_generation())
    return [plot]

anim = FuncAnimation(fig, update, init_func=init, frames=n_frames, interval=3, blit=True)
plt.show()
