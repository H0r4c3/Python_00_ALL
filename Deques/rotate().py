'https://www.geeksforgeeks.org/deque-in-python/'

'''
Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. 
Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, 
as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.

rotate() :- This function rotates the deque by the number specified in arguments. 
If the number specified is negative, rotation occurs to left. Else rotation is to right. 
'''

# importing "collections" for deque operations
import collections
  
# initializing deque
de = collections.deque([1, 2, 3,])

# using rotate() to rotate the deque rotates by 3 to left
de.rotate(-3)
  
# printing modified deque
print("The deque after rotating deque is : ")
print(de)