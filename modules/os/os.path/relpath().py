'''
os.path.relpath() method in Python is used to get a relative filepath to the given path either from the current working directory or from the given directory
Syntax: os.path.relpath(path, start = os.curdir)

Parameters:
path: A path-like object representing the file system path.
start (optional): A path-like object representing the file system path.
The relative path for given path will be computed with respect to the directory indicated by start. 
The default value of this parameter is os.curdir which is a constant string used by the operating system to refer to the current directory.
'''

# Python program to explain os.path.relpath() method 
    
# importing os module 
import os
  
# Path
path = r"C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\os.path\relpath().py"
  
# Path of Start directory
#start = "/home / User"
  
# Compute the relative file path to the given path from the the given start directory.
relative_path1 = os.path.relpath(path, start = os.curdir)
print(relative_path1)

relative_path2 = os.path.relpath(path, start = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules')
print(relative_path2)
  