import pandas as pd

df = pd.read_csv("iris.csv")

print("First five rows:")
print(df.head())

print("Complete dataset:")
print(df)

print("Dataset summary:")
print(df.describe())