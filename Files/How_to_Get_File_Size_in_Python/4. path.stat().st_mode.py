'''
The stat() method of the Path object returns the properties of a file like st_mode, st_dev, etc. and, 
the st_size attribute of the stat method returns the file size in bytes.
'''

# Import pathlib module
import pathlib

# set the file path
file_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Files\How_to_Get_File_Size_in_Python\Fluent Python ( PDFDrive ).pdf'

# Get the file size using pathlib.Path() function
file_size = pathlib.Path(file_path).stat().st_size

print('File Size in Bytes is ', file_size)
print('File Size in KiloBytes is ', (file_size / 1024))
print('File Size in MegaBytes is ', (file_size / (1024 * 1024)))