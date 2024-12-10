# -*- coding: utf-8 -*-
"""Apple Stock Price Analysis EDA

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VO6Ozu7Z0JfDd3bjTN8MwiHhE9R8plgK

**Importing Libraries**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""**Loading Dataset File**"""

data = pd.read_csv('Apple_Dataset.csv')

"""**Understand the Dataset**"""

# Get information about dataset
data.info()

# Check all columns
data.columns

# Check how many rows and columns has in the dataset
data.shape

# Display first 10 rows
data[0:10]

# Print last values
data.tail()

# Check how many null values
data.isnull().sum()

"""**Visualizing Explorative Data Analysis**

"""

# Convert Date column into datetime and set index
data['Datetime'] = pd.to_datetime(data['Date'])
print(data["Datetime"])
data.set_index('Datetime', inplace=True)

# Stock prices overtime
plt.figure(figsize=(24, 15))
plt.subplot(2, 2, 1)
sns.lineplot(data['Open'], color='red')
plt.title('Apple Stock Open Prices Over Time')
plt.xlabel('Datetime')
plt.ylabel('Opening Price (USD)')
plt.subplot(2, 2, 2)
sns.lineplot(data['Close'], color='blue')
plt.title('Apple Stock Close Prices Over Time')
plt.xlabel('Datetime')
plt.ylabel('Closing Price (USD)')
plt.subplot(2, 2, 3)
sns.lineplot(data['High'], color='orange')
plt.title('Apple Stock Highest Prices Over Time')
plt.xlabel('Datetime')
plt.ylabel('Higest Price (USD)')
plt.subplot(2, 2, 4)
sns.lineplot(data['Low'], color='green')
plt.title('Apple Stock Lowest Prices Over Time')
plt.xlabel('Datetime')
plt.ylabel('Lowest Price (USD)')
plt.savefig("price_over_time", dpi=300)
plt.show()

plt.figure(figsize=(24, 15))
plt.subplot(2, 2, 1)
sns.histplot(data['Close'], kde=True, color='red', bins=50)
plt.title('Distribution of Close Prices')
plt.xlabel('Closing Price (USD)')
plt.ylabel('Frequency')
plt.subplot(2, 2, 2)
sns.histplot(data['Open'], kde=True, color='blue', bins=50)
plt.title('Distribution of Open Prices')
plt.xlabel('Opening Price (USD)')
plt.ylabel('Frequency')
plt.subplot(2, 2, 3)
sns.histplot(data['High'], kde=True, color='orange', bins=50)
plt.title('Distribution of Highest Prices')
plt.xlabel('Highest Price (USD)')
plt.ylabel('Frequency')
plt.subplot(2, 2, 4)
sns.histplot(data['Low'], kde=True, color='green', bins=50)
plt.title('Distribution of Lowest Prices')
plt.xlabel('Lowest Price (USD)')
plt.ylabel('Frequency')
plt.savefig("price_distribution", dpi=300)
plt.show()

correlation_matrix = data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Heatmap')
plt.savefig("correlation_matrix", dpi=300)
plt.show()

plt.figure(figsize=(20,10))
plt.subplot(131)
sns.scatterplot(x='High', y='Low', data=data)
plt.title("Correlation between High and Low Prices")
plt.subplot(132)
sns.scatterplot(x='Open', y='Close', data=data)
plt.title("Correlation between Open and Close Prices")
plt.subplot(133)
sns.scatterplot(x='Volume', y='Adj Close', data=data)
plt.title("Correlation between Volume and Adjusted Close Prices")
plt.savefig("scatter_plot", dpi=300)
plt.show()

# here we are summarize stats
data.describe()