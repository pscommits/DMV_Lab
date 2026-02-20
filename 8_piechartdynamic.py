import matplotlib.pyplot as plt

labels = list(map(str, input("Enter labels values separated by space: ").split()))
sizes = list(map(float, input("Enter sizes values separated by space: ").split()))

plt.pie(sizes,labels=labels)
plt.title("Pie chart Example")
plt.show()