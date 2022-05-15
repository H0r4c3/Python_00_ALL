'''
path. splitext() method in Python is used to split the path name into a pair root and ext (tuple of strings).
'''

import os

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\os.path\splitext().py'
name, ext = os.path.splitext(path)

print(f'path & name = {name}')
print(f'extension = {ext}')
print(os.path.splitext(path))