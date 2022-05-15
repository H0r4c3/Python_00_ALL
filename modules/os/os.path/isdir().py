'''
os.path.isdir(path)
Return True if path is an existing directory. 
This follows symbolic links, so both islink() and isdir() can be true for the same path.
'''


import os

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\os'

print(os.path.isdir(path))