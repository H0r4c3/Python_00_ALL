'https://campus.datacamp.com/courses/introduction-to-tensorflow-in-python/63343?ex=11'

'''
Since you can't fit the entire dataset in memory, you will instead divide it into batches and train on those batches sequentially. 
A single pass over all of the batches is called an epoch and the process itself is called batch training. 
'''

import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow import keras

# Define the trainable variables
intercept = tf.Variable(10.0, np.float32)
slope = tf.Variable(0.1, np.float32)


# Define a linear regression model
def linear_regression(intercept, slope, features):
    return intercept + features * slope

# Set loss_function() to take the variables as arguments
def loss_function(intercept, slope, features, targets):
	# Set the predicted values
	predictions = linear_regression(intercept, slope, features)
    
    # Return the mean squared error loss
	return keras.losses.mse(targets, predictions)

# Define an Adam optimizer
opt = keras.optimizers.Adam()

# Load the data in batches from pandas
path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\TensorFlow\Introduction to TensorFlow in Python\kc_house_data.csv'
for batch in pd.read_csv(path, chunksize=100):
    # Extract the target and feature columns
    price_batch = np.array(batch['price'], np.float32)
    size_batch = np.array(batch['sqft_lot'], np.float32)
    
    # Minimize the loss function
    opt.minimize(lambda: loss_function(intercept, slope, price_batch, size_batch), var_list=[intercept, slope])
    

# Print parameter values
print(intercept.numpy(), slope.numpy())

