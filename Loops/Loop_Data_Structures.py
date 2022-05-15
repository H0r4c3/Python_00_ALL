'''
Created on Oct 18, 2020

@author: Horace.000
'''
import pandas as pd
import numpy as np

# Dictionary
world = {"Afghanistan":30.55, "Albania":2.77, "Algeria":39.21}

for key, value in world.items():
    print(key + " -- " + str(value))
    
# numpy array
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
meas = np.array([np_height, np_weight])

# the for loop prints out an entire array on each iteration
for val in meas:
    print(val)
    
# to get every element of an array, you must use the numpy function nditer()
for val in np.nditer(meas):
    print(val)
    
cars = pd.read_csv("cars.csv", index_col = 0)

print(cars)

# the iterrow method
for label, data in cars.iterrows():
    print("label: ", label)
    print("data: ", data)
    
# print only the label and 1 column (country)
for label, data in cars.iterrows():
    print("label: ", label)
    print("data: ", data["country"])
    print(label+":"+data["country"])
    
for label, data in cars.iterrows():
    print(label + " : " + data["country"])
    
# use the "for" loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = (row["country"]).upper()
    
# use the function "apply" to call the function "len" on each country name as input and produces a new array stored as a new column "name_length"
cars["name_length"] = cars["country"].apply(len)
print(cars)

# use the function "apply" to call the function "upper" on each country name as input and produces a new array stored as a new column "COUNTRY"
cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)

    
