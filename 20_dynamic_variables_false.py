import matplotlib.pyplot as plt

x = list(map(str, input("Enter x values separated by space: ").split()))
y = list(map(float, input("Enter y values separated by space: ").split()))



plt.plot(x, y, marker='o')

plt.xlabel("X labels (Inependent variables)")
plt.ylabel("Y labels (Dependent variable)")

plt.title("X-Y axis Data Plot")

plt.grid(False)

plt.show()