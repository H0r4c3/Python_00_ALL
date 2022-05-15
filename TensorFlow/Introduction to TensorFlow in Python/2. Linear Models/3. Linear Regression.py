'https://campus.datacamp.com/courses/introduction-to-tensorflow-in-python/63343?ex=7'

'''
Now that you understand how to construct loss functions, you're well-equipped to start training models. 
We'll do that for the first time in this video with a linear regression model.

Let's say we want to examine the relationship between house size and price in the King County housing dataset. 

A linear regression model assumes that the relationship between these variables can be captured by a line.

'''

import tensorflow as tf
import numpy as np
from tensorflow import keras

# Define the targets and features
price = np.array(housing['price'], np.float32)
size = np.array(housing['sqft_living'], np.float32)

# Define the intercept and slope
intercept = tf.Variable(0.1, np.float32)
slope = tf.Variable(0.1, np.float32)

# Define a linear regression model
def linear_regression(intercept, slope = slope, features = size):
    return intercept + features * slope

# Set loss_function() to take the variables as arguments
def loss_function(intercept, slope, features = size_log, targets = price_log):
	# Set the predicted values
	predictions = linear_regression(intercept, slope, features)
    
    # Return the mean squared error loss
	return keras.losses.mse(targets, predictions)

# Compute the loss for different slope and intercept values
print(loss_function(0.1, 0.1).numpy())
print(loss_function(0.1, 0.5).numpy())


# Initialize an Adam optimizer
opt = keras.optimizers.Adam(0.5)

for j in range(100):
	# Apply minimize, pass the loss function, and supply the variables
	opt.minimize(lambda: loss_function(intercept, slope), var_list=[intercept, slope])

	# Print every 10th value of the loss
	if j % 10 == 0:
		print(loss_function(intercept, slope).numpy())

# Plot data and regression line
plot_results(intercept, slope)


