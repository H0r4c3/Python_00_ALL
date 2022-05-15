'''
os.walk() generate the file names in a directory tree
For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).
root : Prints out directories only from what you specified.
dirs : Prints out sub-directories from root.
files : Prints out all files from root and directories.
'''

import os

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules'
for (root, dirs, files) in os.walk(path, topdown=True):
    print (root)
    print (dirs)
    print (files)
    print ('--------------------------------')
