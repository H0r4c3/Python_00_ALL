'''
The os.stat() function takes a file path as an argument and returns the statistical details of the file as a tuple. 
The stat() method will get the status of the specified file path, and the st_size  attribute will fetch the file size in bytes.
'''

# Import os module
import os

# set the file path
file_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Files\How_to_Get_File_Size_in_Python\Fluent Python ( PDFDrive ).pdf'

#If you want to print the file info 
file_info= os.stat(file_path)
print(file_info)

# Get the file size using os.stat() function
file_size = os.stat(file_path).st_size

print('File Size in Bytes is ', file_size)
print('File Size in KiloBytes is ', (file_size / 1024))
print('File Size in MegaBytes is ', (file_size / (1024 * 1024)))