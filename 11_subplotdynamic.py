import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array(list(map(int, input("Enter x values separated by space: ").split())))
y = np.array(list(map(int, input("Enter y values separated by space: ").split())))


plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array(list(map(int, input("Enter x values separated by space: ").split())))
y = np.array(list(map(int, input("Enter y values separated by space: ").split())))


plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()