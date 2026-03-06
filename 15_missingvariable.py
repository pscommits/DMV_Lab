import pandas as pd

df = pd.read_csv("sampledata.csv")

print("True - missing value in the file")
print(df.isnull())

print("Total missing values")
print(df.isnull().sum())
