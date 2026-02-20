import numpy as np
import matplotlib.pyplot as plt

data_input = input("Enter data values:")
data = np.array(list(map(float, data_input.split())))

plt.figure()
plt.hist(data)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Dynamic Histogram")
plt.show()