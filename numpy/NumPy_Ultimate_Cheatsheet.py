'https://levelup.gitconnected.com/numpy-ultimate-cheatsheet-2021-9dbf8c94f64b'

import numpy as np



#Creating array
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

#Placeholder for all zeros
np.zeros(shape=(1,2))

#Placeholder for all ones
np.ones(shape=(1,2))

#Evenly spaced array (step size)
np.arange(start=5, stop=25, step=5)
#>>> [5,10,15,20]

#Evenly spaced array (sample size)
np.linspace(start=5, stop=25, num=5)
#>>> [5,10,15,20,25]

#Random array
np.random.random(size=(1,2))
#>>> [0.1, 0.2]

#I/O
#Saving array
np.save(file='numpy', arr=a)

#Saving multiple array into uncompressed .npz
np.savez(file='numpy.npz', a=[1, 2, 3], b=[4, 5, 6])

#Loading array
np.load(file='numpy.npz')

#Loading from .txt
np.loadtxt(fname='file.txt')

#Generate array from .csv
np.genfromtxt(fname='file.csv', delimiter=',')

#Save to .txt file (can only save 1D or 2D arrays)
np.savetxt(fname='file.txt', X=a)


#Properties
#Dimension of array
a.shape

#Length of array
len(a)

#Number of array dimension
a.ndim

#Datatype of array
a.dtype

#Convert datatype:
a.astype(int)


#Arithmetic
#Subtraction
c = np.subtract(b,a)
c = b - a

#Addition
c = np.add(b,a)
c = b + a

#Division
c = np.divide(b,a)
c = b/a

#Multiply
c = np.multiply(b,a)
c = b * a

#Exponent
np.exp(a)

#Square root
np.sqrt(a)

#Sine
np.sin(a)

#Cosine
np.cos(a)

#Log
np.log(a)


#Aggregate
#Sum
a.sum()

#Minimum
a.min()

#Maximum
a.max()

#Mean
a.mean()

#Median
a.median()

#Correlation coefficient
a.corrcoef()

#Standard deviation
np.std(a)


#Manipulation
#Transpose (switch dimension eg. from (2,1) to (1,2))
a.T

#Reshape
a.reshape(newshape=(2,3))

#Subsetting
a[1,2] #is similar to a[1][2]

#Boolean indexing
a[a<2] #will return elements that satisfy the condition

#Vertical concatenate or stacking (row-wise)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.vstack(tup=(a,b))
#>>>[[1,2,3],
#   [4,5,6]]

#Horizontal concatenate or stacking (column-wise)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.hstack(tup=(a,b))
#>>>[1,2,3,4,5,6]


#Bonus
#Asking for help
np.info(object=np.ndarray.dtype)

#Copying array
b = np.copy(a)

#Copying array with view (if you change one, the other one will change also) — NOT RECOMMENDED
b = a.view()