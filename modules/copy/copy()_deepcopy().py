'https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/'

'''
In Python, Assignment statements do not copy objects, they create bindings between a target and an object. When we use = operator user thinks that this creates a new object; well, it doesn’t. 
It only creates a new variable that shares the reference of the original object.

The copy() returns a shallow copy of list and deepcopy() return a deep copy of list.

The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):

A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
'''

# importing copy module
import copy
  
# initializing list 1 
li1 = [1, 2, [3,5], 4]
  
  
# using copy for shallow copy  
li2 = copy.copy(li1) 
  
# using deepcopy for deepcopy  
li3 = copy.deepcopy(li1) 


# original elements of list
print ("The original elements before deep copying")
for i in range(0,len(li1)):
    print (li1[i],end=" ")
  
print("\r")
  
# adding and element to new list
li2[2][0] = 7
  
# Change is reflected in l2 
print ("The new list of elements after deep copying ")
for i in range(0,len( li1)):
    print (li2[i],end=" ")
  
print("\r")
  
# Change is NOT reflected in original list
# as it is a deep copy
print ("The original elements after deep copying")
for i in range(0,len( li1)):
    print (li1[i],end=" ")
    
    
    
    
# Python code to demonstrate copy operations
  
# importing "copy" for copy operations
import copy
  
# initializing list 1
li1 = [1, 2, [3,5], 4]
  
# using copy to shallow copy 
li2 = copy.copy(li1)
  
# original elements of list
print ("The original elements before shallow copying")
for i in range(0,len(li1)):
    print (li1[i],end=" ")
  
print("\r")
  
# adding and element to new list
li2[2][0] = 7
  
# checking if change is reflected
print ("The original elements after shallow copying")
for i in range(0,len( li1)):
    print (li1[i],end=" ")