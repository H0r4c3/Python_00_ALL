'''
os.path.join(path, *paths)
Join one or more path components intelligently. The return value is the concatenation of path and any members of *paths with exactly one directory 
separator following each non-empty part except the last, meaning that the result will only end in a separator if the last part is empty. 
If a component is an absolute path, all previous components are thrown away and joining continues from the absolute path component.
'''


# Python program to explain os.path.join() method
   
# importing os module
import os
 
# Path
path = "/home"
 
# Join various path components
print(os.path.join(path, "User/Desktop", "file.txt"))
 
 
# Path
path = "User/Documents"
 
# Join various path components
print(os.path.join(path, "/home", "file.txt"))
 
# In above example '/home'
# represents an absolute path
# so all previous components i.e User / Documents
# are thrown away and joining continues
# from the absolute path component i.e / home.