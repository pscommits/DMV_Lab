import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,15,25,30]

plt.plot(x, y, marker='o')

plt.xlabel("X labels (Inependent variables)")
plt.ylabel("Y labels (Dependent variable)")

plt.title("X-Y axis Data Plot")

plt.grid(False)

plt.show()