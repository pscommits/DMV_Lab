import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('practicedata.csv')

# Extract the 'price' column
prices = data['Actual Price'].dropna()  # remove missing values if any

# Create box plot
plt.boxplot(prices)

# Labels and title
plt.xlabel('Price')
plt.title('Box plot of Price column')

# Show plot
plt.show()