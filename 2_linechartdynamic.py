import numpy as np
import matplotlib.pyplot as plt

x_input = input("Enter x values:")
y_input = input("Enter y values:")

x = np.array(list(map(float, x_input.split())))
y = np.array(list(map(float, y_input.split())))

plt.figure()
plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Dynamic Line Chart")
plt.show()