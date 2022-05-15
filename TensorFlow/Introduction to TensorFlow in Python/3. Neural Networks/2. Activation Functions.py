'https://campus.datacamp.com/courses/introduction-to-tensorflow-in-python/63344?ex=5'

'''
In this exercise, you will again make use of credit card data. 
The target variable, default, indicates whether a credit card holder defaults on his or her payment in the following period. 
Since there are only two options--default or not--this is a binary classification problem. While the dataset has many features, 
you will focus on just three: the size of the three latest credit card bills. Finally, you will compute predictions from your untrained network, 
outputs, and compare those the target variable, default.
'''



import tensorflow as tf
from tensorflow import Variable, keras, matmul, constant

# Construct input layer from features
inputs = constant(bill_amounts, float32)

# Define first dense layer
dense1 = keras.layers.Dense(3, activation='relu')(inputs)

# Define second dense layer
dense2 = keras.layers.Dense(2, activation='relu')(dense1)

# Define output layer
outputs = keras.layers.Dense(1, activation='sigmoid')(dense2)

# Print error for first five examples
error = default[:5] - outputs.numpy()[:5]
print(error)


# Construct input layer from borrower features
inputs = constant(borrower_features, float32)

# Define first dense layer
dense1 = keras.layers.Dense(10, activation='sigmoid')(inputs)

# Define second dense layer
dense2 = keras.layers.Dense(8, activation='relu')(dense1)

# Define output layer
outputs = keras.layers.Dense(6, activation='softmax')(dense2)

# Print first five predictions
print(outputs.numpy()[:5])


