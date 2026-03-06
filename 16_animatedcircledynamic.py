import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ---- USER INPUT ----
radius = float(input("Enter circle radius (example 0.5): "))
frames = int(input("Enter number of frames (example 100): "))
speed = float(input("Enter movement speed (example 0.1): "))
interval = int(input("Enter frame interval in ms (example 30): "))
y_pos = float(input("Enter Y position of circle (example 5): "))

# ---- FIGURE SETUP ----
fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Create circle using user radius
circle = plt.Circle((0, y_pos), radius)
ax.add_patch(circle)

# ---- INIT FUNCTION ----
def init():
    circle.center = (0, y_pos)
    return circle,

# ---- ANIMATION FUNCTION ----
def animate(frame):
    x = frame * speed
    y = y_pos
    circle.center = (x, y)
    return circle,

# ---- CREATE ANIMATION ----
ani = animation.FuncAnimation(
    fig,
    animate,
    frames=frames,
    init_func=init,
    interval=interval,
    blit=True
)

plt.show()