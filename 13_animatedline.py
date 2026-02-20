import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Data
x = np.arange(0, 10, 1)
y = np.array([1, 3, 2, 5, 4, 6, 5, 7, 6, 8])

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 9)
ax.set_ylim(0, 9)
ax.set_title("Animated Line Chart")

# Create empty line
line, = ax.plot([], [], lw=2)

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Animation function
def animate(i):
    line.set_data(x[:i+1], y[:i+1])
    return line,

# Create animation
ani = animation.FuncAnimation(
    fig,
    animate,
    init_func=init,
    frames=len(x),
    interval=1000,
    blit=True
)

plt.show()