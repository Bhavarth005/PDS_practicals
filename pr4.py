import pandas as pd

df = pd.read_csv("iris.csv")

print("Dataset Description:")
print(df.describe())

print("Maximum Values:")
print(df.max())

print("Minimum Values:")
print(df.min())

print("Mean Values:")
print(df.mean())

print("Median Values:")
print(df.median())

print("Count of Non-Null Values:")
print(df.count())

print("Standard Deviation:")
print(df.std())

print("Correlation Matrix:")
print(df.corr())
