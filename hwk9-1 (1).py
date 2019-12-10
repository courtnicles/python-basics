"""
DATA 200 Fall 2019 Homework 9
Courtney Nguyen
06DEC19
hw9-1.py
"""

import pandas as pd

## Quick View of Data
df = pd.read_csv('car_data.csv')
print(df.head())

print('Price of the Most Expensive Car by Company')
print(df[['company', 'price']][df.price == df.price.max()])

print('')
print('Details for Nissan and Mazda Cars')
niszda = df.loc[(df['company'] == 'nissan') | (df['company'] == 'mazda')]
print(niszda)

print('')
print('Total Number of Cars Grouped By Company')
total_cars = df.groupby(['company']).company.count()
print(total_cars)

print('')
print('Total Number of Cars Grouped By Company')
print(df.loc[df.reset_index().groupby(['company'])['price'].idxmax()])

print('')
print('Average Mileage of Cars from Each Company')
df.columns=[it.replace('average-mileage', 'mileage') for it in df.columns]
avg_mileage = df.groupby(['company']).mileage.mean()
print(avg_mileage)

import matplotlib.pyplot as plt
plt.title('Histogram of Car Prices')
plt.xlabel('Price')
df['price'].plot.hist(bins = 40)
plt.show()