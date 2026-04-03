import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
data = pd.read_csv('practicedata.csv')

# Clean price columns (remove ₹, commas, etc.)
data['Actual Price'] = data['Actual Price'].replace('[₹,]', '', regex=True).astype(float)
data['Discounted Price'] = data['Discounted Price'].replace('[₹,]', '', regex=True).astype(float)

# Take relevant columns
x = data['Actual Price']
y = data['Discounted Price']

# Remove missing values
x = x.dropna()
y = y.loc[x.index]

# Add an artificial outlier (like your reference)
x = np.append(x, 200000)   # very high actual price
y = np.append(y, 10000)    # unusually low discounted price

# Scatter plot
plt.scatter(x, y)

# Labels and title
plt.xlabel('Actual Price')
plt.ylabel('Discounted Price')
plt.title('Scatter Plot: Price Correlation with Outlier')

# Show plot
plt.show()