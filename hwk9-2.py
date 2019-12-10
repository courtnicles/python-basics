"""
DATA 200 Fall 2019 Homework 9
Courtney Nguyen
06DEC19
hw9-1.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

df = pd.read_csv('cities.csv')
print(df.head())

df['log_pop'] = np.log10(df['population_total'])

print(df['log_pop'].min())
print(df['log_pop'].max())

plt.scatter(x=df['longd'],
            y=df['latd'],
            s=df['area_total_sq_mi'],
            c=df['log_pop'],
            alpha=0.3,
            cmap='jet')
plt.title('Cities: Area and Population')
plt.xlabel('longitude')
plt.ylabel('latitude')
cb = plt.colorbar()
cb.set_label("log$10$(population)")
plt.show()