'https://pythontic.com/containers/deque/rotate'

'''
rotate(n)

rotate() method of python deque class rotates the sequence present in the deque object ‘n’ times.
 
If no parameter is passed, 'n' will have the default value of 1.
 
If 'n' is negative, rotation direction is right to left.
 
If 'n' is positive, rotation direction is left to right.
 
The rotate() method does not return a copy of the deque which has the new sequence. Instead, rotation is applied on the contents of the deque object itself.
'''

import collections

# Create an empty deque object
dequeObject = collections.deque()

# Add elements to the deque - left to right
dequeObject.append(1)
dequeObject.append(2)
dequeObject.append(3)
dequeObject.append(4)

# Print the deque content
print(f'Deque before any rotation: {dequeObject}')

# Rotate once in positive direction
dequeObject.rotate()

print(f'Deque after 1 positive rotation: {dequeObject}')

# Rotate twice in positive direction
dequeObject.rotate(2)

print(f'Deque after 2 more positive rotations: {dequeObject}')