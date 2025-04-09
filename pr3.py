import pandas as pd

df = pd.read_csv("iris.csv")

print("Sliced Data (Rows 1-5, Columns 1-3):")
print(df.iloc[1:5, 0:3])

print("Split Dataset into Two Parts:")
df_split1 = df.iloc[:len(df)//2]
df_split2 = df.iloc[len(df)//2:]
print("First Part:")
print(df_split1)
print("Second Part:")
print(df_split2)

print("Merged Dataset:")
df_merged = pd.concat([df_split1, df_split2])
print(df_merged)
