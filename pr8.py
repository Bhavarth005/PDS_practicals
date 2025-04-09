import pandas as pd 
from matplotlib import pyplot as plt

url = "https://github.com/chris1610/pbpython/blob/master/data/sample-salesv3.xlsx?raw=true"
df = pd.read_excel(url)

df['date'] = pd.to_datetime(df['date'])
daily_sales = df.groupby(df['date'].dt.date)['ext price'].sum()

plt.plot(daily_sales)
plt.title("Total Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales Amount")
plt.grid()
plt.show()
