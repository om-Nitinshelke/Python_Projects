import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_excel('Coffe_sales.csv.xlsx',na_values=["########"])

data1=data.copy()

print(data1)

print(pd.crosstab(index=data1['coffee_name'],columns='counts',dropna=True))

print()

print(data1.dtypes)

print()

plt.hist(data1['coffee_name'],color='red',edgecolor='black',bins=8)
plt.title('Histogram of Coffe Names')
plt.xlabel('Coffe name')
plt.ylabel('Frequency')
plt.show()