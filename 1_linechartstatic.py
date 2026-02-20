import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5,6,7])
y = np.array([0,10,20,30,40,50,60,70])

plt.figure()
plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Static Line Chart")
plt.show()