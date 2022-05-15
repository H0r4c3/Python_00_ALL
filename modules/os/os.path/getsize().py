'https://itsmycode.com/how-to-get-file-size-in-python/'

'''
The os.path.getsize() function takes a file path as an argument and returns the file size in bytes. 
If the function cannot find the file or is inaccessible, or if file is deleted, Python will raise an OSError. 
'''

# Import os module
import os

# set the file path
file_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\os.path\getsize().py'

# Get the file size using os.path.getsize() function
file_size = os.path.getsize(file_path)

print('File Size in Bytes is ', file_size)
print('File Size in KiloBytes is ', (file_size / 1024))
print('File Size in MegaBytes is ', (file_size / (1024 * 1024)))