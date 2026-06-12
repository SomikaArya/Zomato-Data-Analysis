# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 16:10:57 2026

@author: Somika Arya
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Creating the data frame.
dataframe = pd.read_csv(
   r"F:\SOMIKA ARYA\PROJECTS\Zomato-Data-Analysis\Zomato-data-.csv")
print(dataframe.head())

#Data Cleaning and Preparation
def handleRate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)

#Convert the rate column to a float by removing denominator characters.
dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())

#Getting summary of the dataframe use df.info().
dataframe.info()

#Checking for missing or null values to identify any data gaps.
print(dataframe.isnull().sum())


#Exploring Restaurant Types
#Let's see the listed_in (type) column to identify popular restaurant categories.
sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")

#Votes by Restaurant Type
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c='green', marker='o')
plt.xlabel('Type of restaurant')
plt.ylabel('Votes')


#Identify the Most Voted Restaurant
max_votes = dataframe['votes'].max()
restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']

print('Restaurant(s) with the maximum votes:')
print(restaurant_with_max_votes)


#Online Order Availability
sns.countplot(x=dataframe['online_order'])

#Analyze Ratings
plt.hist(dataframe['rate'],bins=5)
plt.title('Ratings Distribution')
plt.show()

#Approximate Cost for Couples
couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)

#Ratings Comparison - Online vs Offline Orders
plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = dataframe)

#Order Mode Preferences by Restaurant Type
pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Heatmap')
plt.xlabel('Online Order')
plt.ylabel('Listed In (Type)')
plt.show()


plt.show()

