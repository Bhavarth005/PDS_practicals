import numpy as np
from matplotlib import pyplot as plt
from random import random

# a
x = np.arange(1, 50)
y = x*3

plt.subplot(2,2,1)
plt.title("Line Plot")
plt.plot(x,y)

# b
languages =  ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.subplot(2,2,2)
plt.title("Bar Chart")
plt.bar(languages,popularity)

#c 
colors =  ["#1f77b4", "#ff7f0e", "#2ca02c",
"#d62728", "#9467bd", "#8c564b"]
plt.subplot(2,2,3)
plt.title("Pie Chart")
plt.pie(popularity, labels=languages, colors=colors)

#d
plt.subplot(2,2,4)
numsX = np.random.randint(10, 500, 200)
numsY = np.random.randint(10, 500, 200)
plt.title("Scatter Plot")
plt.scatter(numsX, numsY)

plt.tight_layout()
plt.show()
