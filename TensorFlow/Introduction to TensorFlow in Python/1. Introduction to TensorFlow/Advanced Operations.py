'https://campus.datacamp.com/courses/introduction-to-tensorflow-in-python/introduction-to-tensorflow?ex=8'

'''
gradient() = Computes the sloap of a function at a point

reshape() = Reshapes a tensor

random() = Populates tensor with random entries
'''

# How to reshape a grayscale image:

import tensorflow as tf

# Generate grayscale image
gray = tf.random.uniform([2, 2], maxval=255, dtype='int32')

# Reshape grayscale image
gray = tf.reshape(gray, [2*2, 1])

print(gray)


# How to reshape a color image:

import tensorflow as tf

# Generate color image
gray = tf.random.uniform([2, 2, 3], maxval=255, dtype='int32')

# Reshape color image
gray = tf.reshape(gray, [2*2, 3])

print(gray)