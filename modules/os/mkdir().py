'''
os.mkdir() method in Python is used to create a directory named path with the specified numeric mode. 
This method raise FileExistsError if the directory to be created already exists.

Syntax: os.mkdir(path, mode = 0o777, *, dir_fd = None)

Parameter:
path: A path-like object representing a file system path. A path-like object is either a string or bytes object representing a path.
mode (optional) : A Integer value representing mode of the directory to be created. If this parameter is omitted then default value Oo777 is used.
dir_fd (optional) : A file descriptor referring to a directory. The default value of this parameter is None.
If the specified path is absolute then dir_fd is ignored.
'''

import os

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\os\New_dir'

os.mkdir(path)

