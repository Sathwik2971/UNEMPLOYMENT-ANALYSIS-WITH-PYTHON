# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jXeJuTtfCIso6FhuVKqGa2BcJmKdezrS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

data = pd.read_csv("Unemployment.csv")

data

data = data.dropna()
data.info()

data[' Date'] = pd.to_datetime(data[' Date'])
data.describe()

min = data[' Date'].min()
max = data[' Date'].max()
print(min,max)

plt.figure(figsize=(15,5))
plt.plot(data[' Date'], data[' Estimated Unemployment Rate (%)'])
plt.xlabel('Date')
plt.ylabel('Unemployment Rate')
plt.title('Unemployment Rate in India')
plt.show()

plt.figure(figsize=(15,5))
sns.lineplot(x=' Date',y = ' Estimated Unemployment Rate (%)',data=data)

mean_unemployment = data[' Estimated Unemployment Rate (%)'].mean()
median_unemployment = data[' Estimated Unemployment Rate (%)'].median()
print(f'Mean Unemployment Rate: {mean_unemployment}')
print(f'Median Unemployment Rate: {median_unemployment}')

rate = pd.read_csv("Unemployment_Rate.csv")
rate.info()

plt.figure(figsize=(15,5))
plt.plot(rate[' Date'],rate[' Estimated Unemployment Rate (%)'])
plt.xlabel("Date")
plt.ylabel("Unemployment Rate")
plt.title("Unemployment rate Upto 11-2020")
plt.show()

plt.figure(figsize=(15,5))
sns.lineplot(x=' Date',y = ' Estimated Unemployment Rate (%)',data=rate)

mean_unemployment = rate[' Estimated Unemployment Rate (%)'].mean()
median_unemployment = rate[' Estimated Unemployment Rate (%)'].median()
print(f'Mean Unemployment Rate during Covid-19: {mean_unemployment}')
print(f'Median Unemployment Rate during Covid-19: {median_unemployment}')