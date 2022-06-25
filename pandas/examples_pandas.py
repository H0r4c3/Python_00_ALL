'''
Created on Oct 10, 2020

@author: Horace.000
'''
# Import pandas as pd
import pandas as pd

import numpy as np


# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]


# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names, 'drives_right':dr, 'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
'''print(cars)'''

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

'''
# saving the dataframe to a csv file (Excel)
cars.to_csv('cars.csv')

# Import the cars.csv data: cars without the index
cars = pd.read_csv('cars.csv', index_col=0)

# Print out cars
print(cars)

# Print only a column (if only a square brackets would have been used, the result would have been a Series, not a DataFrame)
print(cars[["country"]])

# Print only 2 rows (the second row and the third row)
print(cars[1:3])

# Using the "loc" function to select parts of the DataFrame based on labels
print(cars.loc["JPN"])
print(cars.loc[["JPN", "RU"]])
print(cars.loc[["JPN", "RU"], ["country", "cars_per_cap"]]) #intersection between lines and columns

# Using the "iloc" function to select parts of the DataFrame based on position (intersection between rows 2 and 4, and columns 0 and 2)
print(cars.iloc[[2,4], [0,2]])'''

# FILTERING Pandas DataFrames

# Select a column (Panda Series, NOT a Panda DataFrame)
print(cars["cars_per_cap"])

# Make the comparison (will obtain a boolean Series)
print(cars["cars_per_cap"] > 500)

# Store the boolean Series into many_cars
many_cars = cars["cars_per_cap"] > 500

# Use the boolean Series (many_cars) to subset the Pandas DataFrame
print(cars[many_cars])

# Use the logical_and from numpy to form a boolean Series
many_cars_but_less_than_800 = np.logical_and(cars["cars_per_cap"] > 500, cars["cars_per_cap"] < 800)

# Use the boolean Series (many_cars_but_less_than_800) to subset the Pandas DataFrame
print(cars[many_cars_but_less_than_800])





