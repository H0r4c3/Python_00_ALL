'https://campus.datacamp.com/courses/introduction-to-tensorflow-in-python/introduction-to-tensorflow?ex=1'

import tensorflow as tf

# 0D tensor
d0 = tf.ones((1,))

# 1D tensor
d1 = tf.ones((2,))

# 2D tensor
d2 = tf.ones((2, 2))

# 3D tensor
d3 = tf.ones((2, 2, 2))

print(d3.numpy())



# Constants
from tensorflow import constant

# Define a 2x3 constant
a = constant(3, shape=[2, 3])
print(a)

# Define a 2x2 constant
b = constant([1, 2, 3, 4], shape=[2, 2])
print(b)


# Variables
a0 = tf.Variable([1, 2, 3, 4, 5, 6], dtype=tf.float32)
a1 = tf.Variable([1, 2, 3, 4, 5, 6], dtype=tf.int16)
print(a1)

import numpy as np
# Convert a1 to a numpy array and assign it to A1
A1 = np.array(a1)
print(A1)


