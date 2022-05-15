'''
os.path.basename(path)
Return the base name of pathname path. This is the second element of the pair returned by passing path to the function split().

This method internally use os.path.split() method to split the specified path into a pair (head, tail). 
os.path.basename() method returns the tail part after splitting the specified path into (head, tail) pair.
'''

# Python program to explain os.path.basename() method 
    
import os
  
path = '/home/User/Documents'
    
# Above specified path will be splited into (head, tail) pair as ('/home/User', 'Documents')

basename = os.path.basename(path)

print(basename)
  

path = '/home/User/Documents/file.txt'
  
# Above specified path will be splited into (head, tail) pair as ('/home/User/Documents', 'file.txt')

basename = os.path.basename(path)

print(basename)