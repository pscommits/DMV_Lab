import numpy as np
import matplotlib.pyplot as plt

data = np.array([1,2,3,3,4,5,2,5,6,6,7])

plt.figure()
plt.hist(data)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Static Histogram")
plt.show()