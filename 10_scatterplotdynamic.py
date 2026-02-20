import matplotlib.pyplot as plt
import numpy as np

x = np.array(list(map(int, input("Enter x values separated by space: ").split())))
y = np.array(list(map(int, input("Enter y values separated by space: ").split())))

plt.scatter(x, y)
plt.show()