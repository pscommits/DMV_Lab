import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x, y = 0, 0

fig, ax = plt.subplots()
circle = plt.Circle((x, y), 0.5, color='red')
ax.add_patch(circle)

ax.set_xlim(-10,10)
ax.set_ylim(-10,10)

def move(event):
    global x, y
    if event.key == "left": x -= 1
    if event.key == "right": x +=1
    if event.key == "up": y +=1
    if event.key == "down": y -= 1
    circle.center = (x,y)

fig.canvas.mpl_connect("key_press_event", move)

def update(frame):
    return circle,

ani = FuncAnimation(fig, update, interval=60)
plt.show()