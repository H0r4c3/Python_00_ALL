'''
The other methods perfectly work in the case of an actual file, and if you have something like file-like objects, 
you could use seek() and tell() to fetch the file size.

There are three steps involved to get the file size.

Step 1: Open the file using the open() function and store the return object into a variable. 
When the file is opened, the cursor always points to the beginning of the file.

Step 2: File objects provide a seek() method to set the cursor into the desired location. 
It accepts two arguments start position and the end position. To set the cursor at the end location of the file, use method os.SEEK_END.

Step 3: The file object has a tell() method that can get the current cursor position and provides the number of bytes it has moved from the initial position. 
Basically, it gives the actual file size in bytes format.

'''

# Import os module
import os

# set the file path
file_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Files\How_to_Get_File_Size_in_Python\Fluent Python ( PDFDrive ).pdf'
 
# open file using open() function
file = open(file_path)
 
# set the cursor position to end of file
file.seek(0, os.SEEK_END)

# get the current position of cursor
# this will be equivalent to size of file
file_size= file.tell()
 

print('File Size in Bytes is ', file_size)
print('File Size in KiloBytes is ', (file_size / 1024))
print('File Size in MegaBytes is ', (file_size / (1024 * 1024)))