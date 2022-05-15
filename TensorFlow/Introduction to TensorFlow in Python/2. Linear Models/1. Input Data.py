'https://campus.datacamp.com/courses/introduction-to-tensorflow-in-python/63343?ex=1'

# 1. Method

# Import pandas under the alias pd
import pandas as pd

# Assign the path to a string variable named data_path
data_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\TensorFlow\Introduction to TensorFlow in Python\kc_house_data.csv'

# Load the dataset as a dataframe named housing
housing = pd.read_csv(data_path)

# Print the price column of housing
print(housing['price'])

# 2. Method
# Import numpy and tensorflow with their standard aliases
import numpy as np
import tensorflow as tf

# Use a numpy array to define price as a 32-bit float
price = np.array(housing['price'], np.float32)

# Define waterfront as a Boolean using cast
waterfront = tf.cast(housing['waterfront'], tf.bool)

# Print price and waterfront
print(price)
print(waterfront)