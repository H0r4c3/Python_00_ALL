'https://hackernoon.com/how-to-read-text-file-in-python'

'''
The open() function has a lot of parameters. Let’s take a look at the necessary params for reading the text file. It opens the file in a specified mode and returns a file object.

Parameters
file – A path-like object which represents the file path
mode (Optional) – The mode  is an optional parameter. It’s a string that specifies the mode in which you want to open the file.
Mode - Description:
'r' Open a file for reading mode (default if the mode is not specified)
'w' Open a file for writing. Python will create a new file if does not exist or truncates a file content if the file exists
'x' Open a file for exclusive creation.
'a' Open a file for appending the text. Creates a new file if the file does not exist.
't' Open a file in text mode. (default)
'b' Open a file in binary mode.
'+' Open a file for updating (reading and writing)
'''

# Example
file = open(r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Files\my_file.txt','r')

file.close()




'''
Methods for Reading File Contents:

There are three ways to read data from a text file:

read() : The read() function returns the read bytes in the form of a string. This method is useful when you have a small file, and you want to read the specified bytes or entire file and store it into a string variable.

readline() : The **readline() **function returns one line from a text file and returns in the form of a string.

readlines(): The **readlines() **function reads all the lines from the text file and returns each line as a string element in a list.
'''

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Files\my_file.txt'

# Example 1 – Read the Entire Text File Using the read() Function

# Program to read the entire file (absolute path) using read() function
print('\nExample 1: read()')
file = open(path, "r")
content = file.read()
print(content)
file.close()

print("\nExample 1: read() after split('\\n')")
content_list = content.split('\n')
print(content_list)


# Example 2 – Read the Specific Length of Characters in a Text File Using the read() Function

# Program to read the specific length of characters in a file using read() function
print('\nExample 2: read(20)')
file = open(path, "r")
content = file.read(20)
print(content)
file.close()


# Example 3 – Read a Single Line in a File Using the readline() Function

# Program to read single line in a file using readline() function
print('\nExample 3: readline()')
file = open(path, "r")
content = file.readline()
print(content)
file.close()


# Example 4 - Read Text File Line by Line Using the readline() Function

# Program to read all the lines in a file using readline() function
print('\nExample 4:')
file = open(path, "r")
while True:
	content=file.readline()
	if not content:
		break
	print(content)
file.close()


# Example 5 – Read All the Lines as a List in a File Using the readlines() Function

# Program to read all the lines as a list in a file using readlines() function
print('\nExample 5: readlines()')
file = open(path, "r")
content=file.readlines()
print(content)
file.close()