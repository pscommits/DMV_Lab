import matplotlib.pyplot as plt

x = list(map(str, input("Enter x values separated by space: ").split()))
y = list(map(float, input("Enter y values separated by space: ").split()))

plt.bar(x,y)
plt.title("Bar chart Example")
plt.show()