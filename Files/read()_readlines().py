'''
https://appdividend.com/2021/06/21/how-to-read-file-into-list-in-python/
'''

# 1.
'''
To read a file into a list in Python, use the file.read() method to return the entire content of the file as a string
Then, use the str.split() method to split the string into a list.
The split() method returns the list of strings after breaking the given string by a specified separator.
'''

path1 = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Files\my_file.txt'
txt_file = open(path1, "r")

# The read() method
file_content = txt_file.read()
print("The file content are: ", file_content)

content_list = file_content.split(",")
txt_file.close()
print("The list after read() method and split() method is: ", content_list)


# 2.
'''
The readlines() is a built-in Python method that returns a list containing each line in the file as a list element. 
The readlines() method returns all the lines in the file as a list where each line is an item in the list object.
'''

path2 = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Files\my_file.txt'
txt_file2 = open(path2, "r")

# The readlines() method
content_list2 = txt_file2.readlines()
txt_file2.close()
print(f'The list after readlines() method is: {content_list2}')
