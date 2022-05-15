'https://campus.datacamp.com/courses/introduction-to-tensorflow-in-python/introduction-to-tensorflow?ex=4'

# The addition operator

from audioop import mul
from tensorflow import constant, add

# Define 0-dimensional tensors
A0 = constant([1])
B0 = constant([2])

# Define 1-dimensional tensors
A1 = constant([1, 2])
B1 = constant([3, 4])

# Define 2-dimensional tensors
A2 = constant([[1, 2], [3, 4]] )
B2 = constant([[5, 6], [7, 8]])

# Perform tensor addition with add() (element-wise addition)
C0 = add(A0, B0)
C1 = add(A1, B1)
C2 = add(A2, B2)

from tensorflow import multiply
# Perform element-wise multiplication using multiply(A, B)
# The tensors must have the same shape
D = multiply(A1, B1)
print(f'D = multiply(A1, B1) = {multiply(A1, B1)}')

# Perform matrix multiplication using matmul(A, B)
# Numbers of columns of A must equal the number of rows of B

import tensorflow as tf
from tensorflow import ones, multiply, matmul

# Define tensors
A0 = ones(1)
A31 = ones([3, 1])
A34 = ones([3, 4], dtype=tf.int32)
A43 = ones([4, 3], dtype=tf.int32)
print(f'A34 = {A34}')
print(f'A43 = {A43}')

B1 = multiply(A0, A0)
B2 = multiply(A31, A31)
B3 = multiply(A34, A34)

# matmul = r1*c1 + r2*c2
C1 = matmul(A34, A43)
C2 = matmul(A43, A34)
print(f'matmul(A34, A43) = {matmul(A34, A43)}')
print(f'matmul(A43, A34) = {matmul(A43, A34)}')


# Sum over tensor dimensions reduce_sum()
from tensorflow import reduce_sum

A = ones([2, 3, 4])
print(A)

# Sums over all dimensions of A
B = reduce_sum(A)
print(B)

# Sums over dimension i = reduce_sum(A, i)
# Sums over dimensions 0, 1, 2
B0 = reduce_sum(A, 0)
B1 = reduce_sum(A, 1)
B2 = reduce_sum(A, 2)
print(B0)
print(B1)
print(B2)

'''
If we sum over all elements of A, we get 24, since the tensor contains 24 elements, all of which are 1. 
If we sum over dimension 1, we get a 3 by 4 matrix of 2s. If we sum over 1, we get a 2 by 4 matrix of 3s. 
And if we sum over 2, we get a 2 by 3 matrix of 4s. 
In each case, we reduce the size of the tensor by summing over one of its dimensions.
'''






