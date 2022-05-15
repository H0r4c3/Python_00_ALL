'https://campus.datacamp.com/courses/introduction-to-tensorflow-in-python/63343?ex=4'

'''
Loss functions play a fundamental role in machine learning. 
We need loss functions to train models because they tell us how well our model explains the data.

While it is possible to define a custom loss function, this is typically not necessary, since many common options are available in TensorFlow. 
Typical choices for training linear models include the mean squared error loss (MSE), the mean absolute error loss (MAE), and the Huber loss. 
All of these are accessible from tf.keras.losses().
'''


'''
Let's say we decide to use the MSE loss. 
We'll need two tensors to compute it: the actual values or "targets" tensor and the predicted values or "predictions." 
Passing them to the MSE operation will return a single number: the average of the squared differences between the actual and predicted values.
'''

import tensorflow as tf

# Compute the MSE loss
loss = tf.keras.losses.mse(targets, predictions)

# Define a linear regression model
def linear_regression(intercept, slope = slope, features = features):
    return intercept + features * slope

# Define a loss function to compute the MSE
def loss_function(intercept, slope, targets=targets, features = features):
    # Compute the predictions for a linear model
    predictions = linear_regression(intercept, slope)
    
    # Return the loss
    return tf.keras.losses.mse(targets, predictions)


# Compute the loss for test data inputs
loss_function(intercept, slope, test_targets, test_features) # -> 10.77

# Compute the loss for default data inputs
loss_function(intercept, slope) # -> 5.43



