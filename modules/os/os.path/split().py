'''
os.path.split(path)
Split the pathname path into a pair, (head, tail) where tail is the last pathname component and head is everything leading up to that. The tail part will never contain a slash; 
'''

import os

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\os.path\split().py'
path1, file_name = os.path.split(path)

print(path1)
print(file_name)