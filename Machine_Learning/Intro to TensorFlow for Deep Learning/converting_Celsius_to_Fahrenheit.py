'''
Intro to TensorFlow for Deep Learning

https://www.udacity.com/enrollment/ud187

Feature: The input(s) to our model
Examples: An input/output pair used for training
Labels: The output of the model
Layer: A collection of nodes connected together within a neural network.
Model: The representation of your neural network
Dense and Fully Connected (FC): Each node in one layer is connected to each node in the previous layer.
Weights and biases: The internal variables of model
Loss: The discrepancy between the desired output and the actual output
MSE: Mean squared error, a type of loss function that counts a small number of large discrepancies as worse than a large number of small ones.
Gradient Descent: An algorithm that changes the internal variables a bit at a time to gradually reduce the loss function.
Optimizer: A specific implementation of the gradient descent algorithm. (There are many algorithms for this. In this course we will 
only use the “Adam” Optimizer, which stands for ADAptive with Momentum. It is considered the best-practice optimizer.)
Learning rate: The “step size” for loss improvement during gradient descent.
Batch: The set of examples used during training of the neural network
Epoch: A full pass over the entire training dataset
Forward pass: The computation of output values from input
Backward pass (backpropagation): The calculation of internal variable adjustments according to the optimizer algorithm, starting 
from the output layer and working back through each layer to the input.
'''

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import logging
import os

logging.basicConfig(level=logging.ERROR)
        
def save_model(my_model):
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Path to the "models" folder inside the script's directory
    models_folder = os.path.join(current_dir, 'models')

    # Ensure the "models" folder exists; create if it doesn't
    os.makedirs(models_folder, exist_ok=True)
    
    # Define the filepath for the new file in the "models" folder
    my_model_path = os.path.join(models_folder, 'my_model.keras')

    # Save the model to the specified path
    my_model.save(my_model_path)
    print(f"Model saved at {my_model_path}")

def compare_results(input_Celsius_list):
    correct_fahrenheit_list = [(input_celsius * 1.8 + 32) for input_celsius in input_Celsius_list]
    my_prediction_list = [my_model.predict(np.array([input_celsius])) for input_celsius in input_Celsius_list]
    my_prediction_list_float = [round(arr.item(), 1) for arr in my_prediction_list]
    print(f'My prediction Fahrenheit list: {my_prediction_list_float}')
    print(f'The correct Fahrenheit list: {correct_fahrenheit_list}')

# Dataset nr. 1
# Feature = Inputs
#celsius_q = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
# Labels = Outputs (f = c * 1.8 + 32)
#fahrenheit_a = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# Dataset nr. 2
celsius_q = np.array([
    -50, -40, -30, -20, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 
    45, 50, 60, 70, 80, 90, 100, 110, 120, 150
], dtype=float)
fahrenheit_a = np.array([c * 1.8 + 32 for c in celsius_q], dtype=float)

for i, c in enumerate(celsius_q):
    print(f'{c} degrees Celsius = {fahrenheit_a[i]} degrees Fahrenheit')

# Create the model
# We will use the simplest model, a Dense network, that will require a single layer with a single neuron
# input_shape = [1] means that the input to this layer is a single value (number of degrees Celsius)
# units = 1 means the number of neurons in the layer = how many internal variables the layer has to try to 
# learn how to solve the problem (number of degrees Fahrenheit)
# Assemble layers into the model
inputs = tf.keras.Input(shape=(1,))
layer0 = tf.keras.layers.Dense(units=1)
my_model = tf.keras.Sequential([inputs, layer0])

# Compile the model, with loss and optimizer functions
# Loss function = how far off predictions are from the desired outcome -> the loss
# Optimizer function = a way of adjusting internal values in order to reduce the loss
# The learning rate = 0.1 = the step size taken when adjusting values in the model (the range is within 0.001 and 0.1)
my_model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))

# Train the model by calling the 'fit' method
# During training, the model takes in Celsius values, perform a calculation using the current internal variables (called 'weights') and 
# output values to be the Fahrenheit equivalent
# The 'weights' are initially set randomly
# The 'epoch' argument specifies how many times this cycle should be run
# The 'verbose' argument specifies how much output the method produces
history = my_model.fit(celsius_q, fahrenheit_a, epochs=500, verbose=False)
print('Finished training the model')

# Save 'my_model' in the 'models' folder
save_model(my_model)

# Display training statistics
# The 'fit' method returns a history object. We can use this object to plot how the loss of our model goes down after each training epoch
plt.xlabel('Epoch Number')
plt.ylabel('Loss Magnitude')
plt.plot(history.history['loss'])
plt.show()

# Use the model to predict values
# So if we execute this,you can see that our model returns 211 degrees in Fahrenheit for 100 degrees Celsius.
# That is actually very good because when using the formula,you can see that a 100 degrees Celsius is 212 degrees Fahrenheit.
print(my_model.predict(np.array([100.0])))

# Repeat for 13 input values:
input_Celsius_list = [-40, 0, 10, 30, 50, 70, 80, 90, 120, 200, 400, 750, 1000]
compare_results(input_Celsius_list)

# Print the internal variables of the Dense layer (with 3500 examples = 7 pairs, over 500 epochs)
# Our model tuned the variables ('weights') in the Dense layer until it was able
# to return the correct Fahrenheit value for any Celsius value
print(f'These are the layer variables:, {layer0.get_weights()}')

# For fun, what if we create more Dense layers with different units (more variables)
