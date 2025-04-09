import pandas as pd
import numpy as np

df = pd.read_csv("iris.csv")

# Introducing some missing values for demonstration
df.loc[0, 'sepal length (cm)'] = np.nan
df.loc[1, 'sepal width (cm)'] = ""

# Adding a timestamp column with some correct and incorrect values
df['timestamp'] = pd.Series(["2024-03-28", "2024-02-30", "invalid-date", "2023-12-15", np.nan])

df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

print("Null Values in Dataset:")
print(df.isnull().sum())

print("Empty Values in Dataset:")
print(df[df.eq("")].count())

incorrect_timestamps = df[df['timestamp'].isna()]
print("Incorrect Timestamps:")
print(incorrect_timestamps)
